---
type: guidance
title: Azure Managed RedisとPostgreSQLのキャッシュアサイド構成
title_original: Cache-aside caching using Azure Managed Redis and Azure Database for PostgreSQL
ai_relevant: false
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/architecture/cache-aside-azure-managed-redis-postgresql
published_at: '2026-10-05'
---

## 概要

App ServiceアプリがPostgreSQLを正本とし、Azure Managed Redisでキャッシュアサイドを実装する参照アーキテクチャ。読み取りはTTL付きでキャッシュ、書き込み時にキーを無効化する。短時間の古いデータを許容できる場合向け。
