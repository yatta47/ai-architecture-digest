---
type: guidance
title: AKSによる大規模バッチトランザクション処理基盤
title_original: High-volume batch transaction processing
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/process-batch-transactions
published_at: '2026-06-03'
---

## 概要

IBMメインフレームのMQベースのバッチ処理をAzureに移行する構成として、Service Busのキュー/トピックからAKSクラスタがメッセージを受け取り並列処理するアーキテクチャを解説する。Azure Managed RedisやCosmos DBを一時ストレージに、SQL Managed Instanceを永続層に用い、GRSによる災害対策で高可用な大量トランザクション処理を実現する設計を示す。
