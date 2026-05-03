# Valkey Integration Analysis: vllm-project/semantic-router

**GitHub:** https://github.com/vllm-project/semantic-router
**Analyzed:** 2026-05-02T01:40:32.885931+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | True |
| RediSearch Usage | True |

## Summary

Explicit Valkey support detected. Valkey-Glide client library detected. 20 related issue(s)/PR(s) found. Redis modules used: redisearch, redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series, vector_store
- **Integration Type:** none
- **Redis Modules:** redisearch, redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 56 file(s)
  - [tools/make/valkey.mk](https://github.com/vllm-project/semantic-router/blob/e3c9bc82f67f58634759daf21ac408a6d924b126/tools/make/valkey.mk)
  - [website/docs/installation/valkey-memory.md](https://github.com/vllm-project/semantic-router/blob/e3c9bc82f67f58634759daf21ac408a6d924b126/website/docs/installation/valkey-memory.md)
  - [deploy/addons/valkey/valkey-cache.go](https://github.com/vllm-project/semantic-router/blob/e3c9bc82f67f58634759daf21ac408a6d924b126/deploy/addons/valkey/valkey-cache.go)

**Valkey-Glide code references:**
- `valkey-glide`: 11 file(s)

**Redis module code references:**
- `redisearch` / `ft.search`: 10 file(s)
- `redistimeseries` / `ts.add`: 8 file(s)
- `redisjson` / `rejson`: 3 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #1776](https://github.com/vllm-project/semantic-router/issues/1776): Require valkey-search ≥ 1.2.0 for TEXT field support in query index (closed)
- [ISSUE #15](https://github.com/vllm-project/semantic-router/issues/15): vLLM Semantic Router WG Initialization 👋 (open)
- [ISSUE #1695](https://github.com/vllm-project/semantic-router/issues/1695): feature: Valkey backend for agentic memory (open)
- [ISSUE #1611](https://github.com/vllm-project/semantic-router/issues/1611): feature: Valkey vector store backend (closed)
- [ISSUE #1484](https://github.com/vllm-project/semantic-router/issues/1484): feature: add a Valkey cache backend (closed)
- [PR #1842](https://github.com/vllm-project/semantic-router/pull/1842): Feat/model switch gate (closed)
- [PR #1806](https://github.com/vllm-project/semantic-router/pull/1806): [Router][Bugfix]: Pre-check search module version before FT.CREATE (closed)
- [PR #1800](https://github.com/vllm-project/semantic-router/pull/1800): feature: Persist SessionID and TurnIndex into replay records for multi-turn trajectory stitching (closed)
- [PR #1739](https://github.com/vllm-project/semantic-router/pull/1739): [Router] Add Valkey memory backend with TLS support (closed)
- [PR #1788](https://github.com/vllm-project/semantic-router/pull/1788): fix: flaky TestValkeyStoreInteg_List ordering in CI (closed)
- [PR #1772](https://github.com/vllm-project/semantic-router/pull/1772): [Router][CLI][Dashboard] Add Redis-backed startup status with API endpoint (closed)
- [PR #1733](https://github.com/vllm-project/semantic-router/pull/1733): [Router][CLI][E2E] Add durable MetadataRegistry for vector store and file metadata (closed)
- [PR #1727](https://github.com/vllm-project/semantic-router/pull/1727): Add cross-model global budget rate limiting with Valkey provider (open)
- [PR #1762](https://github.com/vllm-project/semantic-router/pull/1762): [Router][Bugfix]: parseBestMatch select best match from all KNN candidates (closed)
- [PR #1737](https://github.com/vllm-project/semantic-router/pull/1737): [Router] Fix: wire Valkey config into createSemanticCache (closed)
- [PR #1726](https://github.com/vllm-project/semantic-router/pull/1726): Add cross-model global budget rate limiting with Valkey provider (closed)
- [PR #1663](https://github.com/vllm-project/semantic-router/pull/1663): [CI/Build][Misc] simplify harness context, skills, and PR gates (closed)
- [PR #1671](https://github.com/vllm-project/semantic-router/pull/1671): [Feat] Valkey vector store implementation (closed)
- [PR #1540](https://github.com/vllm-project/semantic-router/pull/1540): feat: initial implementation of valkey cache backend (closed)
- [PR #1535](https://github.com/vllm-project/semantic-router/pull/1535): [Router][Feat] Add Valkey semantic cache backend support (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Valkey mentions:**
- `valkey` (50 occurrences)
  - `Sources:        README.md  12-31         website/docs/intro.md  88-94                   Dismiss   Refresh this wiki  Enter email to refresh    On this page    Overview    High-Level Architecture    Si`

**Redis mentions:** 2 keyword(s) found
- `redis` (252 occurrences)
- `go-redis` (2 occurrences)

**Redis module mentions:** ['redisearch']
