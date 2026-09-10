---
type: case
title: Kinaxis Maestroによるエージェント型サプライチェーン計画
title_original: What if everything changes tomorrow? A Canadian company is using agentic AI for supply chain resilience
company: Kinaxis
industry: logistics
cloud:
- azure
patterns:
- multi-agent-orchestration
- ai-agent
- decision-execution
components:
- Azure Kubernetes Service
- Azure Databricks
- Azure OpenAI
- Azure Cosmos DB
- Azure AI Content Safety
outcome:
  type: speed
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://news.microsoft.com/source/canada/features/ai/kinaxis-supply-chain/
published_at: '2026-09-10'
---

## 概要

カナダのKinaxisは、需要予測・在庫・生産などをこれまで別々のシステムで管理していたサプライチェーン計画を、予測AIとエージェント型AIを組み合わせた単一モデルのプラットフォームMaestroに統合した。ホルムズ海峽情勢下でシナリオモデリングの利用が120%以上増加するなど、地政学リスクへの即応を支援する。

## 設計のポイント

- 販売・生産・在庫といった機能別に分断されていたシステムを1つのモデルに統合し、変化の波及を一括評価できるようにする
- 社内データと天候・市場動向・ニュースなどの外部シグナルを組み合わせ、予測AIとエージェントAIの複数レイヤーで推論する
- Azure Kubernetes ServiceとAzure Databricksで大量データのリアルタイム処理とスケーリングを支える

## 使いどころ

- 関税・地政学リスクなど外部環境変化に対し、シナリオ分析を高速に回したいグローバル製造・物流企業
- 需要計画・生産計画・在庫管理が個別最適化され、全体最適の意思決定ができていない組織
