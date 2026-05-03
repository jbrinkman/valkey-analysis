# Valkey Integration Analysis: Azure-Samples/azure-search-openai-demo

**GitHub:** https://github.com/Azure-Samples/azure-search-openai-demo
**Analyzed:** 2026-05-02T01:40:32.442845+00:00

## Classification

| Field | Value |
|-------|-------|
| Valkey Support | **none** |
| Valkey-Search Support | **none** |
| Valkey-Glide Used | False |
| RediSearch Usage | True |

## Summary

Redis integration detected but uses Valkey-incompatible module(s): redistimeseries. 9 related extension repo(s) found (0 mention Valkey). Redis modules used: redisearch, redisjson, redistimeseries.

## Integration Details

- **Client Libraries:** None detected
- **Use Cases:** time_series, vector_store
- **Integration Type:** extension
- **Redis Modules:** redisearch, redisjson, redistimeseries

## Phase 1: Dependency Scan

Manifests checked: pyproject.toml

## Phase 2: Documentation Scan

## Phase 3: Code Search

**Redis module code references:**
- `redisearch` / `ft.search`: 5 file(s)
- `redistimeseries` / `ts.add`: 1 file(s)

## Phase 4: Community Signals

## Phase 5: Ecosystem

**Related repos in org (500 total org repos):**
- [active-directory-php-graphapi-directoryextensions-web](https://github.com/Azure-Samples/active-directory-php-graphapi-directoryextensions-web): A PHP web application that calls the Graph API to register new directory extensions and manipulate the extension properties 
- [active-directory-dotnet-graphapi-directoryextensions-web](https://github.com/Azure-Samples/active-directory-dotnet-graphapi-directoryextensions-web): An .NET 4.5 web app that uses the Azure AD Graph API to add custom properties using directory extensions.
- [redis-cache-getting-started](https://github.com/Azure-Samples/redis-cache-getting-started): Basic operation with Redis Cache 🔴 Redis
- [compute-java-manage-virtual-machine-using-vm-extensions](https://github.com/Azure-Samples/compute-java-manage-virtual-machine-using-vm-extensions): Getting started on managing virtual machines using vm extensions using Java
- [redis-cache-dotnet-manage-cache](https://github.com/Azure-Samples/redis-cache-dotnet-manage-cache): Getting started on managing Redis Cache in C# 🔴 Redis
- [compute-dotnet-manage-virtual-machine-using-vm-extensions](https://github.com/Azure-Samples/compute-dotnet-manage-virtual-machine-using-vm-extensions): Getting started on managing virtual machines using vm extensions in C#
- [redis-java-manage-cache](https://github.com/Azure-Samples/redis-java-manage-cache): Getting started on managing Redis Cache using Java 🔴 Redis
- [redis-cache-cli-export-to-storage](https://github.com/Azure-Samples/redis-cache-cli-export-to-storage): This sample demonstrates how to use Azure CLI to export Azure Redis Cache data to Azure Storage as backup 🔴 Redis
- [redis-cache-dotnet-export-simulate-portal](https://github.com/Azure-Samples/redis-cache-dotnet-export-simulate-portal): This sample demonstrates how to use Azure Portal endpoint to export Azure Redis Cache data to Azure Storage as backup 🔴 Redis

## DeepWiki Analysis

**Redis mentions:** 1 keyword(s) found
- `redis` (1 occurrences)

**Redis module mentions:** ['redisjson']
