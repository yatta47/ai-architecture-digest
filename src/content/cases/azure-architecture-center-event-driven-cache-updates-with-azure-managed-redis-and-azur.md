---
type: guidance
title: Cosmos DB変更フィードでRedisを更新するイベント駆動キャッシュ
title_original: Event-driven cache updates with Azure Managed Redis and Azure Cosmos DB
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/architecture/event-driven-cache-updates-azure-managed-redis-cosmos-db
published_at: '2026-10-03'
---

## 概要

Cosmos DBを正本として、Azure Functionsが変更フィードを読みAzure Managed Redisの値を更新（または版付き墓標を書き込み）するアーキテクチャ。書き込みを妨げず、短い遅延を許容できる場面向けで、即時反映が必要ならライトスルーを推奨する。
