# Valkey Integration Analysis: goharbor/harbor

**GitHub:** https://github.com/goharbor/harbor
**Analyzed:** 2026-05-02T01:40:32.766050+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 8 related issue(s)/PR(s) found. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 9 file(s)
  - [make/photon/valkey/Dockerfile](https://github.com/goharbor/harbor/blob/62c278dfb10939947a1aa0c54bea65722dfcaa78/make/photon/valkey/Dockerfile)
  - [make/photon/valkey/Dockerfile.base](https://github.com/goharbor/harbor/blob/62c278dfb10939947a1aa0c54bea65722dfcaa78/make/photon/valkey/Dockerfile.base)
  - [make/photon/valkey/docker-healthcheck](https://github.com/goharbor/harbor/blob/62c278dfb10939947a1aa0c54bea65722dfcaa78/make/photon/valkey/docker-healthcheck)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 2 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #22935](https://github.com/goharbor/harbor/issues/22935): Replace Redis with Valkey (closed)
- [ISSUE #22739](https://github.com/goharbor/harbor/issues/22739): Long running GC with S3 storage expires before finishing, takes minutes for just a few objects. Logs/traces not showing the full story? (open)
- [ISSUE #23004](https://github.com/goharbor/harbor/issues/23004): Redis 7.2 is EOL since February 28, 2026 (open)
- [ISSUE #22636](https://github.com/goharbor/harbor/issues/22636): Registry health check fails behind load-balancer with sticky session cookie (closed)
- [ISSUE #22310](https://github.com/goharbor/harbor/issues/22310): Jobservice pod uses default user instead of username defined in URL for redis connection (closed)
- [ISSUE #21985](https://github.com/goharbor/harbor/issues/21985): Endpoint with auth registry get unhealthy without any reason after 5-24h (closed)
- [ISSUE #20822](https://github.com/goharbor/harbor/issues/20822): ODIC + CLI Secret mismatch (open)
- [PR #23157](https://github.com/goharbor/harbor/pull/23157): feat: replace redis with valkey as cache backend (closed)

## Phase 5: Ecosystem

**Related repos in org (28 total org repos):**
- [community](https://github.com/goharbor/community): Harbor community-related material

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (135 occurrences)
