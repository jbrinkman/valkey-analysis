# Valkey Integration Analysis: coze-dev/coze-studio

**GitHub:** https://github.com/coze-dev/coze-studio
**Analyzed:** 2026-05-02T01:40:32.738247+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 1 file(s)
  - [frontend/packages/agent-ide/bot-plugin/tools/src/components/plugin_modal/utils.ts](https://github.com/coze-dev/coze-studio/blob/22275b1c2661d35344a7493cffe401e8cc61cf8e/frontend/packages/agent-ide/bot-plugin/tools/src/components/plugin_modal/utils.ts)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 6 file(s)
- `redisjson` / `rejson`: 3 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (59 occurrences)
- `go-redis` (1 occurrences)
