---
type: guidance
title: Azure Table Storageのマルチテナント向けキー設計と分離
title_original: Multitenancy and Azure Table Storage
ai_relevant: false
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/table-storage
published_at: '2026-10-20'
---

## 概要

マルチテナントでAzure Table Storageを使う際のPartitionKey/RowKey設計と、テナント分離モデルを説明したガイダンス。クエリパターンに合わせたキー設計やインデックステーブルの考え方を扱う汎用ストレージ設計で、AIは主題ではない。
