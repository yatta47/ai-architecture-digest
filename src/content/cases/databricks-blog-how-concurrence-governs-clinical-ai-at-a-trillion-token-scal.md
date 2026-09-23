---
type: case
title: 臨床AIエージェントを1.2兆トークン規模で統制するConcurrenceのデータ・AIガバナンス基盤
title_original: How Concurrence governs clinical AI at a trillion-token scale with Unity Gateway
company: Concurrence
industry: healthcare
cloud: []
patterns:
- ai-agent
- llm-gateway
- guardrails
- context-engineering
- eval
components:
- Databricks Lakebase
- Unity Catalog
- Unity Gateway
- Zerobus Ingest
- Apache Spark Declarative Pipelines
- Databricks Apps
- Delta Lake
outcome:
  type: risk-compliance
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-concurrence-governs-clinical-ai-trillion-token-scale-unity-gateway
published_at: '2026-09-23'
---

## 概要

Concurrenceは患者・医療者向けの臨床AIエージェントを、月約1008億入力トークン・1120万LLM呼び出しの規模で運用している。運用状態をLakebase、データとAI資産のガバナンスをUnity Catalog、AIアクセスの集中管理をUnity Gatewayに集約した。

## 設計のポイント

- 患者情報を不変イベントとして記録し、そこから現在の患者状態(world model)を算出して出所を保持し、エージェントに一貫した文脈を与えている。
- Zerobus IngestでイベントをDeltaテーブルへストリームし、宣言型パイプラインでworld modelを導出している。
- 独自のプロンプトログ基盤とreverse-ETLをガバナンス済みのDeltaとLakebase Synced Tablesに置き換えた。
- Unity Gatewayで開発者のAIワークロードのアクセスとセキュリティを集中管理している。

## 使いどころ

- 高い規制要件の下でエージェントを本番運用するヘルスケア企業。
- 相反する情報源から信頼できる状態を作る必要のある業務。
- LLM利用量が急増しアクセス統制が課題になっている組織。
