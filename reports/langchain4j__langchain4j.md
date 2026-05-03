# Valkey Integration Analysis: langchain4j/langchain4j

**GitHub:** https://github.com/langchain4j/langchain4j
**Analyzed:** 2026-05-02T01:40:32.798145+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. 1 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** none
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pom.xml

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redistimeseries` / `ts.add`: 83 file(s)
- `redisjson` / `rejson`: 5 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (20 total org repos):**
- [langchain4j-community](https://github.com/langchain4j/langchain4j-community): LangChain4j integrations that are maintained by the community

## DeepWiki Analysis

**Redis module mentions:** ['redisjson']

No Valkey or Redis mentions found in DeepWiki content.
