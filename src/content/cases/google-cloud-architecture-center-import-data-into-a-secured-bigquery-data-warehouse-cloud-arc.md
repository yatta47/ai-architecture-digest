---
type: guidance
title: 機密データを扱うBigQueryデータウェアハウスのセキュア取り込みブループリント
title_original: Import data into a secured BigQuery data warehouse
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
source_url: https://docs.cloud.google.com/architecture/blueprints/confidential-data-warehouse-blueprint
published_at: '2026-07-20'
---

## 概要

オンプレミス等の外部ネットワークからBigQueryへ機密データを取り込む際の、データの非識別化・列レベル暗号化・列レベルアクセス制御などのガバナンス統制をTerraformで実装するブループリント。エンタープライズ基盤ブループリントへの追加統制として位置づけられる。
