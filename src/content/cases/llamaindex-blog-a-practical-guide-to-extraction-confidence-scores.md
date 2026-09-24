---
type: guidance
title: 帳票抽出の信頼度スコアで自動承認と人手レビューの境界を決める方法
title_original: A practical guide to extraction confidence scores
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- human-in-the-loop
- eval
components:
- LlamaIndex Extract
- LlamaParse
- ExtractBench
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/what-makes-an-extraction-confidence-score-useful
published_at: '2026-09-24'
---

## 概要

LlamaIndexが、文書からの抽出結果に付く0〜1の信頼度スコアを使い、自動承認と人手レビューの境界（カットオフ）を決める手順を解説した。97%の精度目標に対しExtractBenchでは約0.77のカットオフが必要で、その時点で自動承認できる割合と再現率が示される。

## 設計のポイント

- 業務が求める精度目標（例: 自動承認値の97%が正しい）を先に決め、その精度を満たす最低のカットオフを選ぶ。
- 代表的な文書と正解データを用意し、カットオフを上げながら精度を測る。
- カットオフの決定に使っていない別データで再検証する。
- 文書の傾向が変わるため、定期的に手順を再実行する。

## 使いどころ

- 請求書や契約書などの抽出を大量に処理し、人手レビューの件数を最小化したい業務部門。
- 抽出結果の自動承認に精度保証を持たせたいエンタープライズ。
- 抽出パイプラインに Human-in-the-loop を組み込む設計者。
