---
type: guidance
title: 基本から高度RAGまでの改善手法を整理したチートシート
title_original: A Cheat Sheet and Some Recipes For Building Advanced RAG
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- eval
components:
- LlamaIndex
- ParamTuner
- SemanticSimilarityEvaluator
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b
published_at: '2024-01-05'
---

## 概要

RAGの成功条件を「関連文書を取得できる」「取得内容を生成で活かせる」の2点に定め、それぞれを改善する手法とコード例を整理した。チャンクサイズ調整などを評価指標に基づいて行う方法を示す。

## 設計のポイント

- 改善手法は検索側と生成側のどちらの課題に効くかで分類して選ぶ。
- チャンクサイズやtop-kは参照回答付きの評価セットで探索して決める。

## 使いどころ

- 初めてRAGを作る開発者の道筋整理。
- 基本RAGの回答品質が頭打ちになったチームの改善検討。
