# Valkey Integration Analysis: metersphere/metersphere

**GitHub:** https://github.com/metersphere/metersphere
**Analyzed:** 2026-05-02T01:40:32.810229+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis. 2 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pom.xml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (2 occurrences)

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 41 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (22 total org repos):**
- [chrome-extensions](https://github.com/metersphere/chrome-extensions): MeterSphere 录制浏览器请求的插件，记录浏览器中的网络请求并导出为 JMeter 或 JSON 格式的文件
- [jmeter-plugins](https://github.com/metersphere/jmeter-plugins): JMeter 插件集

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (169 occurrences)
