---
type: guidance
title: 異なるメッセージング基盤をブリッジで橋渡しする統合パターン
title_original: Messaging Bridge pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/messaging-bridge
published_at: '2026-06-03'
---

## 概要

MSMQ・RabbitMQ・Azure Service Bus・Amazon SQSなど異なるメッセージング基盤が混在する環境で、双方に接続するブリッジコンポーネントを挟んでペイロードを変更せずに中継するMessaging Bridgeパターンを解説する。HTTPベースの統合に比べ、既存システムの改修なしに少なくとも1回配信の信頼性を確保できる。
