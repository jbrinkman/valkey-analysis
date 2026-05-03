# Valkey Integration Analysis: chatwoot/chatwoot

**GitHub:** https://github.com/chatwoot/chatwoot
**Analyzed:** 2026-05-02T01:40:32.732565+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis. 2 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json, Gemfile

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 11 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (70 total org repos):**
- [contributors](https://github.com/chatwoot/contributors): None
- [chatwoot-contributors](https://github.com/chatwoot/chatwoot-contributors): None

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (440 occurrences)
