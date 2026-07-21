---
type: case
title: ベクトル検索×AI Classifyで10万ラベル分類を1/100のコストで実現
title_original: Scaling document classification to 100k labels
company: Databricks
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- Databricks AI Classify
- Databricks Vector Search
- Qwen3-Embedding-8B
- Databricks AI Query
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/scaling-document-classification-100k-labels
published_at: '2026-07-20'
---

## 概要

Databricksは、生物医学用語の紐付けやベンダー名寄せなど10万ラベル超のタクソノミー分類において、ベクトル検索で候補ラベルを絞り込んでからAI Classify関数に渡す2段階方式を提案した。3つのベンチマークで、コスト効率の良いフロンティアモデル単体より精度で5ポイント上回りながら、トークンコストは約1/100に抑えられた。

## 設計のポイント

- 全ラベルをLLMのコンテキストに詰め込むと数千候補でハルシネーションが増えるため、まずベクトル検索(意味的類似度+BM25のハイブリッド)で候補を絞る。
- 10万ラベルの埋め込みはホスト型ベクトル検索インデックスより、オンメモリでインデックスを構築する方がコスト効率が良い。
- 絞り込んだショートリストのみをAI Classify関数に渡すことで、精度を落とさずコストとレイテンシを削減する。

## 使いどころ

- 正解データが疎で偏っており、教師あり分類器の学習が難しい大規模タクソノミーの分類タスク。
- タクソノミーが頻繁に更新され、regexやモデルの再学習を都度行うコストを避けたい場合。
