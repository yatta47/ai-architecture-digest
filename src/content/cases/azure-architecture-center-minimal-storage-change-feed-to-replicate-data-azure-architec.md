---
type: guidance
title: Cosmos DB変更フィードで低コストストレージへデータ複製する高可用Webアプリ構成
title_original: Minimal storage – Change feed to replicate data
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/idea/minimal-storage-change-feed-replicate-data
published_at: '2026-06-04'
---

## 概要

大量データを一定期間だけ高速にアクセス可能にしたいWebアプリケーション向けに、Azure Cosmos DBをプライマリストアとして使い、変更フィードでAzure Table Storageへデータを複製し、期限切れデータはAzure Functionsで削除するリファレンスアーキテクチャ。複数リージョンへのジオレプリケーションとAzure Front Doorによるフェイルオーバーで高可用性を確保しつつ、監査・分析用データは低コストのTable Storageに長期保持する構成になっている。
