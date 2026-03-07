#!/usr/bin/env python3
"""Generate a daily tech news post via Google Search + Gemini."""

from __future__ import annotations

import argparse
import datetime as dt
import os
import re
from dataclasses import dataclass
from pathlib import Path
from zoneinfo import ZoneInfo


POSTS_DIR = Path(__file__).resolve().parent.parent / "_posts"
LOCAL_TZ = ZoneInfo("Asia/Ho_Chi_Minh")

PRIORITY_SOURCES = [
    "Google Developers Blog",
    "Google Cloud Blog",
    "Google Search Central Blog",
    "Google Research Blog",
    "OpenAI News",
    "Anthropic News",
    "Meta AI Blog",
    "Meta Engineering Blog",
    "Cursor Blog",
    "Alibaba Cloud Community",
    "AWS News Blog",
    "AWS Architecture Blog",
    "Microsoft Research Blog",
    "Azure Blog",
    "NVIDIA Blog",
    "Apple Machine Learning Research",
]


@dataclass
class Source:
    title: str
    uri: str


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    cleaned = re.sub(r"-+", "-", cleaned).strip("-")
    return cleaned or "daily-tech-news"


def _resolve_api_key(explicit: str | None) -> str:
    key = explicit or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY") or os.getenv("API_KEY")
    if not key:
        raise RuntimeError(
            "Missing Gemini API key. Set GEMINI_API_KEY/GOOGLE_API_KEY/API_KEY or pass --api-key."
        )
    return key


def _extract_sources(response) -> list[Source]:
    sources: list[Source] = []
    seen: set[str] = set()

    try:
        candidates = response.candidates or []
    except Exception:
        candidates = []

    for candidate in candidates:
        grounding = getattr(candidate, "grounding_metadata", None) or getattr(
            candidate, "groundingMetadata", None
        )
        if not grounding:
            continue
        chunks = getattr(grounding, "grounding_chunks", None) or getattr(
            grounding, "groundingChunks", None
        )
        if not chunks:
            continue

        for chunk in chunks:
            web = getattr(chunk, "web", None)
            if not web:
                continue
            uri = (getattr(web, "uri", "") or "").strip()
            title = (getattr(web, "title", "") or "Source").strip()
            if not uri or uri in seen:
                continue
            seen.add(uri)
            sources.append(Source(title=title, uri=uri))

    return sources


def generate_news_markdown(target_date: dt.date, api_key: str) -> tuple[str, list[Source], str]:
    try:
        from google import genai
        from google.genai import types
    except ImportError as exc:
        raise RuntimeError("google-genai is not installed. Run: pip install -r script/requirements.txt") from exc

    client = genai.Client(api_key=api_key)
    date_iso = target_date.isoformat()
    date_display = target_date.strftime("%d/%m/%Y")
    sources_hint = "\n".join(f"- {item}" for item in PRIORITY_SOURCES)

    prompt = f"""
Bạn là biên tập viên tin công nghệ.
Hãy dùng Google Search (grounding) để tổng hợp tin công nghệ trong ngày {date_display} (múi giờ Asia/Ho_Chi_Minh).

Ưu tiên lấy tin từ các nguồn sau:
{sources_hint}

Yêu cầu đầu ra:
1) Viết bằng tiếng Việt, chuẩn markdown.
2) Chỉ gồm đúng 3 section:
   - ## Tổng quan
   - ## Tin công nghệ Việt Nam
   - ## Tin công nghệ thế giới
3) Mỗi section dùng bullet ngắn gọn, tập trung thông tin quan trọng.
4) Không thêm section "Sources", không thêm phần mở đầu/kết luận ngoài 3 section trên.
5) Không dùng thông tin ngoài ngày mục tiêu nếu không bắt buộc; nếu có thì ghi rõ là bối cảnh.

Ngày mục tiêu (ISO): {date_iso}
"""

    model_candidates = [
        "gemini-3.1-flash-lite",
        "gemini-2.5-flash-lite",
        "gemini-2.5-flash",
    ]
    last_error: Exception | None = None

    for model_name in model_candidates:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    tools=[types.Tool(google_search=types.GoogleSearch())],
                    temperature=0.3,
                ),
            )
            markdown = (response.text or "").strip()
            if markdown:
                return markdown, _extract_sources(response), model_name
        except Exception as exc:
            last_error = exc
            continue

    raise RuntimeError(f"Failed to generate content with all Gemini models. Last error: {last_error}")


def build_post(body_markdown: str, target_date: dt.date, sources: list[Source], model_used: str) -> str:
    title_date = target_date.strftime("%d/%m/%Y")
    source_lines = [f"- [{src.title}]({src.uri})" for src in sources[:40]]
    if not source_lines:
        source_lines = ["- Không trích xuất được nguồn grounding từ phản hồi Gemini."]

    source_lines.append("")
    source_lines.append(f"- Model: `{model_used}`")

    return f"""---
layout: post
title: "Điểm tin công nghệ Việt Nam và thế giới ngày {title_date}"
subtitle: "Tổng hợp nhanh các diễn biến công nghệ nổi bật trong ngày."
tags: [news, cong-nghe]
---

{body_markdown.strip()}

### Sources
{chr(10).join(source_lines)}
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate daily tech news post with Gemini + Google Search")
    parser.add_argument(
        "--date",
        help="Target date in YYYY-MM-DD (default: today in Asia/Ho_Chi_Minh)",
        default=None,
    )
    parser.add_argument(
        "--api-key",
        dest="api_key",
        default=None,
        help="Gemini API key (fallback to GEMINI_API_KEY/GOOGLE_API_KEY/API_KEY)",
    )
    args = parser.parse_args()

    now_local = dt.datetime.now(LOCAL_TZ)
    target_date = dt.date.fromisoformat(args.date) if args.date else now_local.date()
    api_key = _resolve_api_key(args.api_key)

    body, sources, model_used = generate_news_markdown(target_date=target_date, api_key=api_key)
    post_content = build_post(body, target_date=target_date, sources=sources, model_used=model_used)

    file_date = target_date - dt.timedelta(days=1)
    output_path = POSTS_DIR / f"{file_date.isoformat()}-{slugify('daily-tech-news')}.md"
    output_path.write_text(post_content.strip() + "\n", encoding="utf-8")

    print(f"Created/updated: {output_path}")
    print(f"Target date: {target_date.isoformat()} | Model used: {model_used} | Sources: {len(sources)}")


if __name__ == "__main__":
    main()
