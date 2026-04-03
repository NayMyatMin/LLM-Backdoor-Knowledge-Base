"""
Data Ingestion Tool
====================
Indexes source documents into raw/ and creates a manifest.
Supports: .md, .txt, .html, .pdf, .json

Usage:
  python3 run.py ingest add <file>       # Add a single source
  python3 run.py ingest scan             # Re-scan raw/ and update manifest
  python3 run.py ingest list             # List all ingested sources
"""

import json
import shutil
import sys
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from tools.utils import (
    RAW_DIR,
    CONFIG,
    file_hash,
    list_raw_files,
    now_iso,
    write_file,
    slugify,
)

console = Console()
MANIFEST_PATH = RAW_DIR / "_manifest.json"


def load_manifest():
    """Load the raw data manifest."""
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text())
    return {"sources": [], "last_updated": None}


def save_manifest(manifest):
    """Save the raw data manifest."""
    manifest["last_updated"] = now_iso()
    write_file(MANIFEST_PATH, json.dumps(manifest, indent=2))


@click.group()
def cli():
    """Data ingestion tool for the LLM Knowledge Base."""
    pass


@cli.command()
@click.argument("source", type=click.Path())
@click.option("--tag", "-t", multiple=True, help="Tags for categorization")
@click.option("--venue", "-v", default=None, help="Publication venue (e.g., NeurIPS)")
@click.option("--year", "-y", default=None, type=int, help="Publication year")
@click.option("--summary", "-s", default="", help="Brief summary of the source")
def add(source, tag, venue, year, summary):
    """Add a source file to the raw/ directory."""
    source_path = Path(source).resolve()
    if not source_path.exists():
        console.print("[red]File not found: {}[/red]".format(source))
        sys.exit(1)

    # Check extension
    supported = CONFIG["ingest"]["supported_extensions"]
    if source_path.suffix.lower() not in supported:
        console.print(
            "[red]Unsupported file type: {}. Supported: {}[/red]".format(
                source_path.suffix, supported
            )
        )
        sys.exit(1)

    # Check file size
    max_size = CONFIG["ingest"]["max_file_size_mb"] * 1024 * 1024
    if source_path.stat().st_size > max_size:
        console.print("[red]File too large (max {}MB)[/red]".format(
            CONFIG["ingest"]["max_file_size_mb"]
        ))
        sys.exit(1)

    # Copy to raw/
    dest = RAW_DIR / source_path.name
    if dest.exists():
        console.print("[yellow]File already exists in raw/: {}[/yellow]".format(dest.name))
        stem = source_path.stem
        suffix = source_path.suffix
        i = 1
        while dest.exists():
            dest = RAW_DIR / "{}_{}{}".format(stem, i, suffix)
            i += 1

    shutil.copy2(source_path, dest)
    console.print("[green]Copied to:[/green] {}".format(dest))

    # Update manifest
    manifest = load_manifest()
    entry = {
        "filename": dest.name,
        "original_path": str(source_path),
        "hash": file_hash(dest),
        "added": now_iso(),
        "tags": list(tag),
        "venue": venue,
        "year": year,
        "summary": summary,
        "compiled": False,
    }
    manifest["sources"].append(entry)
    save_manifest(manifest)
    console.print("[green]Manifest updated.[/green]")


@cli.command()
def scan():
    """Re-scan raw/ directory and update the manifest with any new files."""
    manifest = load_manifest()
    known_files = {s["filename"] for s in manifest["sources"]}
    raw_files = list_raw_files()

    new_count = 0
    for f in raw_files:
        if f.name not in known_files:
            console.print("[green]New file found:[/green] {}".format(f.name))
            entry = {
                "filename": f.name,
                "original_path": str(f),
                "hash": file_hash(f),
                "added": now_iso(),
                "tags": [],
                "venue": None,
                "year": None,
                "summary": "",
                "compiled": False,
            }
            manifest["sources"].append(entry)
            new_count += 1

    save_manifest(manifest)
    console.print(
        "\n[bold]Scan complete.[/bold] Found {} new file(s). Total: {} source(s).".format(
            new_count, len(manifest["sources"])
        )
    )


@cli.command("list")
def list_sources():
    """List all ingested sources."""
    manifest = load_manifest()
    if not manifest["sources"]:
        console.print("[yellow]No sources ingested yet. Use 'add' or 'scan'.[/yellow]")
        return

    table = Table(title="Ingested Sources")
    table.add_column("#", style="dim")
    table.add_column("File", style="cyan")
    table.add_column("Venue", style="green")
    table.add_column("Year")
    table.add_column("Tags", style="yellow")
    table.add_column("Compiled", style="magenta")
    table.add_column("Summary", max_width=50)

    for i, s in enumerate(manifest["sources"], 1):
        table.add_row(
            str(i),
            s["filename"],
            s.get("venue") or "-",
            str(s.get("year") or "-"),
            ", ".join(s.get("tags", [])) or "-",
            "Yes" if s.get("compiled") else "No",
            (s.get("summary") or "-")[:50],
        )
    console.print(table)


@cli.command()
def uncompiled():
    """List sources that haven't been compiled into wiki articles yet."""
    manifest = load_manifest()
    pending = [s for s in manifest["sources"] if not s.get("compiled")]
    if not pending:
        console.print("[green]All sources are compiled![/green]")
        return

    console.print("[bold]Uncompiled sources ({}):[/bold]\n".format(len(pending)))
    for s in pending:
        venue_info = ""
        if s.get("venue") or s.get("year"):
            venue_info = " ({}{})".format(
                s.get("venue", ""),
                " {}".format(s["year"]) if s.get("year") else "",
            )
        console.print("  - [cyan]{}[/cyan]{}".format(s["filename"], venue_info))
        console.print("    Path: raw/{}".format(s["filename"]))


@cli.command("mark-compiled")
@click.argument("filename")
def mark_compiled(filename):
    """Mark a source as compiled (after Claude Code writes its wiki article)."""
    manifest = load_manifest()
    found = False
    for s in manifest["sources"]:
        if s["filename"] == filename:
            s["compiled"] = True
            found = True
            break
    if found:
        save_manifest(manifest)
        console.print("[green]Marked '{}' as compiled.[/green]".format(filename))
    else:
        console.print("[red]Source '{}' not found in manifest.[/red]".format(filename))


@cli.command("mark-all-compiled")
def mark_all_compiled():
    """Mark all sources as compiled."""
    manifest = load_manifest()
    count = 0
    for s in manifest["sources"]:
        if not s.get("compiled"):
            s["compiled"] = True
            count += 1
    save_manifest(manifest)
    console.print("[green]Marked {} source(s) as compiled.[/green]".format(count))


@cli.command("reset-compiled")
def reset_compiled():
    """Reset all sources to uncompiled state (for full rebuild)."""
    manifest = load_manifest()
    for s in manifest["sources"]:
        s["compiled"] = False
    save_manifest(manifest)
    console.print("[yellow]All sources marked as uncompiled.[/yellow]")


if __name__ == "__main__":
    cli()
