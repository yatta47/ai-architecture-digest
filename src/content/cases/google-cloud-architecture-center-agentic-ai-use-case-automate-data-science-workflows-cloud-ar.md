---
type: guidance
title: 自然言語でSQL/Pythonを書かずにデータ分析・機械学習を自動化するマルチエージェントシステム
title_original: 'Agentic AI use case: Automate data science workflows'
industry: cross-industry
cloud:
- gcp
patterns:
- multi-agent-orchestration
- text-to-sql
components:
- Cloud Run
- Agent Development Kit (ADK)
- Gemini Enterprise Agent Platform
- Gemini
- BigQuery
- AlloyDB for PostgreSQL
- MCP Toolbox for Databases
- BigQuery ML
outcome:
  type: productivity
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/agentic-ai-data-science
published_at: '2026-07-19'
---

## 概要

Google Cloudは、自然言語の指示だけでBigQueryやAlloyDBのデータ分析・可視化・機械学習を実行できるマルチエージェントのデータサイエンスワークフローを示す。ルートエージェントが分析用・DB接続用・BigQuery ML用の専門エージェントへタスクを振り分ける構成で、SQLやPythonを書かずに複雑な分析を可能にする。

## 設計のポイント

- ルートエージェントがリクエストを解釈し、自身で解決できない場合のみ分析・AlloyDB・BigQuery・BigQuery MLの各専門エージェントへ委譲する『agent as a tool』構成をとる
- AlloyDB用エージェントはPostgreSQL方言のSQLを、BigQuery用エージェントはGoogleSQLをそれぞれ生成し、MCP ToolboxやADK組み込みツールでDB接続の複雑さを隠蔽する
- BigQuery MLエージェントはモデルの学習・評価・予測生成までMLライフサイクル全体を担当する専門サブエージェントとして独立させる

## 使いどころ

- SQLやPythonを書けない事業部門メンバーが自然言語でデータ分析したい小売・金融・製造業
- フライトデータやECの売上データなど複数業種のデータセットに対する柔軟な分析基盤を構築したいデータチーム
