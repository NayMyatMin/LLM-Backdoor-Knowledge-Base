"""
Image Downloader
=================
Downloads remote images referenced in raw/ markdown files to local storage,
rewrites the markdown to use local paths so Obsidian can display them.

Usage:
  python3 run.py images download              # Download all remote images
  python3 run.py images download raw/file.md  # Download images from one file
  python3 run.py images list                  # List all local images
"""

import re
import hashlib
from pathlib import Path
from urllib.parse import urlparse, unquote

import click
from rich.console import Console
from rich.table import Table

from tools.utils import (
    RAW_DIR,
    CONFIG,
    read_file,
    write_file,
    list_raw_files,
)

console = Console()
IMAGES_DIR = RAW_DIR / "images"


def find_remote_images(content):
    """Find all remote image URLs in markdown content."""
    patterns = [
        r"!\[([^\]]*)\]\((https?://[^)]+)\)",        # ![alt](url)
        r"<img[^>]+src=[\"'](https?://[^\"']+)[\"']", # <img src="url">
    ]
    images = []
    for pattern in patterns:
        for match in re.finditer(pattern, content):
            if len(match.groups()) == 2:
                images.append({"alt": match.group(1), "url": match.group(2), "full_match": match.group(0)})
            else:
                images.append({"alt": "", "url": match.group(1), "full_match": match.group(0)})
    return images


def url_to_filename(url):
    """Convert a URL to a safe local filename."""
    parsed = urlparse(url)
    path = unquote(parsed.path)
    name = Path(path).name

    if not name or len(name) > 100:
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        ext = Path(path).suffix or ".png"
        name = "img-{}{}".format(url_hash, ext)

    # Ensure it has an image extension
    known_exts = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico"}
    if Path(name).suffix.lower() not in known_exts:
        name = name + ".png"

    return name


def download_image(url, dest_path):
    """Download an image from a URL to a local path."""
    import urllib.request
    import ssl

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    try:
        ctx = ssl.create_default_context()
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, context=ctx, timeout=15) as response:
            data = response.read()
            dest_path.write_bytes(data)
            return True
    except Exception as e:
        console.print("  [red]Failed: {} — {}[/red]".format(url[:60], e))
        return False


def localize_images_in_file(file_path):
    """Download remote images and rewrite markdown to use local paths."""
    content = read_file(Path(file_path))
    if not content:
        return 0

    images = find_remote_images(content)
    if not images:
        return 0

    downloaded = 0
    new_content = content

    for img in images:
        local_name = url_to_filename(img["url"])
        local_path = IMAGES_DIR / local_name
        rel_path = "images/{}".format(local_name)

        if local_path.exists():
            console.print("  [dim]Already local: {}[/dim]".format(local_name))
        else:
            console.print("  Downloading: {}".format(img["url"][:80]))
            if not download_image(img["url"], local_path):
                continue

        # Rewrite the markdown reference
        if img["full_match"].startswith("!"):
            old = img["full_match"]
            new = "![{}]({})".format(img["alt"], rel_path)
            new_content = new_content.replace(old, new, 1)
        elif img["full_match"].startswith("<img"):
            new_content = new_content.replace(img["url"], rel_path, 1)

        downloaded += 1

    if downloaded > 0:
        write_file(Path(file_path), new_content)

    return downloaded


@click.group()
def cli():
    """Image management for the knowledge base."""
    pass


@cli.command()
@click.argument("file_path", required=False, default=None, type=click.Path())
def download(file_path):
    """Download remote images to local and rewrite markdown references.

    If FILE_PATH is given, process only that file.
    Otherwise, process all markdown files in raw/.
    """
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    if file_path:
        files = [Path(file_path)]
    else:
        files = [f for f in list_raw_files() if f.suffix in (".md", ".html", ".txt")]

    if not files:
        console.print("[yellow]No files to process.[/yellow]")
        return

    total = 0
    for f in files:
        console.print("\n[bold]Processing:[/bold] {}".format(f.name))
        count = localize_images_in_file(f)
        total += count

    console.print("\n[bold green]Done.[/bold green] Downloaded {} image(s) to raw/images/".format(total))


@cli.command("list")
def list_images():
    """List all local images."""
    if not IMAGES_DIR.exists():
        console.print("[yellow]No images directory yet.[/yellow]")
        return

    images = sorted(IMAGES_DIR.iterdir())
    images = [f for f in images if f.is_file() and not f.name.startswith(".")]

    if not images:
        console.print("[yellow]No images downloaded yet.[/yellow]")
        return

    table = Table(title="Local Images")
    table.add_column("File", style="cyan")
    table.add_column("Size", style="dim")

    total_size = 0
    for img in images:
        size = img.stat().st_size
        total_size += size
        if size > 1024 * 1024:
            size_str = "{:.1f}MB".format(size / (1024 * 1024))
        else:
            size_str = "{:.1f}KB".format(size / 1024)
        table.add_row(img.name, size_str)

    console.print(table)
    console.print("\nTotal: {} images, {:.1f}MB".format(
        len(images), total_size / (1024 * 1024)
    ))


if __name__ == "__main__":
    cli()
