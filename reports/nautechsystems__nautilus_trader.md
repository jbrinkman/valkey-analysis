# Valkey Integration Analysis: nautechsystems/nautilus_trader

**GitHub:** https://github.com/nautechsystems/nautilus_trader
**Analyzed:** 2026-05-02T01:40:32.824238+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis. 1 related issue(s)/PR(s) found. Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml, Cargo.toml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (6 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 14 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #3094](https://github.com/nautechsystems/nautilus_trader/issues/3094): Redis external stream consumer fails when multiple streams are configured (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (138 occurrences)
