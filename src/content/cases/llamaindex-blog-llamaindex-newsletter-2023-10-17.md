---
type: announcement
title: SQL+ベクトル検索や複数文書エージェントなどの週次機能まとめ（2023-10-17）
title_original: LlamaIndex Newsletter 2023-10-17
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- text-to-sql
- ai-agent
- eval
components:
- LlamaIndex
- PGVectorSQLQueryEngine
- text-embeddings-inference
- UnstructuredIO
- AssemblyAI
- Nougat
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-10-17-33514cbc04a2
published_at: '2023-10-17'
---

## 概要

LlamaIndexの週次ニュースレター。PostgreSQL上でSQLとベクトル検索を併用するエンジン、Multi-Document Agents、表を含む文書の階層パーサなどを紹介する。

## 設計のポイント

- 構造化条件と意味検索が混在する問いは、同じPostgreSQL上でSQLとベクトル検索を併用する。
- 表を含む文書は平文分割せず、表と本文を階層的にモデル化して扱う。
- チャンクは多いほど良いとは限らないため、サイズとtop-kを評価で調整する。

## 使いどころ

- 表やPDFが多い文書群でRAG精度を上げたい開発者向け。
- LlamaIndex周辺の新機能と連携先を把握したいチーム向け。
