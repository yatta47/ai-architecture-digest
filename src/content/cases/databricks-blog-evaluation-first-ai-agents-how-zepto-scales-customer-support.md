---
type: case
title: 評価ファーストのマルチエージェント設計でカスタマーサポートを自動化(Zepto)
title_original: 'Evaluation-first AI agents: How Zepto scales customer support with Databricks and MLflow'
company: Zepto
industry: retail
cloud: []
patterns:
- eval
- ai-agent
- llmops
- multi-agent-orchestration
components:
- Databricks
- MLflow
- Unity Catalog
- Delta Lake
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/evaluation-first-ai-agents-how-zepto-scales-customer-support-databricks-and-mlflow
published_at: '2026-09-09'
---

## 概要

インドのクイックコマース企業Zeptoは、1日10万件超のサポートチケットを処理するマルチエージェントAIシステムを、DatabricksとMLflowによる『評価ファースト』のアーキテクチャで運用している。開発ループと本番ループを品質ゲートでつなぐデュアルループ構成により、トレース・ゴールデンデータセット・LLM-as-judge評価を核として、失敗を可視化し継続的に改善する。この結果、サポートコストを65%削減し、1か月未満で投資回収した。

## 設計のポイント

- 開発ループと本番ループを『品質ゲート』で接続し、閾値を満たしたバージョンのみ本番に昇格させるデュアルループ構成にする
- mlflow.autolog()と@mlflow.traceでエージェントの全ステップ（プロンプト・ツール呼び出し・遅延）をOpenTelemetryトレースとして記録し、Unity Catalog経由でDelta Tableに集約する
- ステークホルダーごとに『評価の柱』を定義し、それぞれに数値ゲート閾値を設けてデプロイ判断を属人的な感覚から証拠ベースへ移行する
- ゴールデンデータセットを開発ループの単一の真実源とし、回帰評価を自動化してプロンプト・ポリシー変更の反復速度を上げる

## 使いどころ

- 1日数万〜数十万件規模のチケットを処理する大規模カスタマーサポートAIエージェント
- 多段階の意思決定を行うエージェントで、途中の失敗が最終回答に隠れてしまうのを防ぎたい場合
- 複数ステークホルダー（CX・オペレーション・リスク・財務）の要求を一つの評価基準に統合したいチーム
