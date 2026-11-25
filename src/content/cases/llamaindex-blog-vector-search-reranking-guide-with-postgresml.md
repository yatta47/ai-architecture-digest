---
type: guidance
title: PostgresMLとクロスエンコーダで改善するベクトル検索の再ランク
title_original: Improving Vector Search Reranking With PostgresML
company: PostgresML
industry: cross-industry
cloud: []
patterns:
- rag
- full-text-search
components:
- PostgresML
- LlamaIndex
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/improving-vector-search-reranking-with-postgresml-and-llamaindex
published_at: '2024-07-19'
---

## 概要

初回検索の結果をクロスエンコーダで再ランクし、関連度を高める方法を解説する。PostgresMLのマネージドインデックスが文書の保存、分割、埋め込み、検索をデータベース側で担う。

## 設計のポイント

- クロスエンコーダは高コストなので、絞り込んだ候補の再ランクに限って使う。
- 利用者の操作履歴がない新規コンテンツには、クロスエンコーダの再ランクが有効。
- 分割と埋め込みをデータベース側に寄せ、アプリ側の前処理をなくす。

## 使いどころ

- 検索結果の関連度が物足りないRAGの改善。
- PostgreSQL中心で検索基盤を簡素化したいチーム。
