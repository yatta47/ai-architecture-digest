---
type: guidance
title: Zilliz Cloud Pipelinesでマルチテナント対応のRAG検索を組む
title_original: Building Scalable RAG Applications with LlamaIndex and Zilliz Cloud Pipelines
company: Zilliz
industry: cross-industry
cloud:
- aws
- gcp
patterns:
- rag
- multi-tenant-rag
components:
- Zilliz Cloud Pipelines
- LlamaIndex
- Amazon S3
- Google Cloud Storage
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-scalable-rag-applications-with-llamaindex-and-zilliz-cloud-pipelines-4879e9768baf
published_at: '2024-01-25'
---

## 概要

取り込み・埋め込み・検索をマネージドサービスに任せ、LlamaIndexからManagedIndexとして使うRAGチャットボットの作り方。メタデータフィルタでユーザーごとにデータを分離する。

## 設計のポイント

- 検索パイプラインはマネージド化し、アプリは回答生成とUIに集中する。
- user_idをメタデータに付け、検索時のフィルタでテナントを分離する。

## 使いどころ

- 検索基盤の運用を持ちたくないRAG開発チーム。
- 利用者ごとのデータ分離が必要なSaaS。
