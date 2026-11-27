---
type: announcement
title: PostgreSQLをベクトルDBにするTimescale VectorのLlamaIndex統合
title_original: 'Timescale Vector x LlamaIndex: Making PostgreSQL A Better Vector Database For AI Applications'
company: Timescale
industry: cross-industry
cloud: []
patterns:
- rag
components:
- Timescale Vector
- LlamaIndex
- PostgreSQL
- pgvector
- DiskANN
- HNSW
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/timescale-vector-x-llamaindex-making-postgresql-a-better-vector-database-for-ai-applications-924b0bd29f0
published_at: '2023-09-27'
---

## 概要

Timescale VectorがLlamaIndexに統合された告知。DiskANN系の索引と時間パーティションにより、PostgreSQLでの高速な類似検索と期間絞り込みを実現するとする。

## 設計のポイント

- 埋め込み・リレーショナル・時系列データを1つのPostgreSQLに集約し、運用対象を減らす。
- 時間で自動パーティションし、鮮度や期間で絞るベクトル検索を効率化する。
- データ規模や用途に応じてDiskANN・HNSW・IVFFlatの索引を使い分ける。

## 使いどころ

- 既存のPostgreSQL資産を活かしてRAGを構築したいチーム向け。
- ニュースやログなど、期間指定の意味検索が必要な用途。
