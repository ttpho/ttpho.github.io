#!/usr/bin/env python3
"""Generate a blog post from the template and a content file.

Expected usage:
  python main.py --title "title" --subtitle "subtitle" --url "url" --content "path/to/file.md"

  python script/main.py --title "kreuzberg" \
  --subtitle "A polyglot document intelligence framework with a Rust core. Extract text, metadata, and structured information from PDFs, Office documents, images, and 60+ formats. Available for Rust, Python, Ruby, Java, Go, PHP, Elixir, C#, TypeScript (Node/Bun/Wasm/Deno)- or use via CLI, REST API, or MCP server." \
  --url "https://github.com/kreuzberg-dev/kreuzberg" \
  --content "/Users/ttpho/Downloads/gitexpert-analysis.md"
"""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path
from urllib.parse import urlparse


ROOT_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT_DIR / "_posts" / "_template.md"


def slugify(text: str) -> str:
    """Convert text to a filesystem-friendly slug."""

    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    cleaned = re.sub(r"-+", "-", cleaned).strip("-")
    return cleaned or "post"


def slug_from_url(url: str) -> str:
    parsed = urlparse(url)
    segments = [segment for segment in parsed.path.split("/") if segment]
    candidate = segments[-1] if segments else (parsed.hostname or "post")
    return slugify(candidate)


def build_post_content(title: str, subtitle: str, url: str, content: str) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    return (
        template.replace("$TITLE", title)
        .replace("#SUBTITLE", subtitle)
        .replace("$CONTENT", content.rstrip())
        .replace("$GITHUB_LINK", url)
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a blog post from template")
    parser.add_argument("-t", "--title", required=True, help="Post title")
    parser.add_argument(
        "-s", "--subtitle", default="", help="Post subtitle (can be empty)"
    )
    parser.add_argument("-u", "--url", required=True, help="GitHub page URL")
    parser.add_argument(
        "-c", "--content", required=True, help="Path to the content file"
    )

    args = parser.parse_args()

    content_path = Path(args.content).expanduser()
    if not content_path.is_file():
        raise FileNotFoundError(f"Content file not found: {content_path}")

    content_text = content_path.read_text(encoding="utf-8")

    slug = slug_from_url(args.url)
    today = dt.datetime.now().strftime("%Y-%m-%d")
    output_filename = f"{today}-{slug}.md"
    output_path = TEMPLATE_PATH.parent / output_filename

    post_body = build_post_content(
        args.title, args.subtitle, args.url, content_text)

    output_path.write_text(post_body + "\n", encoding="utf-8")

    print(f"Created: {output_path}")


if __name__ == "__main__":
    main()
