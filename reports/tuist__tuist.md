# Valkey Integration Analysis: tuist/tuist

**GitHub:** https://github.com/tuist/tuist
**Analyzed:** 2026-05-02T01:40:32.872254+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 1 related issue(s)/PR(s) found. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** extension
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 3 file(s)
  - [infra/helm/tuist/values.yaml](https://github.com/tuist/tuist/blob/47d72d91c9bcfe5d48431a7d0937c632cf7cc9e0/infra/helm/tuist/values.yaml)
  - [infra/helm/tuist/values-managed-canary.yaml](https://github.com/tuist/tuist/blob/47d72d91c9bcfe5d48431a7d0937c632cf7cc9e0/infra/helm/tuist/values-managed-canary.yaml)
  - [infra/helm/tuist/values-managed-production.yaml](https://github.com/tuist/tuist/blob/47d72d91c9bcfe5d48431a7d0937c632cf7cc9e0/infra/helm/tuist/values-managed-production.yaml)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 23 file(s)
- `redisjson` / `rejson`: 4 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #10464](https://github.com/tuist/tuist/pull/10464): fix(server): wire in-cluster Valkey for canary/production rate limiter (closed)

## Phase 5: Ecosystem

**Related repos in org (170 total org repos):**
- [asdf-plugins](https://github.com/tuist/asdf-plugins): Convenience shortname repository for asdf community plugins 🔴 Redis

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (46 occurrences)
