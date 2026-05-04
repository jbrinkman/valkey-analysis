# Valkey Integration Analysis: influxdata/telegraf

**GitHub:** https://github.com/influxdata/telegraf
**Analyzed:** 2026-05-04T02:04:36.987542+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis, github.com/redis/go-redis, github.com/go-redis/redis. 6 related issue(s)/PR(s) found (6 positive). 5 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** github.com/go-redis/redis, github.com/redis/go-redis, redis
- **Use Cases:** time_series
- **Integration Type:** extension
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: go.mod

**Redis dependencies:**
- `redis` (redis-client)
- `github.com/redis/go-redis` (redis-client)
- `github.com/go-redis/redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

## Phase 4: Community Signals

**Issues/PRs:**
- ✅ [PR #17983](https://github.com/influxdata/telegraf/pull/17983): chore(deps): Bump github.com/testcontainers/testcontainers-go/modules/azure from 0.39.0 to 0.40.0 (closed)
- ✅ [PR #17972](https://github.com/influxdata/telegraf/pull/17972): chore(deps): Bump github.com/testcontainers/testcontainers-go/modules/kafka from 0.39.0 to 0.40.0 (closed)
- ✅ [PR #17976](https://github.com/influxdata/telegraf/pull/17976): chore(deps): Bump github.com/testcontainers/testcontainers-go from 0.39.0 to 0.40.0 (closed)
- ✅ [PR #17382](https://github.com/influxdata/telegraf/pull/17382): chore(deps): Bump github.com/testcontainers/testcontainers-go/modules/kafka from 0.37.0 to 0.38.0 (closed)
- ✅ [PR #17387](https://github.com/influxdata/telegraf/pull/17387): chore(deps): Bump github.com/testcontainers/testcontainers-go from 0.37.0 to 0.38.0 (closed)
- ✅ [PR #17388](https://github.com/influxdata/telegraf/pull/17388): chore(deps): Bump github.com/testcontainers/testcontainers-go/modules/azure from 0.37.0 to 0.38.0 (closed)

## Phase 5: Ecosystem

**Related repos in org (221 total org repos):**
- [community](https://github.com/influxdata/community): This is a repo for all of the awesomeness happening within the InfluxDB Community
- [community-templates](https://github.com/influxdata/community-templates): InfluxDB Community Templates: Quickly collect & analyze time series data from a range of sources: Kubernetes, MySQL, Postgres, AWS, Nginx, Jenkins, and more. 🔴 Redis
- [communitysearch](https://github.com/influxdata/communitysearch): None
- [redis](https://github.com/influxdata/redis): Redis commands for Elixir 🔴 Redis
- [influxdb3_plugins](https://github.com/influxdata/influxdb3_plugins): Python plugins for InfluxDB 3

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (2 occurrences)

**Redis module mentions:** ['redistimeseries']
