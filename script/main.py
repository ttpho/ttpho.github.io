#!/usr/bin/env python3
"""Generate a blog post from the template and a content file.

Expected usage:
  python main.py --info "path/to/info.json" --content "path/to/file.md"

  python script/main.py --info "/Users/ttpho/Downloads/page_info.json" --content "/Users/ttpho/Downloads/gitexpert-analysis.md"

"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT_DIR / "_posts" / "_template.md"


def slugify(text: str) -> str:
    """Convert text to a filesystem-friendly slug."""

    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    cleaned = re.sub(r"-+", "-", cleaned).strip("-")
    return cleaned or "post"


def build_post_content(title: str, subtitle: str, content: str) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    # Drop the Github section since URL is no longer provided
    template = re.sub(
        r"\n+###\s+Github Page\s*\n+\$GITHUB_LINK", "", template, flags=re.IGNORECASE
    )
    return (
        template.replace("$TITLE", title)
        .replace("#SUBTITLE", subtitle)
        .replace("$CONTENT", content.rstrip())
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a blog post from template")
    parser.add_argument(
        "-i", "--info", required=True, help="Path to JSON file containing title/subtitle"
    )
    parser.add_argument(
        "-c", "--content", required=True, help="Path to the content file (Markdown)"
    )

    args = parser.parse_args()

    info_path = Path(args.info).expanduser()
    if not info_path.is_file():
        raise FileNotFoundError(f"Info file not found: {info_path}")

    content_path = Path(args.content).expanduser()
    if not content_path.is_file():
        raise FileNotFoundError(f"Content file not found: {content_path}")

    info_data = json.loads(info_path.read_text(encoding="utf-8"))
    title = info_data.get("title")
    if not title:
        raise ValueError("Info JSON must include a non-empty 'title' field.")
    subtitle = info_data.get("subtitle", "")

    content_text = content_path.read_text(encoding="utf-8")

    slug = slugify(title)
    today = dt.datetime.now().strftime("%Y-%m-%d")
    output_filename = f"{today}-{slug}.md"
    output_path = TEMPLATE_PATH.parent / output_filename

    post_body = build_post_content(title, subtitle, content_text)

    output_path.write_text(post_body + "\n", encoding="utf-8")

    print(f"Created: {output_path}")


if __name__ == "__main__":
    main()
