# Valkey Integration Analysis: meshery/meshery

**GitHub:** https://github.com/meshery/meshery
**Analyzed:** 2026-05-02T01:40:32.809137+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | True |

## Summary

Explicit Valkey support detected. Redis modules used: redisearch, redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series, vector_store
- **Integration Type:** none
- **Redis Modules:** redisearch, redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 87 file(s)
  - [server/meshmodel/aws-elasticache-controller/v1.0.7/v1.0.0/components/ReplicationGroup.json](https://github.com/meshery/meshery/blob/512b269810281fa0eb0d111151b7ddb9f8cbc4fd/server/meshmodel/aws-elasticache-controller/v1.0.7/v1.0.0/components/ReplicationGroup.json)
  - [server/meshmodel/kubedb/2025.10.17/v1.0.0/components/RedisVersion.json](https://github.com/meshery/meshery/blob/512b269810281fa0eb0d111151b7ddb9f8cbc4fd/server/meshmodel/kubedb/2025.10.17/v1.0.0/components/RedisVersion.json)
  - [server/meshmodel/aws-elasticache-controller/v1.3.3/v1.0.0/components/User.json](https://github.com/meshery/meshery/blob/512b269810281fa0eb0d111151b7ddb9f8cbc4fd/server/meshmodel/aws-elasticache-controller/v1.3.3/v1.0.0/components/User.json)

**Redis module code references:**
- `redisearch` / `ft.search`: 2 file(s)
- `redistimeseries` / `ts.add`: 1 file(s)
- `redisjson` / `rejson`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

No related extension repos found in the org.

## DeepWiki Analysis

No Valkey or Redis mentions found in DeepWiki content.
