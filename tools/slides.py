"""
Slide Deck Helpers
===================
Utilities for Marp slide deck management.
The actual slide generation is done by Claude Code.

Usage:
  python3 run.py slides list           # List generated slide decks
  python3 run.py slides convert FILE   # Convert Marp slides to HTML
"""

from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from tools.utils import (
    OUTPUT_DIR,
    list_md_files,
    read_file,
)

console = Console()
SLIDES_DIR = OUTPUT_DIR / "slides"


@click.group()
def cli():
    """Marp slide deck helpers."""
    pass


@cli.command("list")
def list_slides():
    """List all generated slide decks."""
    slides = list_md_files(SLIDES_DIR)
    if not slides:
        console.print("[yellow]No slide decks yet.[/yellow]")
        console.print("[dim]Ask Claude Code: 'Generate a slide deck on <topic>'[/dim]")
        return

    table = Table(title="Slide Decks")
    table.add_column("File", style="cyan")
    table.add_column("Slides", style="green")
    table.add_column("Size", style="dim")

    for s in slides:
        content = read_file(s)
        n_slides = content.count("\n---\n") + 1
        size = "{:.1f}KB".format(s.stat().st_size / 1024)
        table.add_row(s.name, str(n_slides), size)

    console.print(table)
    console.print("\n[dim]View in Obsidian with the Marp plugin, or convert:")
    console.print("  npx @marp-team/marp-cli output/slides/<file>.md --html[/dim]")


if __name__ == "__main__":
    cli()
