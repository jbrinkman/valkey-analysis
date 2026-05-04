"""LLM-based sentiment analysis for Valkey mentions using OpenRouter."""

import asyncio
import json
import logging

import httpx

from config import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL

log = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are analyzing text from open-source project documentation, issues, and code to determine the project's level of Valkey support.

Classify each text snippet into exactly one category:

POSITIVE — The project explicitly supports, integrates with, or provides functionality for Valkey. Examples:
- "Added Valkey as a supported backend"
- "Valkey vector store integration"
- Import statements for valkey client libraries

NEGATIVE — The text indicates Valkey is NOT supported, incompatible, or has known issues. Examples:
- "Valkey is not supported"
- "Incompatible with ElastiCache Valkey"
- "TEXT field not supported in Valkey"
- "best-effort basis" or "not guaranteed" language about Valkey

NEUTRAL — Valkey is mentioned but not in the context of support or integration. Examples:
- Operational issues ("pods restart after valkey update")
- Passing mentions in comparisons or lists
- Configuration examples that happen to mention valkey
- Variable names or identifiers containing "valkey"

Respond with ONLY a JSON object: {"sentiment": "POSITIVE|NEGATIVE|NEUTRAL", "reason": "brief explanation"}"""


async def classify_mention(client: httpx.AsyncClient, text: str, context: str = "") -> dict:
    """Classify a Valkey mention's sentiment using LLM.

    Args:
        client: httpx async client
        text: The text containing the Valkey mention
        context: Additional context (e.g., source file, repo name)

    Returns:
        {"sentiment": "POSITIVE|NEGATIVE|NEUTRAL", "reason": "..."}
    """
    if not OPENROUTER_API_KEY:
        log.warning("OPENROUTER_API_KEY not set, falling back to keyword-based sentiment")
        return _keyword_fallback(text)

    user_msg = f"Context: {context}\n\nText to classify:\n{text[:1500]}"

    try:
        resp = await client.post(
            f"{OPENROUTER_BASE_URL}/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": OPENROUTER_MODEL,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_msg},
                ],
                "temperature": 0,
                "max_tokens": 150,
            },
            timeout=30,
        )
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"].strip()

        # Parse JSON response
        # Handle cases where LLM wraps in markdown code block
        if content.startswith("```"):
            content = content.split("```")[1]
            if content.startswith("json"):
                content = content[4:]
        result = json.loads(content)
        sentiment = result.get("sentiment", "NEUTRAL").upper()
        if sentiment not in ("POSITIVE", "NEGATIVE", "NEUTRAL"):
            sentiment = "NEUTRAL"
        return {"sentiment": sentiment, "reason": result.get("reason", "")}

    except Exception as e:
        log.debug("LLM sentiment error: %s", e)
        return _keyword_fallback(text)


async def classify_mentions_batch(client: httpx.AsyncClient, mentions: list[dict]) -> list[dict]:
    """Classify a batch of mentions. Each mention should have 'text' and optional 'context'.

    Returns list of {"sentiment": ..., "reason": ...} in same order.
    """
    results = []
    for mention in mentions:
        result = await classify_mention(
            client,
            mention.get("text", ""),
            mention.get("context", ""),
        )
        results.append(result)
    return results


def _keyword_fallback(text: str) -> dict:
    """Fallback keyword-based sentiment when LLM is unavailable."""
    text_lower = text.lower()

    negative_patterns = [
        "not supported", "not compatible", "incompatible", "doesn't work",
        "does not work", "doesn't support", "does not support", "not working",
        "won't work", "will not work", "cannot use", "can't use",
        "unable to", "fails with", "broken with", "not available",
        "unsupported", "no support", "best-effort", "best effort",
        "not guaranteed", "not tested", "experimental support",
        "may not work", "might not work", "limited support",
    ]

    positive_patterns = [
        "valkey support", "supports valkey", "valkey integration",
        "valkey backend", "valkey driver", "valkey client",
        "add valkey", "added valkey", "valkey adapter",
        "import valkey", "from valkey", "require.*valkey",
    ]

    for p in negative_patterns:
        if p in text_lower:
            return {"sentiment": "NEGATIVE", "reason": f"Contains '{p}'"}

    for p in positive_patterns:
        if p in text_lower:
            return {"sentiment": "POSITIVE", "reason": f"Contains '{p}'"}

    return {"sentiment": "NEUTRAL", "reason": "No strong signal detected"}
