# Valkey Integration Analysis: StarRocks/starrocks

**GitHub:** https://github.com/StarRocks/starrocks
**Analyzed:** 2026-05-02T01:40:32.692028+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 2 related extension repo(s) found (0 mention Valkey). Redis modules used: redisbloom, redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redisbloom, redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 1 file(s)
  - [fe/fe-core/src/test/java/com/starrocks/http/rest/v2/TableSchemaActionTest.java](https://github.com/StarRocks/starrocks/blob/2bb40627a036cfe26f2cb8305d2eb27d57026113/fe/fe-core/src/test/java/com/starrocks/http/rest/v2/TableSchemaActionTest.java)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 317 file(s)
- `redisjson` / `rejson`: 1 file(s)
- `redisbloom` / `bf.add`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (51 total org repos):**
- [community](https://github.com/StarRocks/community): Welcome to the StarRocks community! 
- [fe-plugins-auditloader](https://github.com/StarRocks/fe-plugins-auditloader): AuditLoader plugin for FE

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (1 occurrences)
