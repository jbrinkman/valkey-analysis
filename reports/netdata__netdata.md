# Valkey Integration Analysis: netdata/netdata

**GitHub:** https://github.com/netdata/netdata
**Analyzed:** 2026-05-02T01:40:32.825486+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 1 related issue(s)/PR(s) found. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redisgraph, redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redisgraph, redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (4 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 39 file(s)
- `redisjson` / `rejson`: 1 file(s)
- `redisgraph` / `graph.query`: 3 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #17639](https://github.com/netdata/netdata/pull/17639): Add valkey to apps_groups.conf (closed)

## Phase 5: Ecosystem

**Related repos in org (75 total org repos):**
- [community](https://github.com/netdata/community): Netdata-powered applications and examples. For the community, by the community.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (22 occurrences)
