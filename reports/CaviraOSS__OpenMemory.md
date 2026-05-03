# Valkey Integration Analysis: CaviraOSS/OpenMemory

**GitHub:** https://github.com/CaviraOSS/OpenMemory
**Analyzed:** 2026-05-02T01:40:32.489806+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | True |

## Summary

Explicit Valkey support detected. 3 related issue(s)/PR(s) found. 1 related discussion(s) found. Redis modules used: redisearch, redisgraph, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series, vector_store
- **Integration Type:** none
- **Redis Modules:** redisearch, redisgraph, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 9 file(s)
  - [packages/openmemory-js/src/core/vector/valkey.ts](https://github.com/CaviraOSS/OpenMemory/blob/6ab6221a5417784f08e10c0b47f805692d1c95a9/packages/openmemory-js/src/core/vector/valkey.ts)
  - [packages/openmemory-py/src/openmemory/core/vector/valkey.py](https://github.com/CaviraOSS/OpenMemory/blob/6ab6221a5417784f08e10c0b47f805692d1c95a9/packages/openmemory-py/src/openmemory/core/vector/valkey.py)
  - [packages/openmemory-js/src/core/cfg.ts](https://github.com/CaviraOSS/OpenMemory/blob/6ab6221a5417784f08e10c0b47f805692d1c95a9/packages/openmemory-js/src/core/cfg.ts)

**Redis module code references:**
- `redisearch` / `ft.search`: 1 file(s)
- `redistimeseries` / `ts.add`: 3 file(s)
- `redisgraph` / `graph.query`: 1 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #141](https://github.com/CaviraOSS/OpenMemory/issues/141): [Performance] Refactor HSG waypoint creation to use vector store ANN search. (open)
- [ISSUE #65](https://github.com/CaviraOSS/OpenMemory/issues/65): [FEATURE] Discussion: Add Valkey as an Optional Vector Backend (via Pluggable VectorStore Interface) (closed)
- [PR #75](https://github.com/CaviraOSS/OpenMemory/pull/75): PostgreSQL compatibility and vector table configuration (closed)

**Discussions:**
- [Discussion #87](https://github.com/CaviraOSS/OpenMemory/discussions/87): v1.2.2

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Valkey mentions:**
- `valkey` (140 occurrences)
  - `Aspect  Description       Architecture   Hierarchical Memory Decomposition (HMD v2) with multi-sector storage       ARCHITECTURE.md  5       Deployment   Local-first (embedded SQLite) or server mode (`
  - `Sources:        README.md  42-58                   Dismiss   Refresh this wiki  Enter email to refresh    On this page    Overview    Purpose and Scope    What is OpenMemory?    Key Characteristics   `

**Redis mentions:** 1 keyword(s) found
- `redis` (19 occurrences)

**Redis module mentions:** ['redisearch']
