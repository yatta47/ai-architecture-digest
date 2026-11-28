---
type: guidance
title: 埋め込み検索の後段をLLMで並べ替える2段階検索
title_original: Using LLMs for Retrieval and Reranking
industry: cross-industry
cloud: []
patterns:
- rag
- cost-optimization
components:
- LlamaIndex
- LLMRerank
- ListIndexLLMRetriever
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/using-llms-for-retrieval-and-reranking-23cf2d3a14b6
published_at: '2023-05-17'
---

## 概要

LLMによる検索・再ランキングの抽象化を紹介する記事。LLM検索は関連性が高い一方で遅く高価なため、埋め込み検索で候補を絞ってからLLMで並べ替える構成を提案している。

## 設計のポイント

- 第1段は高いtop-kの埋め込み検索で再現率を確保し、第2段のLLM再ランキングで精度を上げる。
- 候補をバッチに分けてLLMに関連度を採点させ、結果を集約する。
- 長い文書は要約を渡してプロンプトに収める。

## 使いどころ

- 単純なtop-k検索で無関係な文脈が混じるRAGを改善したい場面。
- 精度と遅延・コストの折り合いを調整したいチーム。
