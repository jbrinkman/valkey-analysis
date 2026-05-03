# Valkey Integration Analysis: sgl-project/sglang

**GitHub:** https://github.com/sgl-project/sglang
**Analyzed:** 2026-05-02T01:40:32.850193+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 3 related issue(s)/PR(s) found. Redis modules used: redistimeseries.

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
- `redistimeseries` / `ts.add`: 11 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #17604](https://github.com/sgl-project/sglang/issues/17604): [Feature] Valkey HiCacheStore Adapter (closed)
- [PR #16823](https://github.com/sgl-project/sglang/pull/16823): Introduce Valkey HiCacheStore adapter (open)
- [PR #4508](https://github.com/sgl-project/sglang/pull/4508): Introduce session cache (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (4 occurrences)
