# Valkey Integration Analysis: elastic/beats

**GitHub:** https://github.com/elastic/beats
**Analyzed:** 2026-05-02T01:40:32.750504+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 2 related issue(s)/PR(s) found. 9 related extension repo(s) found (0 mention Valkey). Redis modules used: redisbloom, redistimeseries.

## Integration Details

- **Client Libraries:** github.com/gomodule/redigo, redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redisbloom, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: go.mod

**Redis dependencies:**
- `redis` (redis-client)
- `github.com/gomodule/redigo` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 44 file(s)
- `redisbloom` / `bf.add`: 9 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [PR #47022](https://github.com/elastic/beats/pull/47022): build(deps): bump github.com/gomodule/redigo from 1.9.2 to 1.9.3 (closed)
- [PR #41507](https://github.com/elastic/beats/pull/41507): [feat:filebeat/input/redis/slowlog] Add client address and name to submitted slowlogs (closed)

## Phase 5: Ecosystem

**Related repos in org (500 total org repos):**
- [logstash-contrib](https://github.com/elastic/logstash-contrib): THIS REPOSITORY IS NO LONGER USED.
- [elasticsearch-plugins-script](https://github.com/elastic/elasticsearch-plugins-script): Contain utility scripts for releasing elasticsearch official plugins
- [apm-contrib](https://github.com/elastic/apm-contrib): Contrib repository for Elastic APM
- [Elastic-Contributor-Program](https://github.com/elastic/Elastic-Contributor-Program): None
- [uptime-contrib](https://github.com/elastic/uptime-contrib): Contrib repository for Elastic Uptime
- [integrations](https://github.com/elastic/integrations): None
- [go-plugins-helpers](https://github.com/elastic/go-plugins-helpers): Go helper packages to extend the Docker Engine
- [observability-contrib](https://github.com/elastic/observability-contrib): Contrib repository for Elastic Observability
- [harp-plugins](https://github.com/elastic/harp-plugins): Harp Plugins - It uses Harp SDK to provide new features to your secret management pipelines.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (101 occurrences)

**Redis module mentions:** ['redistimeseries']
