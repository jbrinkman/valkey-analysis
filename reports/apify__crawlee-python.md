# Valkey Integration Analysis: apify/crawlee-python

**GitHub:** https://github.com/apify/crawlee-python
**Analyzed:** 2026-05-04T02:04:36.318736+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | False |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. Redis dependencies: redis. 1 related issue(s)/PR(s) found (1 positive). 8 related extension repo(s) found (0 mention Valkey). Redis modules used: redistimeseries.

## Integration Details

- **Client Libraries:** redis
- **Use Cases:** time_series
- **Integration Type:** native
- **Redis Modules:** redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml

**Redis dependencies:**
- `redis` (redis-client)

## Phase 2: Documentation Scan

## Phase 3: Code Search

## Phase 4: Community Signals

**Issues/PRs:**
- ✅ [PR #1406](https://github.com/apify/crawlee-python/pull/1406): feat:  Add `RedisStorageClient` based on Redis v8.0+ (closed)

## Phase 5: Ecosystem

**Related repos in org (217 total org repos):**
- [actor-vector-database-integrations](https://github.com/apify/actor-vector-database-integrations): Transfer data from Apify Actors to vector databases (Chroma, Milvus, Pinecone, PostgreSQL (PG-Vector), Qdrant, and Weaviate)
- [make-integrations-scraper](https://github.com/apify/make-integrations-scraper): Scrape list of available integrations from Make
- [zapier-integrations-scraper](https://github.com/apify/zapier-integrations-scraper): Scrape list of Zapier integrations from Zapier website
- [extensions](https://github.com/apify/extensions): Everything you need to extend Raycast.
- [haystack-integrations](https://github.com/apify/haystack-integrations): 🚀 A list of Haystack Integrations, maintained by the community or deepset. 
- [Integrations-input-test-Actor](https://github.com/apify/Integrations-input-test-Actor): None
- [cursor-plugins](https://github.com/apify/cursor-plugins): Apify Cursor plugins for web scraping, data extraction, and Actor development
- [dify-plugins](https://github.com/apify/dify-plugins): All Dify Plugins listed in Dify Marketplace, plus illustrated plugin examples.

## DeepWiki Analysis

**Redis mentions:** 2 keyword(s) found
- `redis` (92 occurrences)
- `hiredis` (2 occurrences)

**Redis module mentions:** ['redistimeseries']
