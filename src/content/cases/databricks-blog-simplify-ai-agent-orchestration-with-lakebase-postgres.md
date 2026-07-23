---
type: case
title: LakebaseだけでAIエージェントの長時間タスクキューを実装する(CLA監査文書処理)
title_original: Simplify AI agent orchestration with Lakebase Postgres
company: CliftonLarsonAllen LLP (CLA)
industry: other
cloud: []
patterns:
- ai-agent
- document-processing
- event-driven
components:
- Lakebase Postgres
- Databricks Apps
- Lakeflow Jobs
- MLflow
- Unity Catalog Volumes
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/simplify-ai-agent-orchestration-lakebase-postgres
published_at: '2026-07-22'
---

## 概要

監査法人CLAとDatabricksは、Lakebase Postgresの2つのテーブルだけで、外部ブローカーやスケジューラなしに長時間実行するエージェント文書処理タスクの耐障害性キューを構築した。優先度付き並行デキュー、レート制限考慮のスロットリング、タスク単位のコスト帰属、LISTEN/NOTIFYとSSEによるリアルタイム進捗表示を組み合わせ、抽出時間を数時間から数分に短縮した。

## 設計のポイント

- Kafka/Redis等の外部ブローカーやAirflow/Temporalのような別スケジューラを使わず、Postgresの2テーブルだけでキューを実装する
- tasksとtask_attemptsを親子関係にすることでリトライごとの試行を独立に記録し、コスト帰属とデバッグ性を両立する
- Postgres LISTEN/NOTIFYトリガーとServer-Sent Eventsを組み合わせ、低レイテンシのオペレーターダッシュボードをゼロオーバーヘッドで実現する
- ストレージとコンピュートを分離するLakebaseの特性を活かし、需要に応じてコンピュートだけをスケールさせる

## 使いどころ

- 大量の契約書・請求書・財務書類を構造化データに変換する必要がある監査・会計業務
- LLM/画像認識APIのレート制限を意識しながら長時間タスクをさばく必要があるエージェント運用
- 外部インフラを増やさずDatabricksネイティブでオーケストレーションを完結させたいチーム
