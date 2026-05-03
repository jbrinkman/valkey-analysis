# Valkey Integration Analysis: metabase/metabase

**GitHub:** https://github.com/metabase/metabase
**Analyzed:** 2026-05-02T01:40:32.809981+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 1 related issue(s)/PR(s) found. Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 3 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #48376](https://github.com/metabase/metabase/pull/48376): Simple API for storing KV pairs per-user (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (1 occurrences)
