---
type: guidance
title: エージェント開発環境から複数クラウドの分散データを分析するワークフロー
title_original: Implement agentic analytics workflows for distributed data
industry: cross-industry
cloud:
- gcp
- aws
- multi-cloud
patterns:
- data-federation
- ai-agent
components:
- Google Cloud Data Agent Kit
- BigQuery
- Managed Service for Apache Spark
- Lakehouse for Apache Iceberg
- Knowledge Catalog
- Gemini
- Cloud Storage
- Cross-Cloud Interconnect
- Google Cloud MCP servers
- Amazon S3
- Databricks Unity Catalog
- Gemini CLI
- Claude Code
- Codex
outcome:
  type: speed
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/agentic-ai-cross-cloud-analytics
published_at: '2026-07-19'
---

## 概要

Google Cloudは、Gemini CLIやClaude Code、Antigravity IDEなどのエージェント型開発環境から、自然言語だけでBigQueryやAmazon S3にまたがる分散データの分析ワークフローを実行できるアーキテクチャを示す。Data Agent Kit拡張がMCPサーバーへの接続とスキル読み込みを担い、Knowledge Catalogが非構造化データから意味的メタデータを自動生成する。

## 設計のポイント

- データエンジニア・サイエンティストがCLIエージェントやIDEから自然言語で要求を送るだけで、Data Agent Kit拡張がスキルとMCPサーバーツールを組み合わせて分析ワークフローを実行する
- Knowledge CatalogがCloud Storage上の非構造化データをスキャンして意味的メタデータとコンテキストグラフを構築し、エージェントが発見しやすくする
- Cross-Cloud Interconnectでオンプレ以外のクラウド間を高帯域・低遅延に接続し、Amazon S3のデータをゼロコピーで読み込む
- 利用するエージェント環境（Antigravity IDE、VS Code、Gemini CLI、Claude Code、Codexなど）を問わず同じData Agent Kit拡張とMCPサーバー群を再利用できるようにする

## 使いどころ

- Amazon S3の顧客データとBigQueryのマーケティング運用データを横断分析したいグローバル小売のマーケティング担当者
- SCMシステムの構造化データとメール・損害報告書を組み合わせてサプライチェーン障害の要因を分析したい調達担当者
- 大量のPDF請求書から構造化データを抽出しBigQueryで経費分析したい業務担当者
