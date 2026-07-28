---
type: guidance
title: Cloud Monitoringメトリクスの長期分析用BigQueryエクスポート
title_original: Cloud Monitoring metric export
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: cost
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/monitoring-metric-export
published_at: '2026-07-23'
---

## 概要

Cloud Monitoringが保持する6週間分のメトリクスを、繁忙期比較やコスト予測など長期トレンド分析のためにBigQueryへエクスポートするサーバーレス参照実装を解説。メトリクスは集計してから保存することを推奨している。
