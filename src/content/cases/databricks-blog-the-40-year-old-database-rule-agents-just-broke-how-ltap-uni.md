---
type: case
title: AIエージェント時代のOLTP/OLAP統合ストレージ基盤LTAP
title_original: 'The 40-Year-Old Database Rule Agents Just Broke: How LTAP Unifies OLTP and OLAP Workloads'
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- unified-transactional-analytical-storage
- ai-agent
components:
- Lakebase
- Postgres
- Delta Lake
- Apache Iceberg
- Apache Spark
- Parquet
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/40-year-old-database-rule-agents-just-broke-how-ltap-unifies-oltp-and-olap-workloads
published_at: '2026-09-07'
---

## 概要

DatabricksのJonathan Katzは、AIエージェントがミリ秒単位の鮮度で運用データを読み書きする必要から、数十年続いてきたOLTP/OLAP分離の前提が崩れつつあると説明する。LTAP（Lake Transactional/Analytical Processing）はエンジン層ではなくストレージ層で両者を統合し、行形式のホット層と列形式のコールド層を組み合わせることで、コストと複雑さの面でHTAPが解決できなかった課題に応える。

## 設計のポイント

- エンジンではなくストレージ層で運用/分析データを統合し、コンピュートは用途ごとに分離してサーバーレスに個別課金する
- PostgresのデータをビットレベルでParquet形式へ変換し、Delta LakeやIcebergなど既存レイクハウス形式のままSpark/SQLから直接読めるようにする
- ホット層（行形式・低レイテンシの運用アクセス）とコールド層（列形式・分析アクセス）の2層構成で用途ごとに最適なアクセスを提供
- ストレージから分離されたステートレスなコンピュート（Neon由来のアーキテクチャ）により高スループット書き込みとオブジェクトストレージへの非同期フラッシュを両立

## 使いどころ

- 数百ミリ秒単位で発生する不正検知など、鮮度の高い運用データに対してAIエージェントがリアルタイムに分析クエリを投げたい場面
- 多数のエージェント群が運用システムへ大量の読み書きを行い、既存OLTPシステムの負荷が問題になるケース
- ETLパイプラインによるデータ複製・移動のコストと鮮度劣化を避けたいリアルタイム分析基盤の構築
