---
type: case
title: Postgres内で完結するハイブリッド検索のサイジング指針（社内スライド検索アプリ）
title_original: 'Sizing Lakebase Search: Lessons from a Real App and 4 Million Passages'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- full-text-search
- rag
- cost-optimization
components:
- Lakebase Postgres
- Lakebase Search
- lakebase_vector
- lakebase_bm25
- MCP
- Databricks Apps
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/sizing-lakebase-search-lessons-real-app-and-4-million-passages
published_at: '2026-10-15'
---

## 概要

約700の社内資料・2.3万スライドを検索する社内アプリSlide Hubを題材に、ベクトル検索とBM25をPostgres拡張としてアプリDB内で動かすハイブリッド検索のサイジングを検証した記事。ローカルファイルキャッシュをベクトルインデックスと同程度にするとウォームな検索が一桁msになり、常時稼働0.5CU(月31〜40ドル)が本番の基準とされる。

## 設計のポイント

- ベクトル(ANN)とBM25を同一Postgres内に置き、1本のSQLでRRF(k=60)融合・権限フィルタ・投票結合まで行い、別検索基盤と二重トランザクションを避ける
- 候補数を1000から200に絞ってもtop10の90.5%を維持しつつページ読み取りを1/3にする
- 負荷試験でDB側とアプリ側を片方ずつ変え、8CU未満はDBを増やし、それ以上はアプリワーカーを増やすという律速の見極め手順を採る

## 使いどころ

- アプリDBに検索を同居させたいPostgres利用のチーム
- MCP経由でエージェントに検索ツールを渡す前にコンピュートサイズを決めたい場面
