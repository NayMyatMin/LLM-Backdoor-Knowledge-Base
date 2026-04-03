"""
Shared utilities for the LLM Knowledge Base.
Handles config loading and file operations.
"""

import os
import sys
import re
import yaml
import hashlib
import frontmatter
from pathlib import Path
from datetime import datetime

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

ROOT_DIR = Path(__file__).resolve().parent.parent


def load_config() -> dict:
    """Load config.yaml from the project root."""
    config_path = ROOT_DIR / "config.yaml"
    if not config_path.exists():
        print(f"[ERROR] config.yaml not found at {config_path}")
        sys.exit(1)
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


CONFIG = load_config()

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------


def get_path(key):
    """Resolve a path from the config relative to ROOT_DIR."""
    return ROOT_DIR / CONFIG["paths"].get(key, key)


RAW_DIR = get_path("raw")
WIKI_DIR = get_path("wiki")
OUTPUT_DIR = get_path("output")
TEMPLATES_DIR = get_path("templates")

PAPERS_DIR = ROOT_DIR / CONFIG["wiki_structure"]["papers_dir"]
CONCEPTS_DIR = ROOT_DIR / CONFIG["wiki_structure"]["concepts_dir"]
CONNECTIONS_DIR = ROOT_DIR / CONFIG["wiki_structure"]["connections_dir"]
INDEX_PATH = ROOT_DIR / CONFIG["wiki_structure"]["index"]


# ---------------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------------


def read_file(path):
    """Read a text file, return empty string on failure."""
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return ""


def write_file(path, content):
    """Write content to a file, creating parent dirs as needed."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def slugify(text):
    """Convert text to a filename-safe slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def file_hash(path):
    """Return MD5 hash of file contents for change detection."""
    return hashlib.md5(path.read_bytes()).hexdigest()


def list_md_files(directory):
    """Recursively list all .md files under a directory."""
    directory = Path(directory)
    if not directory.exists():
        return []
    return sorted(directory.rglob("*.md"))


def list_raw_files():
    """List all supported files in the raw/ directory (excludes _-prefixed files)."""
    exts = CONFIG["ingest"]["supported_extensions"]
    files = []
    for ext in exts:
        for f in RAW_DIR.rglob("*{}".format(ext)):
            if not f.name.startswith("_"):
                files.append(f)
    return sorted(files)


def parse_frontmatter(path):
    """Parse YAML frontmatter from a markdown file. Returns (metadata, content)."""
    post = frontmatter.load(str(path))
    return dict(post.metadata), post.content


def write_with_frontmatter(path, metadata, content):
    """Write a markdown file with YAML frontmatter."""
    post = frontmatter.Post(content, **metadata)
    write_file(path, frontmatter.dumps(post))


def now_iso():
    """Return current datetime as ISO string."""
    return datetime.now().isoformat(timespec="seconds")


def get_venues_list():
    """Return flat list of all configured venue names."""
    venues = []
    for category in CONFIG["domain"]["venues"].values():
        for v in category:
            if isinstance(v, dict):
                venues.append(v["name"])
            else:
                venues.append(v)
    return venues


def get_wiki_summary():
    """Build a brief summary of all wiki articles."""
    lines = []
    for md_file in list_md_files(WIKI_DIR):
        rel = md_file.relative_to(WIKI_DIR)
        meta, content = parse_frontmatter(md_file)
        title = meta.get("title", md_file.stem)
        summary = meta.get("summary", content[:200].replace("\n", " "))
        lines.append("- **{}** (`{}`): {}".format(title, rel, summary))
    return "\n".join(lines) if lines else "(wiki is empty)"


def get_wiki_full_text(max_chars=400000):
    """Concatenate all wiki articles into one string."""
    parts = []
    total = 0
    for md_file in list_md_files(WIKI_DIR):
        rel = md_file.relative_to(WIKI_DIR)
        text = read_file(md_file)
        header = "\n\n{}\nFILE: {}\n{}\n".format("=" * 60, rel, "=" * 60)
        chunk = header + text
        if total + len(chunk) > max_chars:
            break
        parts.append(chunk)
        total += len(chunk)
    return "".join(parts) if parts else "(wiki is empty)"
