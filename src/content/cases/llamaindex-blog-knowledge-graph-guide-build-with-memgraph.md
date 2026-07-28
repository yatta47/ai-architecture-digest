---
type: guidance
title: LlamaIndex+Memgraphでテキストからナレッジグラフを構築・自然言語で問い合わせる
title_original: Constructing a Knowledge Graph with LlamaIndex and Memgraph
company: Memgraph
industry: cross-industry
cloud: []
patterns:
- knowledge-graph
- rag
components:
- Memgraph
- LlamaIndex
- OpenAI GPT-4
- text-embedding-ada-002
- SchemaLLMPathExtractor
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/constructing-a-knowledge-graph-with-llamaindex-and-memgraph
published_at: '2026-07-22'
---

## 概要

LlamaIndexのPropertyGraphIndexとSchemaLLMPathExtractorを使い、非構造化テキスト(ダーウィンの伝記)からMemgraph上にナレッジグラフを自動構築し、自然言語クエリで関係性を検索するハンズオンガイド。LLMSynonymRetrieverによるデフォルトの自然言語検索も紹介している。

## 設計のポイント

- SchemaLLMPathExtractorでLLMにエンティティ・関係抽出を担わせ、グラフ構築を自動化する
- LLMSynonymRetrieverなどのリトリーバーを使い、専用クエリ言語を知らないユーザーでも自然言語でグラフを検索できるようにする

## 使いどころ

- 非技術者でも自然言語でナレッジベースを検索できるようにしたい社内ツール担当者
- 非構造化文書から関係性を可視化・分析したいアナリスト
