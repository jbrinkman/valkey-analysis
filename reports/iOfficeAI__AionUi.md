# Valkey Integration Analysis: iOfficeAI/AionUi

**GitHub:** https://github.com/iOfficeAI/AionUi
**Analyzed:** 2026-05-02T01:40:32.781164+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 8 file(s)
  - [src/common/chat/approval/index.ts](https://github.com/iOfficeAI/AionUi/blob/d67f4b29f17f28c1f6224c6b23ba6721b70f0f7a/src/common/chat/approval/index.ts)
  - [src/process/agent/acp/ApprovalStore.ts](https://github.com/iOfficeAI/AionUi/blob/d67f4b29f17f28c1f6224c6b23ba6721b70f0f7a/src/process/agent/acp/ApprovalStore.ts)
  - [src/process/agent/gemini/GeminiApprovalStore.ts](https://github.com/iOfficeAI/AionUi/blob/d67f4b29f17f28c1f6224c6b23ba6721b70f0f7a/src/process/agent/gemini/GeminiApprovalStore.ts)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 6 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Valkey mentions:**
- `valkey` (1 occurrences)
  - `Sources:        package.json  1-150         scripts/build-with-builder.js  1-30         electron-builder.yml  1-104                   Dismiss   Refresh this wiki  Enter email to refresh    On this pag`
