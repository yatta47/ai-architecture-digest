---
type: announcement
title: Genie CodeでTableau/Power BIレポートをフォルダ単位で一括移行
title_original: Bulk migrate your dashboards to AI/BI with Genie Code
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- parallel-execution
- business-intelligence-resilience
components:
- Databricks Genie Code
- Databricks AI/BI Dashboards
- Unity Catalog
- Unity Catalog metric views
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/bulk-migrate-your-dashboards-aibi-genie-code
published_at: '2026-11-19'
---

## 概要

Databricksは、Genie Codeの/importBIでTableauやPower BIのレポートをフォルダ単位でAI/BIダッシュボードへ一括移行できるようにした。バッチで処理し、状態を表示しつつ、移行時に作るメトリクスビューを再利用可能な意味層として残せる。

## 設計のポイント

- 1件ずつの移行をバッチ化し、キュー・実行・完了の状態を見えるようにする。
- 既存のテーブルやメトリクスビューを再利用し、重複定義を避ける。
- 移行で作ったメトリクスビューをUnity Catalogに昇格して意味層にする。

## 使いどころ

- 数十〜数百のBIレポートを抱えるBI移行プロジェクト。
- ダッシュボード移行と同時に指標定義を統一したいとき。
