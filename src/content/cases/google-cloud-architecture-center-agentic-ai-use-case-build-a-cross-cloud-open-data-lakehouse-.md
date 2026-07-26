---
type: guidance
title: AWSとGoogle Cloudをまたぐオープンデータレイクハウスでエージェント駆動の分析を行う
title_original: 'Agentic AI use case: Build a cross-cloud open data lakehouse'
industry: cross-industry
cloud:
- gcp
- aws
- multi-cloud
patterns:
- data-federation
- ai-agent
components:
- Managed Service for Apache Spark
- Lightning Engine
- Amazon S3
- Databricks Unity Catalog
- AlloyDB for PostgreSQL
- Cloud Storage
- Lakehouse for Apache Iceberg
- Cloud NAT
- Cloud Router
- Secret Manager
- BigQuery
- BigQuery MCP server
- Gemini CLI
outcome:
  type: cost
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/agentic-ai-build-multicloud-open-data-lakehouse
published_at: '2026-07-19'
---

## 概要

Google Cloudは、Databricks Unity CatalogやAmazon S3上のデータをETLでコピーせずにApache Iceberg形式のレイクハウスへ統合し、BigQuery MCPサーバー経由でGemini CLIなどのAIエージェントから分析できるクロスクラウド構成を示す。AlloyDBとBigQueryのフェデレーションによりCDCパイプラインなしでリアルタイムデータにも分析エンジンから直接アクセスする。

## 設計のポイント

- Databricks Unity CatalogやAmazon S3のデータをコピー・移行せず『その場』で分析することで、ETLパイプラインによる重複やコストを回避する
- Managed Service for Apache SparkのLightning Engineでクロスクラウドの大規模結合・ウィンドウ処理を高速に実行する
- BigQueryとAlloyDBをフェデレーションし、CDCパイプラインを介さずにライブなトランザクションデータへ直接クエリできるようにする
- BigQuery MCPサーバーが統治済みレイクハウスのコンテキストをGemini CLIなどの外部AIモデルへ安全に公開し、カスタムREST APIの開発・保守を不要にする

## 使いどころ

- Amazon S3上のロイヤリティデータとBigQuery上のマーケティング運用データを横断分析したい小売企業のマーケティング担当者
- サプライチェーンの構造化データと非構造化のメール・損害報告書を組み合わせて障害要因を分析したい調達担当者
