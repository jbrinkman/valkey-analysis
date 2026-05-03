# Valkey Integration Analysis: risingwavelabs/risingwave

**GitHub:** https://github.com/risingwavelabs/risingwave
**Analyzed:** 2026-05-02T01:40:32.844875+00:00

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

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: Cargo.toml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 12 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #21050](https://github.com/risingwavelabs/risingwave/pull/21050): chore(deps): Bump redis from 0.25.4 to 0.28.2 (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (37 occurrences)
