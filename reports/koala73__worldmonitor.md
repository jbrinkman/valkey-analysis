# Valkey Integration Analysis: koala73/worldmonitor

**GitHub:** https://github.com/koala73/worldmonitor
**Analyzed:** 2026-05-02T01:40:32.793238+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 1 related issue(s)/PR(s) found. Redis modules used: redisai, redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** cache, time_series
- **Integration Type:** native
- **Redis Modules:** redisai, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (1 occurrences)

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 3 file(s)
  - [docs/railway-seed-consolidation-runbook.md](https://github.com/koala73/worldmonitor/blob/6d1931fb0391cfa95d6aba78f845723947e9469c/docs/railway-seed-consolidation-runbook.md)
  - [scripts/evaluate-forecast-run.mjs](https://github.com/koala73/worldmonitor/blob/6d1931fb0391cfa95d6aba78f845723947e9469c/scripts/evaluate-forecast-run.mjs)
  - [tests/energy-variant-atlas-guard.test.mts](https://github.com/koala73/worldmonitor/blob/6d1931fb0391cfa95d6aba78f845723947e9469c/tests/energy-variant-atlas-guard.test.mts)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 8 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #1966](https://github.com/koala73/worldmonitor/pull/1966): fix(consumer-prices): restore seed script + fix publish job writing to wrong Redis (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (218 occurrences)

**Redis module mentions:** ['redisai']
