---
type: case
title: コンピュートとストレージを分離したPostgresの無停止オートスケーリング
title_original: Autoscaling Lakebase Postgres
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
source_url: https://www.databricks.com/blog/autoscaling-lakebase-postgres
published_at: '2026-08-31'
---

## 概要

DatabricksのLakebase Postgresは、Postgresを実行するコンピュート層と、WAL・ページ・オブジェクトストレージからなる永続化層を分離したアーキテクチャにより、データベースを停止せずにVMサイズをその場でリサイズするオートスケーリングを実現している。CPU負荷・メモリ使用量に加え、HyperLogLogを時間窓付きに拡張して推定した『ワーキングセットのキャッシュ適合度』の3シグナルを監視し、それぞれが算出する目標コンピュートサイズのうち最大値を採用することでスケーリングの見落としを防いでいる。
