# Valkey Integration Analysis: 1Panel-dev/1Panel

**GitHub:** https://github.com/1Panel-dev/1Panel
**Analyzed:** 2026-05-02T01:40:32.397135+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. 3 related issue(s)/PR(s) found. 1 related discussion(s) found. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 2 file(s)
- `redisjson` / `rejson`: 1 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #12451](https://github.com/1Panel-dev/1Panel/issues/12451): [Feature] Hope App Store can add Dragonfly (closed)
- [ISSUE #8577](https://github.com/1Panel-dev/1Panel/issues/8577): Please add Valkey to the app store (closed)
- [ISSUE #12439](https://github.com/1Panel-dev/1Panel/issues/12439): [Feature] Database Redis connection: add support for Valkey (open)

**Discussions:**
- [Discussion #8575](https://github.com/1Panel-dev/1Panel/discussions/8575): 希望应用商店能上架valkey

## Phase 5: Ecosystem

**Related repos in org (30 total org repos):**
- [1Panel-appstore-skills](https://github.com/1Panel-dev/1Panel-appstore-skills): 1Panel App Store app package generator

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (144 occurrences)
