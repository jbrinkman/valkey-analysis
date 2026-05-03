# Valkey Integration Analysis: microsoft/autogen

**GitHub:** https://github.com/microsoft/autogen
**Analyzed:** 2026-05-02T01:40:32.814272+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. 5 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** extension
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 11 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (500 total org repos):**
- [opencv_contrib](https://github.com/microsoft/opencv_contrib): Repository for OpenCV's extra modules
- [DACExtensions](https://github.com/microsoft/DACExtensions): DACExtensions contains samples that extend Data-Tier Applications using DacFx. These samples include deployment contributors and static code analysis rules that can be used with Visual Studio as well as examples of how to use the DacFx public mode
- [tslint-microsoft-contrib](https://github.com/microsoft/tslint-microsoft-contrib): A set of TSLint rules used on some Microsoft projects.
- [unityplugins](https://github.com/microsoft/unityplugins): Unity Plugins for Windows Store and Azure related functions.
- [hiredis](https://github.com/microsoft/hiredis): Minimalistic C client for Redis >= 1.2 🔴 Redis

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (36 occurrences)
