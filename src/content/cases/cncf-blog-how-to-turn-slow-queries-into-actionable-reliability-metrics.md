---
type: guidance
title: OpenTelemetryのDBスパンをアクション可能な信頼性メトリクスに変換する
title_original: How to turn slow queries into actionable reliability metrics with OpenTelemetry
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/08/21/how-to-turn-slow-queries-into-actionable-reliability-metrics-with-opentelemetry/
published_at: '2026-08-21'
---

## 概要

テレメトリを増やすだけでは理解は深まらないという問題意識から、OpenTelemetryのデータベーススパンをスパン由来メトリクスへ変換し、ダッシュボード化・アラート化する再現可能なワークフローを構築する。トラフィック加重した影響度分析と異常検知を組み合わせ、最適化すべきクエリと今まさに異常な挙動をしているクエリを見分ける。
