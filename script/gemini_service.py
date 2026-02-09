"""Gemini-powered repository analyzer (Python port of geminiService.ts).

The function below mirrors the TypeScript implementation but uses the
`google-genai` Python SDK. It takes a GitHub repository URL and returns
structured JSON describing the project (title, subtitle, sections, sources).
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List


def _resolve_api_key(explicit: str | None) -> str:
    key = explicit or os.getenv("API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError(
            "Missing Gemini API key. Set API_KEY or GOOGLE_API_KEY, or pass --api-key."
        )
    return key


def _parse_sources(response: Any) -> List[Dict[str, str]]:
    """Extract grounded web sources from the model response, if present."""

    sources: List[Dict[str, str]] = []
    try:
        candidate = response.candidates[0]
    except Exception:
        return sources

    grounding = getattr(candidate, "grounding_metadata", None) or getattr(
        candidate, "groundingMetadata", None
    )
    if not grounding:
        return sources

    chunks = getattr(grounding, "grounding_chunks", None) or getattr(
        grounding, "groundingChunks", None
    )
    if not chunks:
        return sources

    for chunk in chunks:
        web = getattr(chunk, "web", None)
        if web:
            title = getattr(web, "title", None) or "Resource"
            uri = getattr(web, "uri", None) or ""
            sources.append({"title": title, "uri": uri})

    return sources


def analyze_repository(repo_url: str, api_key: str | None = None) -> Dict[str, Any]:
    """Call Gemini to analyze a repository and return a structured dict.

    Args:
        repo_url: Full GitHub repository URL.
        api_key: Optional explicit API key (falls back to env vars).

    Returns:
        Dict with repoTitle, repoSubtitle, sections, sources.
    """

    try:
        from google import genai
        from google.genai import types
    except ImportError as exc:  # pragma: no cover - library may be absent locally
        raise RuntimeError(
            "google-genai not installed. Install with `pip install google-genai`."
        ) from exc

    client = genai.Client(api_key=_resolve_api_key(api_key))

    schema = types.Schema(
        type=types.Type.OBJECT,
        properties={
            "repoTitle": types.Schema(type=types.Type.STRING),
            "repoSubtitle": types.Schema(type=types.Type.STRING),
            "sections": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "title": types.Schema(type=types.Type.STRING),
                        "content": types.Schema(type=types.Type.STRING),
                    },
                    required=["title", "content"],
                ),
            ),
        },
        required=["repoTitle", "repoSubtitle", "sections"],
    )

    prompt = f"""
    Analyze the following GitHub repository: {repo_url}

    1. Extract the repository name or create a concise title as 'repoTitle'.
    2. Create a short, engaging subtitle (one sentence) summarizing the project's purpose as 'repoSubtitle'.
    3. Provide a comprehensive guide in Vietnamese (Tiếng Việt) organized into the following sections:

    - Giới thiệu: Giải thích repository này giải quyết vấn đề gì, ứng dụng thực tế vào việc gì.
    - Tính năng chính: Liệt kê các tính năng quan trọng nhất.
    - Hướng dẫn cài đặt Local (macOS): Các bước chi tiết để chạy project trên macOS (Homebrew, dependencies, ENV...).
    - Hướng dẫn Docker (nếu có): Cách build và run bằng Docker. Nếu không có Dockerfile, hãy gợi ý cách viết một cái cơ bản.
    - Ví dụ Code (Example Code): Viết một đoạn code mẫu minh họa cách sử dụng project này.

    Return the response as a JSON object.
    """

    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearchRetrieval())],
            response_mime_type="application/json",
            response_schema=schema,
        ),
    )

    text = response.text or "{}"
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        data = {}

    fallback_title = repo_url.rstrip("/").split("/")[-1] or "Repository"

    return {
        "repoTitle": data.get("repoTitle") or fallback_title,
        "repoSubtitle": data.get("repoSubtitle") or f"Analysis of {fallback_title}",
        "sections": data.get("sections") or [],
        "sources": _parse_sources(response),
    }


__all__ = ["analyze_repository"]
