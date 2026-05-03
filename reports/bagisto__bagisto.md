# Valkey Integration Analysis: bagisto/bagisto

**GitHub:** https://github.com/bagisto/bagisto
**Analyzed:** 2026-05-02T01:40:32.720799+00:00

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

- **Client Libraries:** predis/predis, redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json, composer.json

**Redis dependencies:**
- `redis` (redis-client)
- `predis/predis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 5 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #11024](https://github.com/bagisto/bagisto/pull/11024): chore(deps): bump symfony/http-foundation from 7.2.3 to 7.3.7 (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 3 keyword(s) found
- `redis` (101 occurrences)
- `predis` (8 occurrences)
- `phpredis` (1 occurrences)
