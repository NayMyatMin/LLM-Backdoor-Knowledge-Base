"""
Wiki Linter — Structural Checks
=================================
Runs non-LLM structural checks over the wiki to find issues.
For deeper LLM-powered analysis, ask Claude Code directly.

Usage:
  python3 run.py lint check         # Run structural health checks
  python3 run.py lint stats         # Wiki statistics
"""

import re
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from tools.utils import (
    CONFIG,
    WIKI_DIR,
    PAPERS_DIR,
    CONCEPTS_DIR,
    CONNECTIONS_DIR,
    list_md_files,
    read_file,
    parse_frontmatter,
)

console = Console()


def find_wiki_links(content):
    """Extract all [[wiki-link]] references from content."""
    return re.findall(r"\[\[([^\]]+)\]\]", content)


def get_all_slugs():
    """Get all existing article slugs in the wiki."""
    slugs = set()
    for md_file in list_md_files(WIKI_DIR):
        slugs.add(md_file.stem)
    return slugs


def run_structural_checks():
    """Run structural health checks that don't require an LLM."""
    issues = []
    all_files = list_md_files(WIKI_DIR)

    if not all_files:
        return [{"severity": "info", "category": "empty", "file": None,
                 "description": "Wiki is empty. Add raw sources and ask Claude Code to compile them."}]

    all_slugs = get_all_slugs()

    for md_file in all_files:
        rel = str(md_file.relative_to(WIKI_DIR))
        meta, content = parse_frontmatter(md_file)

        # Check for broken wiki links
        links = find_wiki_links(content)
        for link in links:
            target = link.split("|")[0]
            link_slug = target.lower().replace(" ", "-")
            if link_slug not in all_slugs and target not in all_slugs:
                issues.append({
                    "severity": "warning",
                    "category": "broken_link",
                    "file": rel,
                    "description": "Broken wiki link: [[{}]]".format(link),
                })

        # Check for very short articles
        word_count = len(content.split())
        if word_count < 50:
            issues.append({
                "severity": "warning",
                "category": "short_article",
                "file": rel,
                "description": "Very short article ({} words)".format(word_count),
            })

        # Check for missing title in frontmatter
        if not meta.get("title"):
            issues.append({
                "severity": "warning",
                "category": "missing_metadata",
                "file": rel,
                "description": "Missing 'title' in frontmatter",
            })

        # Check for articles with no wiki links (isolated nodes)
        if not links and word_count > 100:
            issues.append({
                "severity": "info",
                "category": "isolated",
                "file": rel,
                "description": "Article has no [[wiki links]] to other articles",
            })

    return issues


@click.group()
def cli():
    """Wiki linter and health check tool."""
    pass


@cli.command()
def check():
    """Run structural health checks on the wiki."""
    console.print("[bold]Running wiki structural checks...[/bold]\n")
    issues = run_structural_checks()

    if not issues:
        console.print("[bold green]No structural issues found![/bold green]")
        console.print("\n[dim]For deeper analysis (inconsistencies, missing data, suggestions),"
                      " ask Claude Code: 'Read my wiki and run a health check'[/dim]")
        return

    table = Table(title="Wiki Health Check - {} issue(s)".format(len(issues)))
    table.add_column("Severity", style="bold")
    table.add_column("Category", style="cyan")
    table.add_column("File", style="dim")
    table.add_column("Description", max_width=60)

    severity_colors = {"error": "red", "warning": "yellow", "info": "blue"}

    for issue in issues:
        sev = issue.get("severity", "info")
        color = severity_colors.get(sev, "white")
        table.add_row(
            "[{}]{}[/{}]".format(color, sev.upper(), color),
            issue.get("category", "-"),
            issue.get("file") or "-",
            issue.get("description", ""),
        )

    console.print(table)
    console.print("\n[dim]For LLM-powered fixes, ask Claude Code: 'Fix the wiki lint issues'[/dim]")


@cli.command()
def stats():
    """Show detailed wiki statistics."""
    all_files = list_md_files(WIKI_DIR)
    n_papers = len(list_md_files(PAPERS_DIR))
    n_concepts = len(list_md_files(CONCEPTS_DIR))
    n_connections = len(list_md_files(CONNECTIONS_DIR))

    total_words = 0
    total_links = 0
    all_link_targets = []

    for md_file in all_files:
        content = read_file(md_file)
        total_words += len(content.split())
        links = find_wiki_links(content)
        total_links += len(links)
        all_link_targets.extend(links)

    console.print(Panel(
        "[bold cyan]{}[/bold cyan]".format(CONFIG["domain"]["name"]),
        title="Wiki Statistics",
        style="cyan",
    ))

    table = Table(show_header=False, box=None, padding=(0, 2))
    table.add_column("Metric", style="bold")
    table.add_column("Value", style="cyan")

    table.add_row("Total articles", str(len(all_files)))
    table.add_row("  Papers", str(n_papers))
    table.add_row("  Concepts", str(n_concepts))
    table.add_row("  Connections", str(n_connections))
    table.add_row("Total words", "~{:,}".format(total_words))
    table.add_row("Total wiki links", str(total_links))
    table.add_row("Unique link targets", str(len(set(all_link_targets))))

    console.print(table)


if __name__ == "__main__":
    cli()
