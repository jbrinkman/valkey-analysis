# Valkey Integration Analysis: lintsinghua/DeepAudit

**GitHub:** https://github.com/lintsinghua/DeepAudit
**Analyzed:** 2026-05-02T01:40:32.801421+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (1 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 2 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 4 keyword(s) found
- `redis` (356 occurrences)
- `redis-py` (1 occurrences)
- `ioredis` (1 occurrences)
- `aioredis` (1 occurrences)

**Redis module mentions:** ['redistimeseries']
