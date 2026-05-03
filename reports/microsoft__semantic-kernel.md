# Valkey Integration Analysis: microsoft/semantic-kernel

**GitHub:** https://github.com/microsoft/semantic-kernel
**Analyzed:** 2026-05-02T01:40:32.816533+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | True |

## Summary

No Valkey or Redis integration detected. 1 related issue(s)/PR(s) found. 5 related extension repo(s) found (0 mention Valkey). Redis modules used: redisai, redisearch, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series, vector_store
- **Integration Type:** extension
- **Redis Modules:** redisai, redisearch, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redisearch` / `ft.search`: 4 file(s)
- `redistimeseries` / `ts.add`: 64 file(s)
- `redisai` / `redisai`: 1 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #13905](https://github.com/microsoft/semantic-kernel/pull/13905): Python: Fix Redis connector bugs — JSON delete prefix, vector search, FT.CREATE PREFIX (open)

## Phase 5: Ecosystem

**Related repos in org (500 total org repos):**
- [opencv_contrib](https://github.com/microsoft/opencv_contrib): Repository for OpenCV's extra modules
- [DACExtensions](https://github.com/microsoft/DACExtensions): DACExtensions contains samples that extend Data-Tier Applications using DacFx. These samples include deployment contributors and static code analysis rules that can be used with Visual Studio as well as examples of how to use the DacFx public mode
- [tslint-microsoft-contrib](https://github.com/microsoft/tslint-microsoft-contrib): A set of TSLint rules used on some Microsoft projects.
- [unityplugins](https://github.com/microsoft/unityplugins): Unity Plugins for Windows Store and Azure related functions.
- [hiredis](https://github.com/microsoft/hiredis): Minimalistic C client for Redis >= 1.2 🔴 Redis

## DeepWiki Analysis

**Redis mentions:** 3 keyword(s) found
- `redis` (39 occurrences)
- `stackexchange.redis` (2 occurrences)
- `hiredis` (2 occurrences)
