---
type: guidance
title: DebeziumとZerobus IngestでKafka無しのpush型CDCをレイクハウスへ
title_original: Push-based CDC into Unity Catalog with Zerobus Ingest and Debezium
ai_relevant: false
company: Databricks
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/push-based-cdc-unity-catalog-zerobus-ingest-and-debezium
published_at: '2026-11-05'
---

## 概要

閉じたネットワーク内のデータベースから、Debezium Serverが変更ログを読み、Zerobus IngestでUnity CatalogのDeltaテーブルへ直接pushするCDC構成の解説。Kafkaを介さない1ホップ構成にし、冪等キーや永続確認でソースのオフセット進行を安全に行う。
