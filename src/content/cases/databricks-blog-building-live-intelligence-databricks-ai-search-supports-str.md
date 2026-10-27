---
type: announcement
title: AI Searchがストリーミングテーブル等に対応
title_original: 'Building live intelligence: Databricks AI Search supports streaming tables and materialized views'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- rag
- full-text-search
- unified-transactional-analytical-storage
components:
- Databricks AI Search
- Streaming Tables
- Materialized Views
- Apache Iceberg
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/building-live-intelligence-databricks-ai-search-supports-streaming-tables-materialized-views
published_at: '2026-10-26'
---

## 概要

Databricks AI SearchがDeltaに加え、ストリーミングテーブル、マテリアライズドビュー、Iceberg v3+のマネージドテーブルを直接インデックス化でき、別の同期パイプラインなしでリアルタイム検索を作れる。

## 設計のポイント

- ソースの更新がインデックスに自動反映され、同期パイプラインが不要になる。
- マテリアライズドビューで個人化された状態を検索に使える。

## 使いどころ

- 新着情報や在庫をすぐ検索したいアプリ。
- 複数エンジンのデータを横断検索したいチーム。
