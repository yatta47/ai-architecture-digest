---
type: guidance
title: マルチテナントシステムにおけるAzure Cosmos DBの分離モデル設計
title_original: Multitenancy and Azure Cosmos DB
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/cosmos-db
published_at: '2026-04-29'
---

## 概要

マルチテナントAzure Cosmos DB設計における「テナントあたりパーティションキー」モデル(B2C向け、低コストだが論理分離のみ)と「テナントあたりデータベースアカウント」モデル(B2B向け、性能保証とカスタマー管理キーが可能)のトレードオフを解説。バーストキャパシティや優先度ベース実行、階層パーティションキーなど、ノイジーネイバー問題を緩和する機能も紹介する。
