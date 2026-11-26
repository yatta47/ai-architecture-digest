---
type: announcement
title: Query Pipelinesと本番ETL構成など：LlamaIndex週次更新（2024-01-09）
title_original: LlamaIndex Newsletter 2024-01-09
company: LlamaIndex
industry: cross-industry
cloud:
- aws
patterns:
- rag
- ai-agent
components:
- LlamaIndex
- Query Pipelines
- RAGatouille
- ColBERT
- AWS EKS
- RabbitMQ
- NVIDIA Triton
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-01-09-6209000da2e6
published_at: '2024-01-09'
---

## 概要

RAGワークフローを宣言的に組むQuery Pipelines、AWS EKS上の本番ETLパイプライン、マルチモーダルReActエージェントなどを紹介する週次まとめ。2024年のロードマップとオフィスアワーも告知している。

## 設計のポイント

- 複雑化するRAGの処理順序はDAGとして宣言的に記述する。
- 取り込み処理はキューを挟んで並列化し、手元の逐次処理から切り離す。

## 使いどころ

- LlamaIndexの新機能を追ってRAG構成を見直したい開発者。
