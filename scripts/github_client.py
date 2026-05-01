"""Shared GitHub API client with adaptive rate limiting based on response headers."""

import asyncio
import logging
import time

import httpx

from config import GITHUB_API_BASE, GITHUB_HEADERS, CONCURRENT_REQUESTS

log = logging.getLogger(__name__)


class RateLimiter:
    """Tracks rate limit state per GitHub resource from response headers."""

    def __init__(self):
        self._state: dict[str, dict] = {}
        self._locks: dict[str, asyncio.Lock] = {}

    def _get_lock(self, resource: str) -> asyncio.Lock:
        if resource not in self._locks:
            self._locks[resource] = asyncio.Lock()
        return self._locks[resource]

    def update(self, headers: httpx.Headers):
        """Update rate limit state from response headers."""
        resource = headers.get("x-ratelimit-resource", "core")
        remaining = headers.get("x-ratelimit-remaining")
        reset_at = headers.get("x-ratelimit-reset")
        limit = headers.get("x-ratelimit-limit")

        if remaining is not None and reset_at is not None:
            self._state[resource] = {
                "remaining": int(remaining),
                "reset_at": int(reset_at),
                "limit": int(limit) if limit else 0,
            }

    async def wait_if_needed(self, resource: str = "core"):
        """Wait if we're close to the rate limit for a resource."""
        async with self._get_lock(resource):
            state = self._state.get(resource)
            if not state:
                return

            remaining = state["remaining"]
            reset_at = state["reset_at"]

            # Keep a small buffer — don't use the last few requests
            buffer = max(2, state["limit"] // 50)

            if remaining <= buffer:
                wait_time = max(0, reset_at - time.time()) + 1
                if wait_time > 0:
                    log.warning(
                        "Rate limit low for %s: %d remaining, waiting %.0fs until reset",
                        resource, remaining, wait_time,
                    )
                    await asyncio.sleep(wait_time)

    def get_remaining(self, resource: str = "core") -> int | None:
        """Get remaining requests for a resource."""
        state = self._state.get(resource)
        return state["remaining"] if state else None

    def get_wait_time(self, resource: str = "core") -> float:
        """Get seconds until rate limit resets for a resource."""
        state = self._state.get(resource)
        if not state:
            return 0
        return max(0, state["reset_at"] - time.time())


# Singleton rate limiter
rate_limiter = RateLimiter()

# Semaphore for concurrency control
_sem = asyncio.Semaphore(CONCURRENT_REQUESTS)


async def github_get(client: httpx.AsyncClient, url: str, params: dict | None = None,
                     resource: str = "core") -> dict | list | None:
    """Make a rate-limit-aware GitHub API GET request."""
    await rate_limiter.wait_if_needed(resource)

    async with _sem:
        try:
            resp = await client.get(url, headers=GITHUB_HEADERS, params=params)
            rate_limiter.update(resp.headers)

            if resp.status_code == 403:
                # Check for rate limit vs other 403s
                if "rate limit" in resp.text.lower():
                    retry_after = resp.headers.get("retry-after")
                    if retry_after:
                        wait = int(retry_after)
                    else:
                        wait = max(0, rate_limiter.get_wait_time(resource)) + 1
                    log.warning("Rate limited on %s, waiting %.0fs", resource, wait)
                    await asyncio.sleep(wait)
                    resp = await client.get(url, headers=GITHUB_HEADERS, params=params)
                    rate_limiter.update(resp.headers)
                else:
                    log.debug("403 (not rate limit) for %s", url)
                    return None

            if resp.status_code == 404:
                return None

            resp.raise_for_status()
            return resp.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code != 404:
                log.warning("HTTP error for %s: %s", url, e)
            return None
        except Exception as e:
            log.warning("Request error for %s: %s", url, e)
            return None


async def github_post_graphql(client: httpx.AsyncClient, query: str, variables: dict) -> dict | None:
    """Make a rate-limit-aware GitHub GraphQL request."""
    await rate_limiter.wait_if_needed("graphql")

    async with _sem:
        try:
            resp = await client.post(
                "https://api.github.com/graphql",
                headers=GITHUB_HEADERS,
                json={"query": query, "variables": variables},
            )
            rate_limiter.update(resp.headers)

            if resp.status_code == 403:
                retry_after = resp.headers.get("retry-after")
                wait = int(retry_after) if retry_after else max(0, rate_limiter.get_wait_time("graphql")) + 1
                log.warning("GraphQL rate limited, waiting %.0fs", wait)
                await asyncio.sleep(wait)
                resp = await client.post(
                    "https://api.github.com/graphql",
                    headers=GITHUB_HEADERS,
                    json={"query": query, "variables": variables},
                )
                rate_limiter.update(resp.headers)

            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            log.debug("GraphQL error: %s", e)
            return None


async def github_search(client: httpx.AsyncClient, endpoint: str, params: dict,
                        resource: str = "code_search") -> dict | None:
    """Make a rate-limit-aware GitHub search request."""
    await rate_limiter.wait_if_needed(resource)

    async with _sem:
        try:
            resp = await client.get(
                f"{GITHUB_API_BASE}/{endpoint}",
                headers=GITHUB_HEADERS,
                params=params,
            )
            rate_limiter.update(resp.headers)

            if resp.status_code == 403:
                retry_after = resp.headers.get("retry-after")
                wait = int(retry_after) if retry_after else max(0, rate_limiter.get_wait_time(resource)) + 1
                log.warning("Search rate limited on %s, waiting %.0fs", resource, wait)
                await asyncio.sleep(wait)
                resp = await client.get(
                    f"{GITHUB_API_BASE}/{endpoint}",
                    headers=GITHUB_HEADERS,
                    params=params,
                )
                rate_limiter.update(resp.headers)

            if resp.status_code == 422:
                log.debug("Search validation error: %s", resp.text[:200])
                return None

            resp.raise_for_status()
            return resp.json()
        except Exception as e:
            log.warning("Search error: %s", e)
            return None


def log_rate_status():
    """Log current rate limit status for all tracked resources."""
    for resource, state in rate_limiter._state.items():
        remaining = state["remaining"]
        limit = state["limit"]
        wait = max(0, state["reset_at"] - time.time())
        log.info("Rate limit %s: %d/%d remaining (resets in %.0fs)", resource, remaining, limit, wait)
