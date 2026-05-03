# Valkey Integration Analysis: PrefectHQ/fastmcp

**GitHub:** https://github.com/PrefectHQ/fastmcp
**Analyzed:** 2026-05-02T01:40:32.682998+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 6 related issue(s)/PR(s) found. 1 related discussion(s) found. Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 8 file(s)
  - [examples/tasks/README.md](https://github.com/PrefectHQ/fastmcp/blob/d0315974fa844b2424c93f4ad43c8f2d543ff51a/examples/tasks/README.md)
  - [src/fastmcp/cli/tasks.py](https://github.com/PrefectHQ/fastmcp/blob/d0315974fa844b2424c93f4ad43c8f2d543ff51a/src/fastmcp/cli/tasks.py)
  - [docs/python-sdk/fastmcp-cli-tasks.mdx](https://github.com/PrefectHQ/fastmcp/blob/d0315974fa844b2424c93f4ad43c8f2d543ff51a/docs/python-sdk/fastmcp-cli-tasks.mdx)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 2 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #2479](https://github.com/PrefectHQ/fastmcp/issues/2479): OAuth Refresh Tokens Lost on Server Restart (closed)
- [ISSUE #2310](https://github.com/PrefectHQ/fastmcp/issues/2310): Update references to py-key-value in the docs (closed)
- [ISSUE #1577](https://github.com/PrefectHQ/fastmcp/issues/1577): FastMCP OAuth Proxy should support token storage like Redis/Valkey instead of in memory (closed)
- [PR #3810](https://github.com/PrefectHQ/fastmcp/pull/3810): chore(deps-dev): update fakeredis requirement from <2.35.0 to <2.36.0 (closed)
- [PR #2454](https://github.com/PrefectHQ/fastmcp/pull/2454): Add distributed task workers and example (closed)
- [PR #1913](https://github.com/PrefectHQ/fastmcp/pull/1913): Add Storage to FastMCP and switch OAuth to use it (closed)

**Discussions:**
- [Discussion #4086](https://github.com/PrefectHQ/fastmcp/discussions/4086): Should durable OAuth state (client registrations, refresh tokens) use a durable (as in ACID) store?

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (27 occurrences)
