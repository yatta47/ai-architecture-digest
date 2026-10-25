---
type: guidance
title: Azure Blob Storageのマルチテナント分割と分離モデル
title_original: Multitenancy and Azure Blob Storage
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/blob-storage
published_at: '2026-10-20'
---

## 概要

マルチテナントでAzure Blob Storageを使う際のパーティション設計（ホットパーティション回避）と、共有コンテナ・テナント別コンテナ・テナント別アカウントの分離モデルを解説したガイダンス。汎用ストレージ設計でAIは主題ではない。
