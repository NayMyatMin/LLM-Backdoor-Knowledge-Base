"""
Search Engine
==============
A lightweight TF-IDF search engine over the wiki, usable via:
  1. Web UI (Flask)
  2. CLI (for direct use or piping to Claude Code)

Usage:
  python3 run.py search serve               # Start web UI
  python3 run.py search "query"             # CLI search
  python3 run.py search "query" -j          # JSON output
"""

import json
import re
import math
from collections import Counter
from pathlib import Path

import click
from rich.console import Console
from rich.table import Table

from tools.utils import (
    WIKI_DIR,
    CONFIG,
    list_md_files,
    read_file,
    parse_frontmatter,
)

console = Console()


# ---------------------------------------------------------------------------
# Search Index (in-memory TF-IDF)
# ---------------------------------------------------------------------------


class WikiSearchEngine:
    """Simple in-memory search engine with TF-IDF ranking."""

    def __init__(self):
        self.documents = []
        self.idf = {}
        self.indexed = False

    def _tokenize(self, text):
        """Simple whitespace + punctuation tokenizer."""
        text = text.lower()
        text = re.sub(r"[^\w\s]", " ", text)
        tokens = text.split()
        return [t for t in tokens if len(t) > 2]

    def build_index(self):
        """Build the search index from all wiki .md files."""
        self.documents = []
        md_files = list_md_files(WIKI_DIR)

        for path in md_files:
            meta, content = parse_frontmatter(path)
            title = meta.get("title", path.stem.replace("-", " ").title())
            full_text = "{}\n{}".format(title, content)
            tokens = self._tokenize(full_text)

            self.documents.append({
                "path": str(path.relative_to(WIKI_DIR)),
                "title": title,
                "content": content,
                "tokens": tokens,
                "tf": Counter(tokens),
                "meta": meta,
            })

        # Compute IDF
        n_docs = len(self.documents)
        if n_docs == 0:
            self.indexed = True
            return

        all_terms = set()
        for doc in self.documents:
            all_terms.update(doc["tf"].keys())

        for term in all_terms:
            df = sum(1 for doc in self.documents if term in doc["tf"])
            self.idf[term] = math.log((n_docs + 1) / (df + 1)) + 1

        self.indexed = True

    def search(self, query, top_k=10):
        """Search the wiki and return ranked results."""
        if not self.indexed:
            self.build_index()

        query_tokens = self._tokenize(query)
        if not query_tokens:
            return []

        results = []
        for doc in self.documents:
            score = 0.0
            n_tokens = len(doc["tokens"]) or 1
            for qt in query_tokens:
                tf = doc["tf"].get(qt, 0) / n_tokens
                idf = self.idf.get(qt, 1.0)
                score += tf * idf
                if qt in doc["title"].lower():
                    score += 2.0

            if score > 0:
                snippet = self._extract_snippet(doc["content"], query_tokens)
                results.append({
                    "path": doc["path"],
                    "title": doc["title"],
                    "score": round(score, 4),
                    "snippet": snippet,
                    "meta": doc["meta"],
                })

        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]

    def _extract_snippet(self, content, query_tokens, window=150):
        """Extract a relevant snippet around the first query term match."""
        content_lower = content.lower()
        best_pos = len(content)

        for qt in query_tokens:
            pos = content_lower.find(qt)
            if pos != -1 and pos < best_pos:
                best_pos = pos

        if best_pos == len(content):
            return content[:window] + "..."

        start = max(0, best_pos - window // 2)
        end = min(len(content), best_pos + window)
        snippet = content[start:end].replace("\n", " ").strip()

        if start > 0:
            snippet = "..." + snippet
        if end < len(content):
            snippet = snippet + "..."

        return snippet


# Singleton
_engine = WikiSearchEngine()


def get_engine():
    if not _engine.indexed:
        _engine.build_index()
    return _engine


# ---------------------------------------------------------------------------
# Flask Web UI
# ---------------------------------------------------------------------------

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Wiki Search &mdash; {domain_name}</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
         background: #0d1117; color: #c9d1d9; max-width: 800px; margin: 0 auto; padding: 2rem; }}
  h1 {{ color: #58a6ff; margin-bottom: 0.5rem; }}
  .subtitle {{ color: #8b949e; margin-bottom: 1.5rem; }}
  .search-box {{ display: flex; gap: 0.5rem; margin-bottom: 2rem; }}
  input[type="text"] {{ flex: 1; padding: 0.75rem 1rem; background: #161b22; border: 1px solid #30363d;
    border-radius: 6px; color: #c9d1d9; font-size: 1rem; }}
  input[type="text"]:focus {{ outline: none; border-color: #58a6ff; }}
  button {{ padding: 0.75rem 1.5rem; background: #238636; color: white; border: none;
    border-radius: 6px; font-size: 1rem; cursor: pointer; }}
  button:hover {{ background: #2ea043; }}
  .result {{ background: #161b22; border: 1px solid #30363d; border-radius: 6px;
    padding: 1rem; margin-bottom: 1rem; }}
  .result h3 {{ color: #58a6ff; margin-bottom: 0.25rem; }}
  .result .path {{ color: #8b949e; font-size: 0.85rem; margin-bottom: 0.5rem; }}
  .result .snippet {{ color: #c9d1d9; font-size: 0.9rem; line-height: 1.5; }}
  .result .score {{ color: #8b949e; font-size: 0.8rem; float: right; }}
  .stats {{ color: #8b949e; margin-bottom: 1rem; font-size: 0.9rem; }}
  .empty {{ color: #8b949e; text-align: center; padding: 3rem; }}
</style>
</head>
<body>
  <h1>Wiki Search</h1>
  <p class="subtitle">{domain_name} Knowledge Base</p>
  <form class="search-box" method="GET" action="/search">
    <input type="text" name="q" placeholder="Search the wiki..." value="{query}" autofocus>
    <button type="submit">Search</button>
  </form>
  {results_html}
</body>
</html>"""


def results_to_html(results, query):
    if not query:
        return '<p class="empty">Enter a search query above.</p>'
    if not results:
        return '<p class="empty">No results found for "{}".</p>'.format(query)

    html = '<p class="stats">{} result(s) for "{}"</p>\n'.format(len(results), query)
    for r in results:
        html += '<div class="result">\n'
        html += '  <span class="score">{}</span>\n'.format(r["score"])
        html += '  <h3>{}</h3>\n'.format(r["title"])
        html += '  <div class="path">{}</div>\n'.format(r["path"])
        html += '  <div class="snippet">{}</div>\n'.format(r["snippet"])
        html += '</div>\n'
    return html


def create_app():
    from flask import Flask, request

    app = Flask(__name__)
    domain = CONFIG["domain"]

    @app.route("/")
    def index():
        return HTML_TEMPLATE.format(
            domain_name=domain["name"],
            query="",
            results_html='<p class="empty">Enter a search query above.</p>',
        )

    @app.route("/search")
    def search():
        q = request.args.get("q", "").strip()
        engine = get_engine()
        results = engine.search(q) if q else []
        return HTML_TEMPLATE.format(
            domain_name=domain["name"],
            query=q,
            results_html=results_to_html(results, q),
        )

    @app.route("/api/search")
    def api_search():
        """JSON API endpoint."""
        q = request.args.get("q", "").strip()
        top_k = int(request.args.get("k", 10))
        engine = get_engine()
        results = engine.search(q, top_k=top_k)
        for r in results:
            r.pop("meta", None)
        return json.dumps(results, indent=2)

    return app


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


@click.group(invoke_without_command=True)
@click.argument("query", required=False, default=None)
@click.option("--top-k", "-k", default=10, help="Number of results")
@click.option("--json-output", "-j", is_flag=True, help="Output as JSON")
@click.pass_context
def cli(ctx, query, top_k, json_output):
    """Search engine for the LLM Knowledge Base wiki.

    Run with a QUERY argument to search directly, or use subcommands (serve)."""
    if ctx.invoked_subcommand is not None:
        return
    if query is None:
        click.echo(ctx.get_help())
        return

    engine = get_engine()
    results = engine.search(query, top_k=top_k)

    if json_output:
        for r in results:
            r.pop("meta", None)
        print(json.dumps(results, indent=2))
        return

    if not results:
        console.print("[yellow]No results for '{}'[/yellow]".format(query))
        return

    table = Table(title="Search: {}".format(query))
    table.add_column("Score", style="cyan", width=8)
    table.add_column("Title", style="green")
    table.add_column("Path", style="dim")
    table.add_column("Snippet", max_width=60)

    for r in results:
        table.add_row(str(r["score"]), r["title"], r["path"], r["snippet"][:60])

    console.print(table)


@cli.command()
@click.option("--host", default=None, help="Host to bind to")
@click.option("--port", default=None, type=int, help="Port to bind to")
def serve(host, port):
    """Start the search engine web UI."""
    host = host or CONFIG["search"]["host"]
    port = port or CONFIG["search"]["port"]
    console.print("[bold green]Starting search engine at http://{}:{}[/bold green]".format(host, port))
    app = create_app()
    app.run(host=host, port=port, debug=True)


if __name__ == "__main__":
    cli()
