# Valkey Integration Analysis: grafana/loki

**GitHub:** https://github.com/grafana/loki
**Analyzed:** 2026-05-02T01:40:32.773655+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 7 related issue(s)/PR(s) found. 10 related extension repo(s) found (0 mention Valkey). Redis modules used: redisbloom, redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** github.com/redis/go-redis, redis
- **Use Cases:** time_series
- **Integration Type:** extension
- **Redis Modules:** redisbloom, redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: go.mod

**Redis dependencies:**
- `redis` (redis-client)
- `github.com/redis/go-redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 43 file(s)
- `redisjson` / `rejson`: 14 file(s)
- `redisbloom` / `bf.add`: 2 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #18063](https://github.com/grafana/loki/issues/18063): helm chart: accept redis password as an existing secret or env var (closed)
- [ISSUE #19923](https://github.com/grafana/loki/issues/19923): `3.6.0` loki failing health checks with 404 error (open)
- [PR #20739](https://github.com/grafana/loki/pull/20739): chore(deps): update terraform aws to ~> 6.31.0 (main) (closed)
- [PR #17310](https://github.com/grafana/loki/pull/17310): chore(deps): update terraform aws to ~> 5.95.0 (main) (closed)
- [PR #15689](https://github.com/grafana/loki/pull/15689): chore(deps): update terraform aws to ~> 5.83.0 (closed)
- [PR #15517](https://github.com/grafana/loki/pull/15517): chore(deps): update terraform aws to ~> 5.82.0 (closed)
- [PR #14717](https://github.com/grafana/loki/pull/14717): chore(deps): update terraform aws to ~> 5.74.0 (closed)

## Phase 5: Ecosystem

**Related repos in org (500 total org repos):**
- [k6-integrations-extras](https://github.com/grafana/k6-integrations-extras): Community developed integrations and plugins for the Datadog Agent.
- [redis_exporter](https://github.com/grafana/redis_exporter): Prometheus Exporter for Redis Metrics. Supports Redis 2.x, 3.x, 4.x, 5.x and 6.x 🔴 Redis
- [xk6-redis](https://github.com/grafana/xk6-redis): A k6 extension to test the performance of a Redis instance 🔴 Redis
- [orbit_integrations_k6](https://github.com/grafana/orbit_integrations_k6): None
- [aioredis-py](https://github.com/grafana/aioredis-py): asyncio (PEP 3156) Redis support 🔴 Redis
- [redislite](https://github.com/grafana/redislite): Redis in a python module. 🔴 Redis
- [community](https://github.com/grafana/community): None
- [grafana-community-support-squad](https://github.com/grafana/grafana-community-support-squad): Public repository for the Grafana community support squad
- [opentelemetry-python-contrib](https://github.com/grafana/opentelemetry-python-contrib): OpenTelemetry instrumentation for Python modules
- [apiextensions-apiserver](https://github.com/grafana/apiextensions-apiserver): API server for API extensions like CustomResourceDefinitions

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (11 occurrences)

**Redis module mentions:** ['redistimeseries']
