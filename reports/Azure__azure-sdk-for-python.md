# Valkey Integration Analysis: Azure/azure-sdk-for-python

**GitHub:** https://github.com/Azure/azure-sdk-for-python
**Analyzed:** 2026-05-02T01:40:32.454596+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | True |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. 8 related extension repo(s) found (0 mention Valkey). Redis modules used: redisearch, redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series, vector_store
- **Integration Type:** extension
- **Redis Modules:** redisearch, redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: None found

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redisearch` / `ft.search`: 18 file(s)
- `redistimeseries` / `ts.add`: 14 file(s)
- `redisjson` / `rejson`: 26 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (500 total org repos):**
- [azure-linux-extensions](https://github.com/Azure/azure-linux-extensions): Linux Virtual Machine Extensions for Azure
- [aspnet-redis-providers](https://github.com/Azure/aspnet-redis-providers): ASP.NET Redis Providers 🔴 Redis
- [azure-webjobs-sdk-extensions](https://github.com/Azure/azure-webjobs-sdk-extensions): Azure WebJobs SDK Extensions
- [azure-extensions-cli](https://github.com/Azure/azure-extensions-cli): This tool is intended only for publishers of Azure VM extensions
- [azure-python-siteextensions](https://github.com/Azure/azure-python-siteextensions): Defines the Python runtime site extensions that are available for Azure App Service
- [azure-batch-cli-extensions](https://github.com/Azure/azure-batch-cli-extensions): Batch extension cli commands for Azure cli v2
- [azure-service-bus-dotnet-plugins](https://github.com/Azure/azure-service-bus-dotnet-plugins): ☁️ Plugins for the .NET Standard client library for Azure Service Bus
- [azure-cli-extensions](https://github.com/Azure/azure-cli-extensions): Public Repository for Extensions of Azure CLI.

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (2 occurrences)
