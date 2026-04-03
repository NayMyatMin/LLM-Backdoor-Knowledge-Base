"""
Wiki Compilation Helpers
=========================
Utility commands for wiki compilation workflow.
The actual compilation (writing articles) is done by Claude Code.

Usage:
  python3 run.py compile status        # Show what needs compiling
  python3 run.py compile rebuild       # Reset all to uncompiled + clear wiki
  python3 run.py compile clear         # Clear all wiki articles
"""

import json
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from tools.utils import (
    RAW_DIR,
    WIKI_DIR,
    PAPERS_DIR,
    CONCEPTS_DIR,
    CONNECTIONS_DIR,
    INDEX_PATH,
    CONFIG,
    read_file,
    list_md_files,
    now_iso,
    write_file,
)

console = Console()
MANIFEST_PATH = RAW_DIR / "_manifest.json"


def load_manifest():
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text())
    return {"sources": [], "last_updated": None}


def save_manifest(manifest):
    manifest["last_updated"] = now_iso()
    write_file(MANIFEST_PATH, json.dumps(manifest, indent=2))


@click.group()
def cli():
    """Wiki compilation helpers."""
    pass


@cli.command()
def status():
    """Show compilation status — what's compiled vs pending."""
    manifest = load_manifest()
    if not manifest["sources"]:
        console.print("[yellow]No sources ingested yet.[/yellow]")
        return

    compiled = [s for s in manifest["sources"] if s.get("compiled")]
    pending = [s for s in manifest["sources"] if not s.get("compiled")]

    n_papers = len(list_md_files(PAPERS_DIR))
    n_concepts = len(list_md_files(CONCEPTS_DIR))
    n_connections = len(list_md_files(CONNECTIONS_DIR))

    table = Table(title="Compilation Status")
    table.add_column("Metric", style="bold")
    table.add_column("Count", style="cyan")

    table.add_row("Raw sources (total)", str(len(manifest["sources"])))
    table.add_row("  Compiled", "[green]{}[/green]".format(len(compiled)))
    table.add_row("  Pending", "[yellow]{}[/yellow]".format(len(pending)))
    table.add_row("Wiki articles", "")
    table.add_row("  Papers", str(n_papers))
    table.add_row("  Concepts", str(n_concepts))
    table.add_row("  Connections", str(n_connections))

    console.print(table)

    if pending:
        console.print("\n[bold]Pending sources:[/bold]")
        for s in pending:
            console.print("  - [cyan]{}[/cyan]".format(s["filename"]))
        console.print(
            "\n[dim]Ask Claude Code: 'Compile the pending sources into wiki articles'[/dim]"
        )


@cli.command()
def rebuild():
    """Reset all sources to uncompiled and clear the wiki for a full rebuild."""
    manifest = load_manifest()
    for s in manifest["sources"]:
        s["compiled"] = False
    save_manifest(manifest)

    # Clear wiki directories
    count = 0
    for d in [PAPERS_DIR, CONCEPTS_DIR, CONNECTIONS_DIR]:
        for f in d.glob("*.md"):
            f.unlink()
            count += 1

    if INDEX_PATH.exists():
        INDEX_PATH.unlink()
        count += 1

    console.print("[yellow]Wiki cleared ({} files removed). All sources marked uncompiled.[/yellow]".format(count))
    console.print("\n[dim]Ask Claude Code: 'Compile all sources into the wiki'[/dim]")


@cli.command()
def clear():
    """Clear all wiki articles (without resetting manifest)."""
    count = 0
    for d in [PAPERS_DIR, CONCEPTS_DIR, CONNECTIONS_DIR]:
        for f in d.glob("*.md"):
            f.unlink()
            count += 1

    if INDEX_PATH.exists():
        INDEX_PATH.unlink()
        count += 1

    console.print("[yellow]Cleared {} wiki files.[/yellow]".format(count))


if __name__ == "__main__":
    cli()
