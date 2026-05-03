# Valkey Integration Analysis: open-webui/open-webui

**GitHub:** https://github.com/open-webui/open-webui
**Analyzed:** 2026-05-02T01:40:32.830817+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 18 related issue(s)/PR(s) found. 10 related discussion(s) found. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** session_store, time_series
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml, package.json

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (1 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 5 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #21515](https://github.com/open-webui/open-webui/issues/21515): issue: OOM while compress_audio (closed)
- [ISSUE #19834](https://github.com/open-webui/open-webui/issues/19834): Does not deploy on TrueNAS (closed)
- [ISSUE #18223](https://github.com/open-webui/open-webui/issues/18223): issue: Redis exception in ydoc manager when working with aws elasticache  (closed)
- [ISSUE #16157](https://github.com/open-webui/open-webui/issues/16157): issue: Backend cannot connect to Redis in cluster mode (closed)
- [ISSUE #16018](https://github.com/open-webui/open-webui/issues/16018): feat: Allow websocket to connect to external Redis over TLS (closed)
- [ISSUE #8074](https://github.com/open-webui/open-webui/issues/8074): infra: Network Problem 0.5+ (closed)
- [ISSUE #11669](https://github.com/open-webui/open-webui/issues/11669): issue: Model appears in selection dropdown while being disabled (closed)
- [ISSUE #9995](https://github.com/open-webui/open-webui/issues/9995): web search using searxng: No search query generated (closed)
- [PR #19799](https://github.com/open-webui/open-webui/pull/19799): feat: introduce REDIS_SOCKET_CONNECT_TIMEOUT with sane default (for smooth failover) (closed)
- [PR #19504](https://github.com/open-webui/open-webui/pull/19504): feat: Implemented redis hash TTL to enable accurate live user count. (closed)
- [PR #19449](https://github.com/open-webui/open-webui/pull/19449): build(deps): bump the pip group across 2 directories with 2 updates (closed)
- [PR #19404](https://github.com/open-webui/open-webui/pull/19404): build(deps): bump the pip group across 2 directories with 2 updates (closed)
- [PR #19232](https://github.com/open-webui/open-webui/pull/19232): fix/refactor: optimize Redis key scanning in YdocManager (closed)
- [PR #18971](https://github.com/open-webui/open-webui/pull/18971): chore(deps): bump the pip group across 2 directories with 2 updates (closed)
- [PR #18813](https://github.com/open-webui/open-webui/pull/18813): chore(deps): bump python-socketio from 5.13.0 to 5.14.3 in /backend (closed)
- [PR #18520](https://github.com/open-webui/open-webui/pull/18520): chore(deps): bump the pip group across 2 directories with 2 updates (closed)
- [PR #18519](https://github.com/open-webui/open-webui/pull/18519): chore(deps): bump the pip group across 2 directories with 2 updates (closed)
- [PR #18370](https://github.com/open-webui/open-webui/pull/18370): chore(deps): bump the pip group across 2 directories with 1 update (closed)

**Discussions:**
- [Discussion #21619](https://github.com/open-webui/open-webui/discussions/21619): issue: OOM while compress_audio
- [Discussion #20316](https://github.com/open-webui/open-webui/discussions/20316): Open WebUI Stack – Production-Ready* with Observability (LGTM), LiteLLM, Qdrant, Traefik
- [Discussion #19661](https://github.com/open-webui/open-webui/discussions/19661): WebSocket Handshake Fails with "Unexpected token ':', ": OPENROUT"..." (OpenRouter Error Leakage?)
- [Discussion #11689](https://github.com/open-webui/open-webui/discussions/11689): issue: Model appears in selection dropdown while being disabled
- [Discussion #19851](https://github.com/open-webui/open-webui/discussions/19851): Does not deploy on TrueNAS
- [Discussion #15834](https://github.com/open-webui/open-webui/discussions/15834): issue: Redis in Cluster Mode - Keys in request don't hash to the same slot
- [Discussion #18251](https://github.com/open-webui/open-webui/discussions/18251): issue: Redis exception in ydoc manager when working with aws elasticache
- [Discussion #9871](https://github.com/open-webui/open-webui/discussions/9871): Support for different redis configurations (Cluster, Sentinel)
- [Discussion #15102](https://github.com/open-webui/open-webui/discussions/15102): TLS support for Redis websocket connections
- [Discussion #13222](https://github.com/open-webui/open-webui/discussions/13222): Are postgres and redis optional?

## Phase 5: Ecosystem

**Related repos in org (21 total org repos):**
- [community-platform](https://github.com/open-webui/community-platform): None

## DeepWiki Analysis

**Redis mentions:** 3 keyword(s) found
- `redis` (587 occurrences)
- `ioredis` (1 occurrences)
- `aioredis` (1 occurrences)
