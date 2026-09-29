---
type: announcement
title: Lakebase Postgresに組み込まれた全文検索とベクトル検索
title_original: 'Lakebase Search: state-of-the-art full-text and vector search in Postgres'
company: Databricks
industry: cross-industry
cloud:
- aws
- azure
patterns:
- full-text-search
- rag
- unified-transactional-analytical-storage
- inference-optimization
- cost-optimization
components:
- Lakebase Postgres
- lakebase_vector
- lakebase_text
- pgvector
- RaBitQ
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/lakebase-search-state-art-full-text-and-vector-search-postgres
published_at: '2026-09-28'
---

## 概要

Lakebase Postgresが拡張機能lakebase_vector（ANN検索）とlakebase_text（BM25）でセマンティック・キーワード・ハイブリッド検索を提供開始した。ストレージと計算を分離し、階層IVFと二値量子化を使うことで、1億ベクトルのベンチマークでpgvectorより低コストに97%再現率・P99 71msを出すとしている。

## 設計のポイント

- 検索エンジンを別立てにせず、運用DBと同じPostgres内で検索してETLを不要にする。
- ストレージと計算を分離し、インデックスがRAMに収まらなくても性能が落ちにくくする。
- インデックス構築を主DBから切り離し、ゼロスケール可能なサーバーレスでバースト的な検索に備える。

## 使いどころ

- エージェント向けに大量のベクトル検索を行うアプリ開発者。
- pgvectorのメモリコストや保守負荷に悩むチーム。
- BM25とベクトルのハイブリッド検索を単一DBで運用したい組織。
