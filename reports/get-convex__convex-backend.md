# Valkey Integration Analysis: get-convex/convex-backend

**GitHub:** https://github.com/get-convex/convex-backend
**Analyzed:** 2026-05-02T01:40:32.762156+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: Cargo.toml

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (1 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 5 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (179 total org repos):**
- [convex-agent-plugins](https://github.com/get-convex/convex-agent-plugins): An plugin for cursor to empower it to build the best apps ever.

## DeepWiki Analysis

No Valkey or Redis mentions found in DeepWiki content.
