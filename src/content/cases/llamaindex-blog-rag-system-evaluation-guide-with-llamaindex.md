---
type: guidance
title: 検索と生成の両面からRAGを評価するOpenAI Cookbook
title_original: Evaluating RAG Systems with LlamaIndex (OpenAI Cookbook)
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- eval
- rag
components:
- LlamaIndex
- VectorStoreIndex
- OpenAI Cookbook
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/openai-cookbook-evaluating-rag-systems-fe393c61fb93
published_at: '2023-11-28'
---

## 概要

RAGの仕組み、LlamaIndexでの構築、評価の3部構成のガイドを公開した。検索システムと応答生成を分けて評価し、評価用の質問と文脈の組は合成して作る。

## 設計のポイント

- 検索の品質と生成の品質を別々に測り、原因を切り分ける。
- 評価用の質問・文脈ペアは対象文書から合成して用意する。

## 使いどころ

- RAG評価をこれから始める開発者。
