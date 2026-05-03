# Valkey Integration Analysis: ray-project/ray

**GitHub:** https://github.com/ray-project/ray
**Analyzed:** 2026-05-02T01:40:32.842067+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 4 related issue(s)/PR(s) found. 8 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** extension
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 34 file(s)
- `redisjson` / `rejson`: 3 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #53475](https://github.com/ray-project/ray/issues/53475): [Ray Serve] GCS Segmentation Fault on failed Redis requests (open)
- [ISSUE #47447](https://github.com/ray-project/ray/issues/47447): [Ray dashboard]  Actors tab does not list actors under certain conditions (open)
- [ISSUE #44641](https://github.com/ray-project/ray/issues/44641): [Core] Discussion to support Valkey instead of or alongside Redis  (open)
- [PR #48225](https://github.com/ray-project/ray/pull/48225): [Core] support redis/valkey authentication with username (closed)

## Phase 5: Ecosystem

**Related repos in org (126 total org repos):**
- [redis-ms](https://github.com/ray-project/redis-ms): Redis is an in-memory database that persists on disk. The data model is key-value, but many different kind of values are supported: Strings, Lists, Sets, Sorted Sets, Hashes 🔴 Redis
- [bredis](https://github.com/ray-project/bredis): Experiments with sharding redis
- [redis-replication](https://github.com/ray-project/redis-replication): Replicating redis
- [credis](https://github.com/ray-project/credis): None 🔴 Redis
- [contrib-workflow-dag](https://github.com/ray-project/contrib-workflow-dag): None
- [community](https://github.com/ray-project/community): Artifacts intended to support the Ray Developer Community: SIGs, RFC overviews, and governance. We're very glad you're here! ✨
- [ray-runtime-env-plugins](https://github.com/ray-project/ray-runtime-env-plugins): A set of runtime environment plugins which can be used by the public.
- [redis](https://github.com/ray-project/redis): For developers, who are building real-time data-driven applications, Redis is the preferred, fastest, and most feature-rich cache, data structure server, and document and vector query engine. 🔴 Redis

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (9 occurrences)
