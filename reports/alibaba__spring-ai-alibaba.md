# Valkey Integration Analysis: alibaba/spring-ai-alibaba

**GitHub:** https://github.com/alibaba/spring-ai-alibaba
**Analyzed:** 2026-05-02T01:40:32.708965+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 3 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pom.xml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 1 file(s)
  - [spring-ai-alibaba-graph-core/src/test/java/com/alibaba/cloud/ai/graph/checkpoint/savers/RedisSaverTest.java](https://github.com/alibaba/spring-ai-alibaba/blob/67e5b58caa545a704469e3680df3a30caa8b111a/spring-ai-alibaba-graph-core/src/test/java/com/alibaba/cloud/ai/graph/checkpoint/savers/RedisSaverTest.java)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 38 file(s)
- `redisjson` / `rejson`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (500 total org repos):**
- [community](https://github.com/alibaba/community): The community common description for Alibaba
- [CNStackCommunityEdition](https://github.com/alibaba/CNStackCommunityEdition): CNStack Community Edition
- [lowcode-plugins](https://github.com/alibaba/lowcode-plugins): An enterprise-class low-code technology stack with scale-out design / 一套面向扩展设计的企业级低代码技术体系

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (35 occurrences)
