# Valkey Integration Analysis: remix-run/remix

**GitHub:** https://github.com/remix-run/remix
**Analyzed:** 2026-05-02T01:40:32.844062+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** session_store, time_series
- **Integration Type:** none
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (3 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 4 file(s)
- `redisjson` / `rejson`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (38 total org repos):**
- [remix-store](https://github.com/remix-run/remix-store): Remix Store - Built on Hydrogen

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (22 occurrences)
