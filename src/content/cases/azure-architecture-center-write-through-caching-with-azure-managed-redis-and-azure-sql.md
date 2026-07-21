---
type: guidance
title: Azure Managed RedisとAzure SQLによるライトスルーキャッシュ構成
title_original: Write-through caching with Azure Managed Redis and Azure SQL Database
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/architecture/write-through-caching-azure-sql-managed-redis
published_at: '2026-07-02'
---

## 概要

Azure Architecture Centerのリファレンスアーキテクチャは、高トラフィックWebアプリケーションにおいてAzure SQL Databaseを正データ（system of record）、Azure Managed Redisを派生キャッシュとするアプリケーション管理型のライトスルーキャッシュ構成を解説する。Azure Functionsが書き込みコーディネーターとしてSQLへのコミットとRedisへの反映を仲介し、SQL側のoutboxテーブルと修復用Functionによって、Redis更新が失敗した場合でも整合性を回復できる設計になっている。
