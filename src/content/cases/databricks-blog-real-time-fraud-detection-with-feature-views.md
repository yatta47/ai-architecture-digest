---
type: case
title: Feature Viewsで学習とリアルタイム推論の特徴量定義を一本化した不正検知
title_original: Real-time fraud detection with Feature Views
company: Databricks
industry: financial-services
cloud: []
patterns:
- unified-runtime
- event-driven
components:
- Databricks Feature Store
- Feature Views
- Lakebase
- Unity Catalog
- Kafka
- Databricks Apps
- Model Serving
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/real-time-fraud-detection-feature-views
published_at: '2026-11-05'
---

## 概要

Databricks Feature Viewsで特徴量を一度定義し、学習用のポイントインタイム整合データとオンライン推論用の管理パイプラインの両方に使う不正検知の構成を示す。ローリングウィンドウ、30日ベースライン、オンデマンド特徴量を組み合わせる。

## 設計のポイント

- 同一定義から学習データとオンライン特徴量を生成し、学習・推論のスキューとデータリークを防ぐ。
- 直近の連続決済、通常の支出傾向、現在の決済との比較という3種類の特徴量を使う。
- materialize_features()でLakebase上のオンラインストアへストリーミングパイプラインを作り、鮮度を200ms未満にする。

## 使いどころ

- 学習と本番で特徴量ロジックが二重管理されている不正検知チーム。
- ストリーミング特徴量を扱うMLプラットフォーム。
