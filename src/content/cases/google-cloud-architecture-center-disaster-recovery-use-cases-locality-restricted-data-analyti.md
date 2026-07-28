---
type: guidance
title: ロケーション制約下のデータ分析基盤（Dataflow/BigQuery）のDR設計
title_original: 'Disaster recovery use cases: locality-restricted data analytics applications'
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/dr-scenarios-locality-restricted-data-analytics
published_at: '2026-07-24'
---

## 概要

小売店のPOSデータをバッチ処理するETLパイプラインを例に、Cloud Storage・Managed Airflow・Managed Service for Apache Spark・BigQueryといったデータ分析基盤コンポーネントを、ロケーション制約下でどうDR設計するかを解説するDRシリーズ第6弾。
