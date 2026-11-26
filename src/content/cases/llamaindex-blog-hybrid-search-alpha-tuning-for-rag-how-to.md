---
type: guidance
title: クエリ種別ごとにハイブリッド検索のalphaを調整する方法
title_original: Enhancing Retrieval Performance with Alpha Tuning in Hybrid Search in RAG
industry: cross-industry
cloud: []
patterns:
- rag
- eval
- full-text-search
components:
- Weaviate
- LlamaIndex
- BM25
- GPT-4
- Cohere Rerank
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-enhancing-retrieval-performance-with-alpha-tuning-in-hybrid-search-in-rag-135d0c9b8a00
published_at: '2024-01-31'
---

## 概要

BM25とベクトル検索の重みalphaを、Web検索型・事実質問・キーワード・誤字などのクエリ種別ごとに、Hit RateとMRRで評価して調整する手順を示す。

## 設計のポイント

- alphaは固定せず、クエリ種別を判定して振り分ける。
- 合成クエリを作り、Hit RateとMRRで定量的に決める。
- リランカーの有無も条件に含めて比較する。

## 使いどころ

- ハイブリッド検索の精度を改善したいRAG開発者。
