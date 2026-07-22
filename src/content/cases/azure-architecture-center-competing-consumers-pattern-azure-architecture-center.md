---
type: guidance
title: メッセージキューで負荷を捌く：Competing Consumersパターンによる非同期処理基盤
title_original: Competing Consumers pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/competing-consumers
published_at: '2026-04-03'
---

## 概要

変動する要求量を捌くため、アプリケーションとコンシューマーサービス間にメッセージキューを挟み、複数のコンシューマーインスタンスが同じキューから非同期にメッセージを取り出して処理するCompeting Consumersパターンを解説する。キューがバッファとして機能することでスループットと可用性を高め、障害時も特定インスタンスに依存しないため信頼性が向上する。メッセージ順序、冪等性、ポイズンメッセージ検出、デッドレターキューなど実装上の考慮点も示す。
