---
type: case
title: TemporalとLakebaseで実現する耐久性のあるローン審査エージェント
title_original: Build durable agents with Temporal and Lakebase
company: Databricks
industry: financial-services
cloud: []
patterns:
- ai-agent
- human-in-the-loop
- event-driven
components:
- Temporal
- Databricks Lakebase
- Unity Catalog
- FastAPI
- Delta Lake
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/build-durable-agents-temporal-and-lakebase
published_at: '2026-09-08'
---

## 概要

個人ローン審査エージェントを、Temporalの耐久実行とDatabricks Lakebase（Postgres）のクエリ可能な運用状態で構成するリファレンス実装。ワーカー再起動やツール呼び出し失敗からの復旧、数日単位のレビュアー待ち、Unity Catalogのポリシー同期を扱い、モデルは推奨のみを行い最終判断は人間が下す設計とする。

## 設計のポイント

- TemporalのActivityで各ステップの結果を記録してリトライ耐性を持たせ、Workflowの制御フロー状態から復旧を可能にする
- 証跡・推奨・レビュー決定・メトリクスをLakebaseに書き込み、アプリケーションからリレーショナルにクエリできるようにする
- Unity CatalogのポリシーをLakebaseの同期テーブルで参照し、Change Data FeedでDelta履歴テーブルへ運用変更を書き戻す
- モデルは推奨のみを行い、承認・却下の最終判断は必ず人間のアンダーライターがSignalで返す

## 使いどころ

- 人間のレビュー待ちで数日単位の長時間実行が発生するエージェントワークフロー
- ワーカー障害やデプロイでプロセスが入れ替わっても進捗を失いたくない業務システム
