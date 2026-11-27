---
type: announcement
title: RAGの可観測性と検索評価を強化した週次アップデート（2023-10-10）
title_original: LlamaIndex Update 2023-10-10
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- eval
- llmops
components:
- LlamaIndex
- Arize AI Phoenix
- RetrieverEvaluator
- LongContextReorder
- TimescaleDB
- Neo4j
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-update-2023-10-10-3718a3d19fb9
published_at: '2023-10-10'
---

## 概要

Arize Phoenixによる1行のトレース連携、検索単体を測るRetrieverEvaluator、Multi-Document Agentsなどを紹介する週次更新。

## 設計のポイント

- 生成の評価とは別に、検索段階をランキング指標で単独評価する。
- 過剰に取得すると重要文脈が埋もれるため、文脈の並べ替えを挟む。
- プロンプト・トークン・検索結果のトレースをローカル保存し、データを外に出さずに観測する。

## 使いどころ

- RAG/エージェントの品質劣化の原因を切り分けたいチーム向け。
- データを社外に出せない環境で可観測性を整えたい場合。
