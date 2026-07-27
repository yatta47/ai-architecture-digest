---
type: guidance
title: Two-Tower検索モデルで実現する大規模レコメンドの候補生成基盤
title_original: Implement two-tower retrieval for large-scale candidate generation
industry: cross-industry
cloud:
- gcp
patterns:
- two-tower-retrieval
- inference-optimization
components:
- Gemini Enterprise Agent Platform
- Vector Search
- Cloud Storage
outcome:
  type: speed
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/implement-two-tower-retrieval-large-scale-candidate-generation
published_at: '2026-07-19'
---

## 概要

クエリと候補アイテムをそれぞれ別のニューラルネットワーク(タワー)で埋め込みベクトルに変換するTwo-Tower方式のレコメンド候補生成アーキテクチャ。候補タワーの埋め込みを事前計算しVector Searchの近似最近傍インデックスとしてデプロイすることで、低レイテンシな候補生成を実現する。

## 設計のポイント

- クエリタワーと候補タワーを別々にデプロイし、候補側は事前計算・クエリ側はオンライン推論と役割を分離する
- 候補アイテムの埋め込みを事前計算しANNインデックス化することでオンライン推論のレイテンシを最小化する
- 未学習の新規アイテムでも特徴量さえあれば埋め込みを計算できるためコールドスタート問題に対応できる

## 使いどころ

- 数百万件規模の候補から低レイテンシで数百件に絞り込む必要がある大規模レコメンドシステム
- 新着商品・新着コンテンツを再学習なしに検索対象へ即座に組み込みたいEC/メディア事業者
