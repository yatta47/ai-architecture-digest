---
type: guidance
title: Cosmos DBのトランザクションバッチとChange Feedで実装するTransactional Outbox
title_original: Implement the Transactional Outbox pattern by using Azure Cosmos DB
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos
published_at: '2026-02-27'
---

## 概要

マイクロサービス間でイベント配信が失敗しデータ不整合が起きる問題に対し、業務オブジェクトとイベントを同一トランザクションで保存するTransactional Outboxパターンを、Cosmos DBのトランザクションバッチとChange Feed、Service Busを組み合わせて実装する方法を解説する。
