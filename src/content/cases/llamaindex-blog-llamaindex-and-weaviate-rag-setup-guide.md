---
type: guidance
title: LlamaIndexとWeaviateによるドキュメントQA向けRAG構成
title_original: LlamaIndex and Weaviate
industry: cross-industry
cloud: []
patterns:
- rag
components:
- LlamaIndex
- Weaviate
- LlamaHub
- GPT-4
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-and-weaviate-ba3ff1cbf5f4
published_at: '2023-06-22'
---

## 概要

ベクトルDBのWeaviateとデータフレームワークのLlamaIndexを組み合わせたRAG構築の入門記事。Weaviateのブログ群を取り込み、チャンク化・索引化して質問応答する例を示している。

## 設計のポイント

- 外部ストレージ（ベクトルDB）とデータ取り込み・オーケストレーション層の責務を分ける。
- ベクトルストアを抽象化した共通インタフェース越しに接続し、クエリエンジンで検索と回答合成をまとめる。
- 問いの難度に応じて意味検索、Text-to-SQL、サブ質問分解を使い分ける。

## 使いどころ

- 社内文書の検索やチャットボットを初めて作る開発者。
- Weaviateを既に使っていてLLM回答層を足したいチーム。
