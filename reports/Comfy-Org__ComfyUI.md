# Valkey Integration Analysis: Comfy-Org/ComfyUI

**GitHub:** https://github.com/Comfy-Org/ComfyUI
**Analyzed:** 2026-05-02T01:40:32.502847+00:00

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

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: requirements.txt, pyproject.toml

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 1 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #1469](https://github.com/Comfy-Org/ComfyUI/pull/1469): Dockerfile and automatic generation of images via GitHub Actions (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (2 occurrences)
