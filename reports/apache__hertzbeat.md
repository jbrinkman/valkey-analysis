# Valkey Integration Analysis: apache/hertzbeat

**GitHub:** https://github.com/apache/hertzbeat
**Analyzed:** 2026-05-02T01:40:32.713766+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **explicit** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Explicit Valkey support detected. 4 related issue(s)/PR(s) found. 5 related extension repo(s) found (0 mention Valkey). Redis modules used: redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series
- **Integration Type:** extension
- **Redis Modules:** redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pom.xml

## Phase 2: Documentation Scan

**Redis mentions in README:**
- `redis` (6 occurrences)

## Phase 3: Code Search

**Valkey code references:**
- `valkey`: 15 file(s)
  - [home/docs/help/valkey.md](https://github.com/apache/hertzbeat/blob/42eec4d559aa450d809a3b407c2b1bc4e3955730/home/docs/help/valkey.md)
  - [hertzbeat-manager/src/main/resources/define/app-valkey.yml](https://github.com/apache/hertzbeat/blob/42eec4d559aa450d809a3b407c2b1bc4e3955730/hertzbeat-manager/src/main/resources/define/app-valkey.yml)
  - [home/i18n/zh-cn/docusaurus-plugin-content-docs/current/help/valkey.md](https://github.com/apache/hertzbeat/blob/42eec4d559aa450d809a3b407c2b1bc4e3955730/home/i18n/zh-cn/docusaurus-plugin-content-docs/current/help/valkey.md)

**Redis module code references:**
- `redistimeseries` / `ts.add`: 35 file(s)
- `redisjson` / `rejson`: 1 file(s)

## Phase 4: Community Signals

**Issues/PRs:**
- [ISSUE #3591](https://github.com/apache/hertzbeat/issues/3591): [Task] Monitoring Template Yml Metrics Japanese I18n (closed)
- [PR #3706](https://github.com/apache/hertzbeat/pull/3706): [doc] add japanese i18n in app-valkey.yml (closed)
- [PR #2633](https://github.com/apache/hertzbeat/pull/2633): [Improve] add valkey help md (closed)
- [PR #2547](https://github.com/apache/hertzbeat/pull/2547): [type:feature] add valkey template (closed)

## Phase 5: Ecosystem

**Related repos in org (500 total org repos):**
- [maven-plugins](https://github.com/apache/maven-plugins): [deprecated] Mirror of Apache Maven plugins
- [servicemix-maven-plugins](https://github.com/apache/servicemix-maven-plugins): Mirror of Apache Servicemix Maven plug-ins
- [grails-redis](https://github.com/apache/grails-redis): Base redis plugin for Grails 🔴 Redis
- [cordova-plugins](https://github.com/apache/cordova-plugins): Apache Cordova
- [couchdb-couch-plugins](https://github.com/apache/couchdb-couch-plugins): Mirror of Apache CouchDB

## DeepWiki Analysis

**Valkey mentions:**
- `valkey` (3 occurrences)
  - `Dismiss   Refresh this wiki  Enter email to refresh    On this page    Overview    What is HertzBeat?    High-Level Architecture    Maven Project Structure    Key Modules    Technology Stack    Core D`

**Redis mentions:** 4 keyword(s) found
- `redis` (201 occurrences)
- `jedis` (1 occurrences)
- `lettuce` (3 occurrences)
- `predis` (1 occurrences)
