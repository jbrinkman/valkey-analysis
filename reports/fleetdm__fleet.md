# Valkey Integration Analysis: fleetdm/fleet

**GitHub:** https://github.com/fleetdm/fleet
**Analyzed:** 2026-05-02T01:40:32.760255+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 7 related issue(s)/PR(s) found. Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** github.com/gomodule/redigo, redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: package.json, go.mod

**Redis dependencies:**
- `redis` (redis-client)
- `github.com/gomodule/redigo` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 2 file(s)
  - [docs/Get started/FAQ.md](https://github.com/fleetdm/fleet/blob/fab3af38ea947d7fc203b18b2ac763c6f8f36ae9/docs/Get%20started/FAQ.md)
  - [tools/redis-tests/elasticache/cf-template.yaml](https://github.com/fleetdm/fleet/blob/fab3af38ea947d7fc203b18b2ac763c6f8f36ae9/tools/redis-tests/elasticache/cf-template.yaml)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 19 file(s)
- `redisjson` / `rejson`: 1 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #42669](https://github.com/fleetdm/fleet/issues/42669): Support Redis 8.x (open)
- [ISSUE #32122](https://github.com/fleetdm/fleet/issues/32122): Add Go test coverage for Redis 6, 7, and 8 (closed)
- [PR #42442](https://github.com/fleetdm/fleet/pull/42442): adding redis and mysql subcharts instead of bitnami (open)
- [PR #42740](https://github.com/fleetdm/fleet/pull/42740): [DO NOT MERGE] Test with Valkey 7 (closed)
- [PR #42739](https://github.com/fleetdm/fleet/pull/42739): [DO NOT MERGE] Test with Valkey 8 (closed)
- [PR #33928](https://github.com/fleetdm/fleet/pull/33928): Fix lingering live queries keys in Redis (closed)
- [PR #31075](https://github.com/fleetdm/fleet/pull/31075): Add AWS IAM auth for RDS MySQL/MariaDB and ElastiCache Redis/Valkey (closed)

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (132 occurrences)
