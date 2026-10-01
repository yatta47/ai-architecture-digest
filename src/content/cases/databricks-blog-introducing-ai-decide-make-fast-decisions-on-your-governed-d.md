---
type: announcement
title: 高速な判断に特化したDatabricksのAI関数ai_decide
title_original: 'Introducing ai_decide: Make Fast Decisions on Your Governed Data'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- text-to-sql
- eval
components:
- Databricks
- ai_decide
- AI Functions
- Unity Catalog
- TypeSafe AI Jev
- Databricks Apps
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/introducing-aidecide-make-fast-decisions-your-governed-data
published_at: '2026-09-30'
---

## 概要

Databricksが、非構造化テキストから構造化された判断を返す新しいAI関数ai_decideをBetaで公開した。テキスト生成ではなく判断に最適化した決定モデルを使うため、同種のタスクでLLMより低遅延・低コストになる。SQLでのバッチ処理とREST APIでのリアルタイム利用の両方に対応する。

## 設計のポイント

- 分類や要否判定など複雑な推論が不要なタスクを、LLMでなく判断専用モデルに切り出し遅延とコストを下げる。
- 質問ごとに確率、名前付き選択肢、順序尺度のスコアのいずれかを返し、結果を構造化する。
- 同じ関数をSQLのバッチとREST APIのリアルタイムの両方で使える。
- プロンプトの難易度判定によるモデルルーティングやLLM評価の判定役に使える。

## 使いどころ

- 顧客レビューの問題タグ付けなど、ガバナンス下のデータへの大規模分類。
- 難易度に応じて複数モデルにリクエストを振り分けるAIアシスタント。
- エージェントが次のツールや分岐を即時に決める場面。
