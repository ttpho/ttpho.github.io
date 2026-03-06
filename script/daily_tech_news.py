#!/usr/bin/env python3
"""Generate a daily Vietnam + global tech news post for Jekyll."""

from __future__ import annotations

import argparse
import datetime as dt
import html
import os
import re
import urllib.parse
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from zoneinfo import ZoneInfo

import feedparser


ROOT_DIR = Path(__file__).resolve().parent.parent
POSTS_DIR = ROOT_DIR / "_posts"
LOCAL_TZ = ZoneInfo("Asia/Ho_Chi_Minh")

VN_FEEDS = {
    "Dân Trí Công Nghệ": "https://dantri.com.vn/rss/cong-nghe.rss",
    "Thanh Niên Công Nghệ": "https://thanhnien.vn/rss/cong-nghe.rss",
    "Tuổi Trẻ Nhịp Sống Số": "https://tuoitre.vn/rss/nhip-song-so.rss",
    "VietnamNet Công Nghệ": "https://vietnamnet.vn/rss/cong-nghe.rss",
    "24h Công Nghệ": "https://cdn.24h.com.vn/upload/rss/congnghethongtin.rss",
}

GLOBAL_FEEDS = {
    "TechCrunch": "https://techcrunch.com/feed/",
    "The Verge": "https://www.theverge.com/rss/index.xml",
    "Wired": "https://www.wired.com/feed/rss",
    "Google Developers Blog": "https://developers.googleblog.com/feeds/posts/default?alt=rss",
    "Google Cloud Blog": "https://cloudblog.withgoogle.com/rss/",
    "Google Research Blog": "https://research.google/blog/rss/",
    "OpenAI News": "https://openai.com/news/rss.xml",
    "Meta Engineering Blog": "https://engineering.fb.com/feed/",
    "AWS News Blog": "https://aws.amazon.com/blogs/aws/feed/",
    "AWS Architecture Blog": "https://aws.amazon.com/blogs/architecture/feed/",
    "Microsoft Research Blog": "https://www.microsoft.com/en-us/research/feed/",
    "Azure Blog": "https://azure.microsoft.com/en-us/blog/feed/",
    "NVIDIA Blog": "https://blogs.nvidia.com/feed/",
    "Apple ML Research": "https://machinelearning.apple.com/rss.xml",
}

GOOGLE_NEWS_SITE_FEEDS = {
    "Google Search Central Blog": "site:developers.google.com/search/blog Google Search Central",
    "Anthropic News": "site:anthropic.com/news Anthropic",
    "Meta AI Blog": "site:ai.meta.com/blog Meta AI",
    "Cursor Blog": "site:cursor.com/blog Cursor",
    "Alibaba Cloud Community": "site:alibabacloud.com/blog Alibaba Cloud",
}


@dataclass
class Article:
    title: str
    link: str
    source: str
    summary: str
    published_local: dt.datetime | None
    region: str


def slugify(text: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower())
    cleaned = re.sub(r"-+", "-", cleaned).strip("-")
    return cleaned or "daily-tech-news"


def _strip_html(text: str) -> str:
    no_tags = re.sub(r"<[^>]+>", " ", text or "")
    no_spaces = re.sub(r"\s+", " ", no_tags).strip()
    no_spaces = html.unescape(no_spaces)
    return no_spaces


def _entry_datetime(entry) -> dt.datetime | None:
    for field in ("published_parsed", "updated_parsed", "created_parsed"):
        parsed = getattr(entry, field, None)
        if parsed:
            try:
                return dt.datetime.fromtimestamp(
                    dt.datetime(*parsed[:6], tzinfo=dt.timezone.utc).timestamp(),
                    tz=LOCAL_TZ,
                )
            except Exception:
                return None
    return None


def _safe_text(entry, name: str, default: str = "") -> str:
    return str(getattr(entry, name, default) or default).strip()


def _google_news_rss(query: str, hl: str = "en-US", gl: str = "US", ceid: str = "US:en") -> str:
    encoded = urllib.parse.quote(query, safe="")
    return f"https://news.google.com/rss/search?q={encoded}&hl={hl}&gl={gl}&ceid={ceid}"


def fetch_articles(
    feeds: dict[str, str],
    region: str,
    target_date: dt.date,
    max_per_feed: int = 8,
) -> list[Article]:
    result: list[Article] = []
    for source, url in feeds.items():
        parsed = feedparser.parse(url)
        today_items: list[Article] = []
        latest_items: list[Article] = []
        for entry in parsed.entries:
            published_local = _entry_datetime(entry)

            title = html.unescape(_safe_text(entry, "title"))
            link = _safe_text(entry, "link")
            if not title or not link:
                continue

            summary = _strip_html(_safe_text(entry, "summary") or _safe_text(entry, "description"))
            article = Article(
                title=title,
                link=link,
                source=source,
                summary=summary[:300],
                published_local=published_local,
                region=region,
            )
            latest_items.append(article)

            if published_local and published_local.date() != target_date:
                continue

            today_items.append(article)

        chosen_items = today_items[:max_per_feed] if today_items else latest_items[:max_per_feed]
        result.extend(chosen_items)
    return result


def sort_articles(articles: Iterable[Article]) -> list[Article]:
    return sorted(
        articles,
        key=lambda a: (
            a.published_local is None,
            a.published_local or dt.datetime.min.replace(tzinfo=LOCAL_TZ),
        ),
        reverse=True,
    )


def _resolve_api_key(explicit: str | None) -> str | None:
    return explicit or os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY") or os.getenv("API_KEY")


def _render_fallback(vn: list[Article], global_news: list[Article]) -> str:
    lines = [
        "## Tổng quan",
        "",
        f"Hôm nay có **{len(vn)}** tin công nghệ Việt Nam và **{len(global_news)}** tin công nghệ thế giới nổi bật.",
        "",
        "## Tin công nghệ Việt Nam",
        "",
    ]

    if vn:
        for item in vn[:10]:
            lines.append(f"- [{item.title}]({item.link}) ({item.source})")
    else:
        lines.append("- Chưa thu thập được tin Việt Nam trong ngày từ các RSS đã cấu hình.")

    lines.extend(["", "## Tin công nghệ thế giới", ""])
    if global_news:
        for item in global_news[:10]:
            lines.append(f"- [{item.title}]({item.link}) ({item.source})")
    else:
        lines.append("- Chưa thu thập được tin thế giới trong ngày từ các RSS đã cấu hình.")

    return "\n".join(lines).strip()


def summarize_with_gemini(vn: list[Article], global_news: list[Article], api_key: str | None) -> str:
    if not api_key:
        return _render_fallback(vn, global_news)

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        return _render_fallback(vn, global_news)

    def as_block(items: list[Article]) -> str:
        rows = []
        for idx, item in enumerate(items[:20], start=1):
            published = item.published_local.strftime("%Y-%m-%d %H:%M") if item.published_local else "N/A"
            rows.append(
                f"{idx}. {item.title}\n"
                f"   - source: {item.source}\n"
                f"   - time: {published} (+07)\n"
                f"   - link: {item.link}\n"
                f"   - summary: {item.summary or 'N/A'}"
            )
        return "\n".join(rows) if rows else "Không có dữ liệu."

    prompt = f"""
Bạn là biên tập viên bản tin công nghệ.
Hãy viết nội dung markdown bằng tiếng Việt, ngắn gọn, dễ đọc theo đúng cấu trúc sau:

## Tổng quan
- 3 đến 5 gạch đầu dòng nêu xu hướng chính trong ngày.

## Tin công nghệ Việt Nam
- Liệt kê tối đa 8 tin nổi bật dạng bullet.
- Mỗi bullet bắt đầu bằng tiêu đề ngắn, sau đó 1 câu phân tích tác động.

## Tin công nghệ thế giới
- Liệt kê tối đa 8 tin nổi bật dạng bullet.
- Mỗi bullet bắt đầu bằng tiêu đề ngắn, sau đó 1 câu phân tích tác động.

Yêu cầu:
- Chỉ sử dụng thông tin trong dữ liệu đầu vào bên dưới.
- Không bịa nguồn, không thêm section khác ngoài 3 section trên.
- Không thêm phần "Sources" (hệ thống sẽ tự chèn).

[DỮ LIỆU VIỆT NAM]
{as_block(vn)}

[DỮ LIỆU THẾ GIỚI]
{as_block(global_news)}
"""

    client = genai.Client(api_key=api_key)
    model_candidates = ["gemini-2.5-flash", "gemini-2.0-flash", "gemini-1.5-flash"]
    for model_name in model_candidates:
        try:
            response = client.models.generate_content(
                model=model_name,
                contents=prompt,
                config=types.GenerateContentConfig(temperature=0.4),
            )
            text = (response.text or "").strip()
            if text:
                return text
        except Exception:
            continue

    return _render_fallback(vn, global_news)


def build_post(
    body_markdown: str,
    target_date: dt.date,
    all_articles: list[Article],
) -> str:
    title_date = target_date.strftime("%d/%m/%Y")
    source_lines: list[str] = []
    seen: set[str] = set()
    for item in all_articles:
        if item.link in seen:
            continue
        seen.add(item.link)
        source_lines.append(f"- [{item.source}: {item.title}]({item.link})")

    sources = "\n".join(source_lines[:30]) if source_lines else "- Chưa có nguồn dữ liệu phù hợp trong ngày."

    return f"""---
layout: post
title: "Điểm tin công nghệ Việt Nam và thế giới ngày {title_date}"
subtitle: "Tổng hợp nhanh các diễn biến công nghệ nổi bật trong ngày."
tags: [news, cong-nghe]
---

{body_markdown.strip()}

### Sources
{sources}
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate daily tech news post")
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

    global_fallback_feeds = {
        source: _google_news_rss(query) for source, query in GOOGLE_NEWS_SITE_FEEDS.items()
    }

    vn_news = sort_articles(fetch_articles(VN_FEEDS, region="vn", target_date=target_date))
    global_news = sort_articles(
        [
            *fetch_articles(GLOBAL_FEEDS, region="global", target_date=target_date),
            *fetch_articles(global_fallback_feeds, region="global", target_date=target_date),
        ]
    )
    all_articles = sort_articles([*vn_news, *global_news])

    body = summarize_with_gemini(vn_news, global_news, api_key=_resolve_api_key(args.api_key))
    post_content = build_post(body, target_date=target_date, all_articles=all_articles)

    slug = slugify(f"daily-tech-news-{target_date.isoformat()}")
    output_path = POSTS_DIR / f"{target_date.isoformat()}-{slug}.md"
    output_path.write_text(post_content.strip() + "\n", encoding="utf-8")
    print(f"Created/updated: {output_path}")
    print(f"VN items: {len(vn_news)}, Global items: {len(global_news)}")


if __name__ == "__main__":
    main()
