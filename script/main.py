#!/usr/bin/env python3
"""Generate a blog post from a single JSON descriptor.

Expected usage:
  python3 script/main.py /Users/ttpho/Downloads/gitexpert-analysis.json
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
        "json_path",
        help="Path to JSON file containing repoTitle, repoSubtitle, sections, sources",
    )

    args = parser.parse_args()

    data_path = Path(args.json_path).expanduser()
    if not data_path.is_file():
        raise FileNotFoundError(f"JSON file not found: {data_path}")

    data = json.loads(data_path.read_text(encoding="utf-8"))

    title = data.get("repoTitle")
    if not title:
        raise ValueError("JSON must include a non-empty 'repoTitle' field.")
    subtitle = data.get("repoSubtitle", "")

    sections = data.get("sections", [])
    content_chunks = []
    for section in sections:
        sec_title = section.get("title")
        sec_content = section.get("content", "")
        if sec_title:
            content_chunks.append(f"## {sec_title}\n\n{sec_content}")
        elif sec_content:
            content_chunks.append(sec_content)

    sources = data.get("sources", [])
    if sources:
        source_lines = []
        for src in sources:
            name = src.get("title", "source")
            uri = src.get("uri")
            if uri:
                source_lines.append(f"- [{name}]({uri})")
            else:
                source_lines.append(f"- {name}")
        content_chunks.append("### Sources\n" + "\n".join(source_lines))

    content_text = "\n\n".join(content_chunks).rstrip()

    slug = slugify(title)
    today = dt.datetime.now().strftime("%Y-%m-%d")
    output_filename = f"{today}-{slug}.md"
    output_path = TEMPLATE_PATH.parent / output_filename

    post_body = build_post_content(title, subtitle, content_text)

    output_path.write_text(post_body + "\n", encoding="utf-8")

    print(f"Created: {output_path}")


if __name__ == "__main__":
    main()
