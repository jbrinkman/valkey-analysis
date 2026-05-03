# Valkey Integration Analysis: agno-agi/agno

**GitHub:** https://github.com/agno-agi/agno
**Analyzed:** 2026-05-02T01:40:32.706022+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. 1 related issue(s)/PR(s) found. Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 4 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #5005](https://github.com/agno-agi/agno/pull/5005): Feat/add valkey search (open)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (50 occurrences)
- `redis-py` (1 occurrences)
