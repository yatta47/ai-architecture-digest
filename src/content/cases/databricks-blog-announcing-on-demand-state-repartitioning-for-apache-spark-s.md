---
type: announcement
title: チェックポイントを保持したままStructured Streamingのパーティション数をオンデマンド変更
title_original: Announcing on-demand state repartitioning for Apache Spark Structured Streaming on Databricks
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/announcing-demand-state-repartitioning-apache-sparktm-structured-streaming-databricks
published_at: '2026-09-14'
---

## 概要

Databricks Runtime 18以降でApache Spark Structured Streamingのステートフルクエリにおいて、チェックポイントを作り直すことなくパーティション数をオンデマンドで変更できる「State Repartitioning」がパブリックプレビューで登場。RocksDBステートストアを使い再起動時に状態を新しいパーティション数へ安全に再分配する。早期採用したCoveoは伸縮するデータ量に合わせて自由にスケールできるようになりAmazon S3 APIコストを40%削減した。
