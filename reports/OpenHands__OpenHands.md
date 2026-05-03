# Valkey Integration Analysis: OpenHands/OpenHands

**GitHub:** https://github.com/OpenHands/OpenHands
**Analyzed:** 2026-05-02T01:40:32.678685+00:00

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

Manifests checked: pyproject.toml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (39 total org repos):**
- [community-pr-dashboard](https://github.com/OpenHands/community-pr-dashboard): None
- [extensions](https://github.com/OpenHands/extensions): Public registry for OpenHands extensions.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (125 occurrences)
