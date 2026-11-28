---
type: announcement
title: 文書ごとの要約を索引にするDocument Summary Index
title_original: A New Document Summary Index for LLM-powered QA Systems
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
components:
- LlamaIndex
- Document Summary Index
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/a-new-document-summary-index-for-llm-powered-qa-systems-9a32ece2f9ec
published_at: '2023-05-08'
---

## 概要

文書単位の要約を抽出して索引化する新しいLlamaIndexのデータ構造を紹介する記事。要約で関連文書を選び、その文書の全ノードを取得することで、チャンク単位の意味検索より広い文脈を得る。

## 設計のポイント

- 検索単位（文書要約）と回答に渡す単位（元の全ノード）を分離する。
- 構築時にLLMで要約を作り、要約と元ノードの対応を保持する。
- 要約に対してLLM検索と埋め込み検索のどちらも選べるようにする。

## 使いどころ

- チャンクだけでは文脈が足りないQAを改善したい場面。
- 文書数が多く、全文をLLMに読ませるとコストが高すぎる場面。
