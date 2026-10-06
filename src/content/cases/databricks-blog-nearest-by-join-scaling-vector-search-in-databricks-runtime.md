---
type: announcement
title: Databricksのバッチベクトル検索SQL結合NEAREST BY
title_original: 'NEAREST BY join: Scaling vector search in Databricks Runtime'
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- parallel-execution
- inference-optimization
components:
- Databricks Runtime
- Photon
- Delta Lake
- NEAREST BY
- IVF index
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/nearest-join-scaling-vector-search-databricks-runtime
published_at: '2026-10-05'
---

## 概要

バッチ型ベクトル検索のためのSQL結合NEAREST BYを紹介する。クエリ行ごとにk近傍を正確または近似で求め、融合Photon演算子と独自GEMMカーネルでスループットを高める。IVFインデックスは液体クラスタリングDeltaテーブルで、別のベクトルストアは不要。

## 設計のポイント

- レイテンシでなくバッチ全体のスループットとSLAを基準に設計する。
- IVFインデックスを通常のDeltaテーブルとし、同期対象の別システムを持たない。
- 距離計算を融合演算子とブロック化GEMMでハードウェア性能に近づける。
- ジョブに合わせて並列度を伸縮し、終了後はゼロに戻す。

## 使いどころ

- エンティティ解決、重複排除、意味タグ付けなどの大量バッチ処理。
- 夜間に数千万件のレコードを埋め込みで拡充する場面。
