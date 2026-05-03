# Valkey Integration Analysis: hatchet-dev/hatchet

**GitHub:** https://github.com/hatchet-dev/hatchet
**Analyzed:** 2026-05-02T01:40:32.775964+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 3 related issue(s)/PR(s) found. Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: go.mod

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (1 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 24 file(s)
- `redisjson` / `rejson`: 2 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #2503](https://github.com/hatchet-dev/hatchet/pull/2503): chore(deps): bump github.com/testcontainers/testcontainers-go/modules/rabbitmq from 0.39.0 to 0.40.0 (closed)
- [PR #2502](https://github.com/hatchet-dev/hatchet/pull/2502): chore(deps): bump github.com/testcontainers/testcontainers-go from 0.39.0 to 0.40.0 (closed)
- [PR #2501](https://github.com/hatchet-dev/hatchet/pull/2501): chore(deps): bump github.com/testcontainers/testcontainers-go/modules/postgres from 0.39.0 to 0.40.0 (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (1 occurrences)
