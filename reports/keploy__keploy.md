# Valkey Integration Analysis: keploy/keploy

**GitHub:** https://github.com/keploy/keploy
**Analyzed:** 2026-05-02T01:40:32.792476+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. 2 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: go.mod

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (2 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 5 file(s)
- `redisjson` / `rejson`: 3 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (58 total org repos):**
- [community-blog](https://github.com/keploy/community-blog): None
- [keploy-integrations-shared](https://github.com/keploy/keploy-integrations-shared): None

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (207 occurrences)
