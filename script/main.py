#!/usr/bin/env python3
"""Generate a blog post from a single JSON descriptor or GitHub URL.

Example usage:
  export GOOGLE_API_KEY=AIZ...
  python3 script/main.py https://github.com/pydantic/monty
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path

from gemini_service import analyze_repository


ROOT_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_PATH = ROOT_DIR / "_posts" / "_template.md"


def slugify(text: str) -> str:
    """Convert text to a filesystem-friendly slug."""

    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    cleaned = re.sub(r"-+", "-", cleaned).strip("-")
    return cleaned or "post"


def build_post_content(title: str, subtitle: str, content: str, github_link: str | None) -> str:
    template = TEMPLATE_PATH.read_text(encoding="utf-8")

    if github_link:
        template = template.replace("$GITHUB_LINK", github_link)
    else:
        template = re.sub(
            r"\n+###\s+Github Page\s*\n+\$GITHUB_LINK", "", template, flags=re.IGNORECASE
        )

    return (
        template.replace("$TITLE", title)
        .replace("#SUBTITLE", subtitle)
        .replace("$CONTENT", content.rstrip())
    )


def load_analysis_data(source: str, api_key: str | None):
    """Load analysis data from a JSON file or generate it via Gemini from a repo URL."""

    potential_path = Path(source).expanduser()
    if potential_path.is_file():
        return json.loads(potential_path.read_text(encoding="utf-8"))

    if source.startswith("http://") or source.startswith("https://"):
        return analyze_repository(source, api_key=api_key)

    raise FileNotFoundError(
        "Input must be an existing JSON file or a GitHub repository URL (http/https)."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a blog post from template")
    parser.add_argument(
        "input",
        help="Path to JSON file or GitHub repository URL",
    )
    parser.add_argument(
        "--api-key",
        dest="api_key",
        default=None,
        help="Gemini API key (fallback to env API_KEY or GOOGLE_API_KEY)",
    )

    args = parser.parse_args()

    data = load_analysis_data(args.input, api_key=args.api_key)

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
    one_day_ago = dt.datetime.now() - dt.timedelta(days=1)
    day = one_day_ago.strftime("%Y-%m-%d")
    output_filename = f"{day}-{slug}.md"
    output_path = TEMPLATE_PATH.parent / output_filename

    github_link = args.input if args.input.startswith("http") else None

    post_body = build_post_content(title, subtitle, content_text, github_link)

    output_path.write_text(post_body + "\n", encoding="utf-8")

    print(f"Created: {output_path}")


if __name__ == "__main__":
    main()
