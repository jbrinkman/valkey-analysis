# Valkey Integration Analysis: lobehub/lobehub

**GitHub:** https://github.com/lobehub/lobehub
**Analyzed:** 2026-05-02T01:40:32.802825+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | True |

## Summary

Explicit Valkey support detected. 4 related issue(s)/PR(s) found. 3 related extension repo(s) found (0 mention Valkey). Redis modules used: redisearch, redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** ioredis, redis
- **Use Cases:** time_series, vector_store
- **Integration Type:** native
- **Redis Modules:** redisearch, redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json

**Redis dependencies:**
- `redis` (redis-client)
- `ioredis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redisearch` / `ft.search`: 1 file(s)
- `redistimeseries` / `ts.add`: 48 file(s)
- `redisjson` / `rejson`: 2 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #13679](https://github.com/lobehub/lobehub/issues/13679): Agent failed to get Web Browsing skill only on the page of "Lobe AI" (open)
- [ISSUE #12085](https://github.com/lobehub/lobehub/issues/12085): [Bug] Cloudflare R2 asset URLs require `S3_PUBLIC_DOMAIN`, conflict with #4a87b31 (closed)
- [PR #10391](https://github.com/lobehub/lobehub/pull/10391): 🔨 chore: support to have Redis and providers (closed)
- [PR #8718](https://github.com/lobehub/lobehub/pull/8718): ⚡️ perf: try upstash redis for api performance (closed)

## Phase 5: Ecosystem

**Related repos in org (47 total org repos):**
- [chat-plugins-gateway](https://github.com/lobehub/chat-plugins-gateway): 🧩 / 🚪 Plugins Gateway - The LobeChat Plugins Gateway is a backend service that serves as a gateway for LobeChat plugins. We deploy this service using Vercel. The primary API POST /api/v1/runner is deployed as an Edge Function.
- [lobe-chat-plugins](https://github.com/lobehub/lobe-chat-plugins): 🧩 / 🏪  Plugin Index - This is the plugin index for LobeChat. It accesses index.json from this repository to display a list of available plugins for LobeChat to the user.
- [lobe-openai-plugins](https://github.com/lobehub/lobe-openai-plugins): 🧩 / 🌐 OpenAI Plugins Directory - collection that support Lobe Chat

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (28 occurrences)
- `ioredis` (1 occurrences)
