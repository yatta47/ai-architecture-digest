---
type: guidance
title: 分散システムにおけるサーキットブレーカーパターン
title_original: Circuit Breaker pattern
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker
published_at: '2025-03-21'
---

## 概要

分散環境でリモートサービス呼び出しが失敗し続ける際に、無駄なリトライを避けて障害を検知・遮断するサーキットブレーカーパターンを解説する。Closed/Open/Half-Openの3状態を持つプロキシとして実装し、システムの安定性とレジリエンスを高める設計を紹介する。
