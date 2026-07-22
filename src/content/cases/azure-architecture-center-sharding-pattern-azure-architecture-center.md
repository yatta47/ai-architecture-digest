---
type: guidance
title: データストアを水平分割するシャーディングパターン
title_original: Sharding pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/sharding
published_at: '2026-04-03'
---

## 概要

単一サーバーのデータストアはストレージ容量・計算資源・ネットワーク帯域・地理的制約という限界に直面するため、データを同一スキーマを持つ複数の水平パーティション（シャード）に分割して別々のストレージノードで運用する。シャードキーの選び方（不変・高カーディナリティ・クエリパターンとの整合）が設計上最も重要な判断であり、ルックアップ方式や範囲ベース方式などの戦略でキーと物理配置を対応付ける。
