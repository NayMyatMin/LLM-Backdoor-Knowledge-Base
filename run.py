#!/usr/bin/env python3
"""
LLM Knowledge Base — Main CLI
===============================
File management and utility commands for the knowledge base.
All LLM-powered tasks (compilation, Q&A, linting, slides) are done
by Claude Code directly in conversation.

Usage:
  python3 run.py status                    # Show knowledge base status
  python3 run.py init                      # Set your research domain
  python3 run.py quickstart                # Getting started guide

  python3 run.py ingest add <file>         # Add a source document
  python3 run.py ingest scan               # Scan raw/ for new files
  python3 run.py ingest list               # List all sources
  python3 run.py ingest uncompiled         # Show what needs compiling

  python3 run.py compile status            # Compilation status
  python3 run.py compile rebuild           # Reset for full rebuild

  python3 run.py search "query"            # CLI search
  python3 run.py search serve              # Start search web UI

  python3 run.py qa topics                 # List all wiki articles
  python3 run.py qa context                # Print wiki summary

  python3 run.py lint check                # Structural health checks
  python3 run.py lint stats                # Wiki statistics

  python3 run.py slides list               # List slide decks
"""

import sys
import os

# Ensure project root is on the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from tools.utils import (
    CONFIG,
    RAW_DIR,
    WIKI_DIR,
    PAPERS_DIR,
    CONCEPTS_DIR,
    CONNECTIONS_DIR,
    OUTPUT_DIR,
    list_raw_files,
    list_md_files,
)

console = Console()


@click.group()
def cli():
    """
    LLM Knowledge Base CLI

    A personal research knowledge base powered by Claude Code,
    following Andrej Karpathy's LLM Knowledge Base approach.

    File management is done via this CLI.
    All LLM tasks (compile, Q&A, lint, slides) are done by
    asking Claude Code directly.
    """
    pass


# ---------------------------------------------------------------------------
# Register sub-command groups
# ---------------------------------------------------------------------------

from tools.ingest import cli as ingest_cli
from tools.compile_wiki import cli as compile_cli
from tools.qa import cli as qa_cli
from tools.search_engine import cli as search_cli
from tools.lint import cli as lint_cli
from tools.slides import cli as slides_cli
from tools.images import cli as images_cli

cli.add_command(ingest_cli, "ingest")
cli.add_command(compile_cli, "compile")
cli.add_command(qa_cli, "qa")
cli.add_command(search_cli, "search")
cli.add_command(lint_cli, "lint")
cli.add_command(slides_cli, "slides")
cli.add_command(images_cli, "images")


# ---------------------------------------------------------------------------
# Status command
# ---------------------------------------------------------------------------

@cli.command()
def status():
    """Show the current status of the knowledge base."""
    domain = CONFIG["domain"]

    n_raw = len(list_raw_files())
    n_papers = len(list_md_files(PAPERS_DIR))
    n_concepts = len(list_md_files(CONCEPTS_DIR))
    n_connections = len(list_md_files(CONNECTIONS_DIR))
    n_slides = len(list_md_files(OUTPUT_DIR / "slides"))
    n_reports = len(list_md_files(OUTPUT_DIR / "reports"))

    # Calculate total wiki word count
    total_words = 0
    for f in list_md_files(WIKI_DIR):
        total_words += len(f.read_text(encoding="utf-8").split())

    console.print(Panel(
        "[bold cyan]{}[/bold cyan]\n[dim]{}[/dim]".format(
            domain["name"], domain["description"]
        ),
        title="LLM Knowledge Base",
        style="cyan",
    ))

    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Metric", style="bold")
    table.add_column("Value", style="cyan")

    table.add_row("Raw sources", str(n_raw))
    table.add_row("Paper articles", str(n_papers))
    table.add_row("Concept articles", str(n_concepts))
    table.add_row("Connection articles", str(n_connections))
    table.add_row("Total wiki words", "~{:,}".format(total_words))
    table.add_row("Slide decks", str(n_slides))
    table.add_row("Q&A reports", str(n_reports))
    table.add_row("", "")
    table.add_row("Raw directory", str(RAW_DIR))
    table.add_row("Wiki directory", str(WIKI_DIR))
    table.add_row("Output directory", str(OUTPUT_DIR))

    console.print(table)

    if n_raw == 0:
        console.print(
            "\n[yellow]No sources yet![/yellow] Get started:\n"
            "  1. Drop .md/.txt/.pdf files into raw/\n"
            "  2. Run: python3 run.py ingest scan\n"
            "  3. Ask Claude Code: 'Compile the wiki'\n"
        )


# ---------------------------------------------------------------------------
# Init command
# ---------------------------------------------------------------------------

@cli.command()
@click.option("--name", prompt="Research domain name", help="Name of your research domain")
@click.option("--description", prompt="Brief description", help="One-line description of the domain")
def init(name, description):
    """Initialize the knowledge base with your research domain."""
    import yaml
    from tools.utils import ROOT_DIR

    CONFIG["domain"]["name"] = name
    CONFIG["domain"]["description"] = description

    config_path = ROOT_DIR / "config.yaml"
    with open(config_path, "w") as f:
        yaml.dump(CONFIG, f, default_flow_style=False, sort_keys=False)

    console.print("\n[bold green]Knowledge base initialized![/bold green]")
    console.print("  Domain: [cyan]{}[/cyan]".format(name))
    console.print("  Description: {}".format(description))
    console.print("\nNext steps:")
    console.print("  1. Drop source files into raw/")
    console.print("  2. Run: python3 run.py ingest scan")
    console.print("  3. Ask Claude Code: 'Compile the wiki from my raw sources'")


# ---------------------------------------------------------------------------
# Quick-start command
# ---------------------------------------------------------------------------

@cli.command()
def quickstart():
    """Interactive quickstart guide."""
    console.print(Panel(
        "[bold]Welcome to your LLM Knowledge Base![/bold]\n\n"
        "This system follows Andrej Karpathy's approach:\n"
        "raw data -> Claude Code compilation -> .md wiki -> Q&A / search / slides\n\n"
        "[bold cyan]Step 1:[/bold cyan] Set your research domain\n"
        "  [dim]python3 run.py init[/dim]\n\n"
        "[bold cyan]Step 2:[/bold cyan] Add source documents\n"
        "  Drop .md files into the raw/ folder, or use:\n"
        "  [dim]python3 run.py ingest add path/to/paper.md --venue NeurIPS --year 2024[/dim]\n"
        "  [dim]python3 run.py ingest scan[/dim]  (to detect new files in raw/)\n\n"
        "[bold cyan]Step 3:[/bold cyan] Compile the wiki (ask Claude Code)\n"
        "  Tell Claude Code: 'Compile my raw sources into wiki articles'\n"
        "  Claude Code reads your raw files and writes structured wiki articles.\n\n"
        "[bold cyan]Step 4:[/bold cyan] Ask questions (ask Claude Code)\n"
        "  Tell Claude Code: 'What are the main findings about X?'\n"
        "  Claude Code reads your wiki and answers with citations.\n\n"
        "[bold cyan]Step 5:[/bold cyan] Search the wiki\n"
        "  [dim]python3 run.py search \"query\"[/dim]\n"
        "  [dim]python3 run.py search serve[/dim]  -> open http://localhost:8877\n\n"
        "[bold cyan]Step 6:[/bold cyan] Generate outputs (ask Claude Code)\n"
        "  'Generate a Marp slide deck on <topic>'\n"
        "  'Write a summary report comparing X and Y'\n\n"
        "[bold cyan]Step 7:[/bold cyan] Maintain quality\n"
        "  [dim]python3 run.py lint check[/dim]  (structural checks)\n"
        "  Tell Claude Code: 'Run a health check on my wiki'\n\n"
        "[bold cyan]Tip:[/bold cyan] Open the wiki/ folder in Obsidian for the best viewing experience!",
        title="Quickstart Guide",
        style="green",
    ))


if __name__ == "__main__":
    cli()
