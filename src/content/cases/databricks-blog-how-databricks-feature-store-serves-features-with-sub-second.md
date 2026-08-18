---
type: guidance
title: KafkaからMLモデルまで200msで届くリアルタイム特徴量ストア
title_original: How Databricks Feature Store Serves Features with Sub-Second Freshness
company: Databricks
industry: cross-industry
cloud: []
patterns:
- event-driven
- inference-optimization
components:
- Databricks Feature Store
- Kafka
- Spark Real-Time Mode (RTM)
- Lakebase
- Model Serving
- Lakeflow Spark Delta Pipelines
- RocksDB
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-databricks-feature-store-serves-features-sub-second-freshness
published_at: '2026-08-17'
---

## 概要

Databricks Feature Storeは、Kafkaのストリーミングイベントからオンライン特徴量ストアまでをp99レイテンシ200msで結ぶアーキテクチャを実現し、従来数分〜数時間かかっていた特徴量の鮮度を大幅に改善した。Spark Real-Time Mode(RTM)がイベント単位でローリングウィンドウ集計を継続的に更新し、Lakebaseが高頻度な小規模書き込みに最適化されたオンラインストレージとして機能する。同じ特徴量定義をバッチとストリーミングの両方で使い回せるため、不正検知やパーソナライゼーションのようにミリ秒単位の鮮度が求められるユースケースにも対応できる。

## 設計のポイント

- 特徴量を一度定義すればバッチ(オフライン)とストリーミング(オンライン)の両方で同じロジックを再利用できるようにする
- ウォールクロックに揃えたTumbling/Slidingウィンドウではなく、各イベント時刻からミリ秒粒度で遡るRolling Windowを採用し常に最新の集計値を保つ
- Spark RTMでマイクロバッチを待たず行単位でストリームを継続処理し、チェックポイントを償却してステートフルなストリーミング遅延を抑える
- Lakebaseでコンピュートとストレージを分離し、高頻度な小規模upsertの書き込み増幅を抑えて低遅延なオンライン提供を可能にする

## 使いどころ

- 不正検知のように直近数分の取引集計と数十日の行動ベースラインを組み合わせて数百ミリ秒で判定する必要があるモデル
- ユーザーの直近の意図を捉えて即座に反映したいパーソナライゼーション/レコメンデーション
- データサイエンティストがストリーミング専用の集計ロジックや専用インフラを自前で構築せずに鮮度の高い特徴量を使いたい場合
