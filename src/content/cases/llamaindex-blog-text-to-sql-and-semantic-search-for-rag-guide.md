---
type: guidance
title: 構造化データと非構造化データをまたぐText-to-SQL＋ベクトル検索エンジン
title_original: Combining Text-to-SQL with Semantic Search for Retrieval Augmented Generation
industry: cross-industry
cloud: []
patterns:
- rag
- text-to-sql
- data-federation
components:
- LlamaIndex
- SQLAutoVectorQueryEngine
- Pinecone
- Chroma
- Milvus
- Weaviate
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/combining-text-to-sql-with-semantic-search-for-retrieval-augmented-generation-c60af30ec3b
published_at: '2023-05-28'
---

## 概要

SQLデータベースへの問い合わせとベクトルストア検索を順に実行して統合するクエリエンジンを紹介する記事。集計で対象を特定してから文書を意味検索するような複合質問に答えられる。

## 設計のポイント

- SQLの結果を第1段の検索とし、その結果で質問を具体化してからベクトル検索に渡す。
- SQLとベクトル検索を名前と説明を持つツールとして包み、LLMに使い分けと結合を任せる。
- ベクトル側は自動検索でtop-kやメタデータフィルタを推定する。

## 使いどころ

- 統計テーブルと文書の両方にまたがる質問に答える社内QAを作る場面。
- 集計や結合が苦手なベクトル検索の限界を補いたい場面。
