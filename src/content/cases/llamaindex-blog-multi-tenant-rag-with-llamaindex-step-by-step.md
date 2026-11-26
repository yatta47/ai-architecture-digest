---
type: guidance
title: メタデータフィルタで利用者ごとに検索を分離するマルチテナントRAG
title_original: Multi-Tenancy RAG with LlamaIndex
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- multi-tenant-rag
- rag
components:
- LlamaIndex
- IngestionPipeline
- VectorStoreIndex
- Qdrant
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-multi-tenancy-rag-system-with-llamaindex-0d6ab4e0c44b
published_at: '2024-01-15'
---

## 概要

1つのインデックスに投入する文書へ利用者情報をメタデータとして付与し、検索時に完全一致フィルタで本人の文書だけを対象にする手順を示す。別の利用者の文書に関する質問には回答できないことをサンプルで確認している。

## 設計のポイント

- 取り込み時に全文書へテナント識別子を必ず付与し、インデックスは共有する。
- 意味検索の前にメタデータフィルタを適用し、取得段階で境界を強制する。
- 他テナントの情報を問う質問で漏えいがないことを検証する。

## 使いどころ

- 利用者や顧客ごとの文書を1つのRAG基盤で扱うSaaS開発者。
- 機密文書の相互参照を防ぎつつインデックス運用をまとめたい場面。
