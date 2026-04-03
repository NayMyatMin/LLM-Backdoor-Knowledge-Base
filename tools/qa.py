"""
Q&A Helpers
============
Utility to prepare wiki context for Q&A.
The actual Q&A is done conversationally with Claude Code.

Usage:
  python3 run.py qa context            # Print wiki summary for quick reference
  python3 run.py qa context --full     # Print full wiki text
"""

import click
from rich.console import Console
from rich.markdown import Markdown

from tools.utils import (
    CONFIG,
    WIKI_DIR,
    OUTPUT_DIR,
    get_wiki_full_text,
    get_wiki_summary,
    write_file,
    slugify,
    now_iso,
    list_md_files,
)

console = Console()


@click.group()
def cli():
    """Q&A helpers for the LLM Knowledge Base."""
    pass


@cli.command()
@click.option("--full", is_flag=True, help="Show full wiki text instead of summary")
def context(full):
    """Display wiki context (useful for quick reference)."""
    if full:
        text = get_wiki_full_text()
    else:
        text = get_wiki_summary()

    if text == "(wiki is empty)":
        console.print("[yellow]Wiki is empty. Add sources and compile first.[/yellow]")
        return

    console.print(Markdown(text))


@cli.command()
@click.argument("question")
@click.argument("answer_file", type=click.Path())
def save_report(question, answer_file):
    """Save a Q&A answer file as a report in output/reports/."""
    from pathlib import Path
    content = Path(answer_file).read_text(encoding="utf-8")
    filename = "qa-{}.md".format(slugify(question[:50]))
    out_path = OUTPUT_DIR / "reports" / filename

    report = "# Q&A Report: {}\n\n".format(question)
    report += "_Generated: {}_\n".format(now_iso())
    report += "_Domain: {}_\n\n---\n\n".format(CONFIG["domain"]["name"])
    report += content

    write_file(out_path, report)
    console.print("[green]Report saved to:[/green] {}".format(out_path))


@cli.command()
def topics():
    """List all wiki article titles for quick reference."""
    files = list_md_files(WIKI_DIR)
    if not files:
        console.print("[yellow]Wiki is empty.[/yellow]")
        return

    from tools.utils import parse_frontmatter, PAPERS_DIR, CONCEPTS_DIR, CONNECTIONS_DIR

    sections = [
        ("Papers", PAPERS_DIR),
        ("Concepts", CONCEPTS_DIR),
        ("Connections", CONNECTIONS_DIR),
    ]

    for section_name, section_dir in sections:
        section_files = list_md_files(section_dir)
        if section_files:
            console.print("\n[bold cyan]{}[/bold cyan]".format(section_name))
            for f in section_files:
                meta, _ = parse_frontmatter(f)
                title = meta.get("title", f.stem)
                console.print("  - {} [dim]({})[/dim]".format(title, f.name))


@cli.command("file-to-wiki")
@click.argument("source", type=click.Path(exists=True))
@click.option("--section", "-s", type=click.Choice(["papers", "concepts", "connections"]),
              default="connections", help="Wiki section to file into")
def file_to_wiki(source, section):
    """File an output (report, exploration) back into the wiki.

    Copies a markdown file from output/ into the appropriate wiki/ section,
    so your explorations 'add up' in the knowledge base.
    """
    import shutil
    from pathlib import Path
    from tools.utils import PAPERS_DIR, CONCEPTS_DIR, CONNECTIONS_DIR

    section_dirs = {
        "papers": PAPERS_DIR,
        "concepts": CONCEPTS_DIR,
        "connections": CONNECTIONS_DIR,
    }

    source_path = Path(source)
    dest_dir = section_dirs[section]
    dest = dest_dir / source_path.name

    if dest.exists():
        console.print("[yellow]File already exists in wiki/{}/: {}[/yellow]".format(
            section, source_path.name
        ))
        return

    shutil.copy2(source_path, dest)
    console.print("[green]Filed into wiki/{}/: {}[/green]".format(section, source_path.name))
    console.print("[dim]The wiki search index will pick this up automatically.[/dim]")


if __name__ == "__main__":
    cli()
