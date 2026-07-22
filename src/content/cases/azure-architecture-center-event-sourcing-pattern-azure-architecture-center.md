---
type: guidance
title: 変更履歴をイベントとして記録するイベントソーシングパターン
title_original: Event Sourcing pattern
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/event-sourcing
published_at: '2026-03-28'
---

## 概要

Event Sourcingパターンは、データの最新状態のみを保存する従来のCRUD方式とは異なり、エンティティに対するすべての操作をイベントとして追記専用ストアに記録し、それを唯一の正とするデータ管理手法である。現在の状態が必要な場合はイベント列を再生（リハイドレーション）して復元するか、クエリ用に最適化されたマテリアライズドビューを別途保持する。書き込み競合の回避や監査性の向上といった利点がある一方、データストア設計・並行処理・スキーマ変更・クエリ方式が大きく変わるため、採用と移行のコストが高い複雑なパターンである。
