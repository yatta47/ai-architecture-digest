---
type: case
title: Feature Viewsで学習と推論の特徴量を統一したリアルタイム次善オファー推薦
title_original: Build a Real-Time Next-Best-Offer Recommender Using Databricks Feature Views
company: Databricks
industry: financial-services
cloud: []
patterns:
- generative-recommendation
- realtime-feature-serving
- inference-optimization
components:
- Databricks Feature Views
- Kafka
- Delta
- Unity Catalog
- Model Serving
- Feature Serving
- LightGBM
- MLflow
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/build-real-time-next-best-offer-recommender-using-databricks-feature-views
published_at: '2026-11-16'
---

## 概要

Databricks は Feature Views で特徴量を一度定義して学習とオンライン推論の両方に使い、リテール銀行向けのリアルタイム次善オファー推薦を構築するソリューションアクセラレータを公開した。バッチ特徴量とKafkaストリーム由来のセッション内意図を LightGBM ランカーに入力し、p95で約34msの応答を実現した。ストリーミングイベントは約0.1秒でモデルから参照可能になる。

## 設計のポイント

- 特徴量を1回宣言して学習とサービングで共有し、train/serve skew と重複ロジックを排除した。
- point-in-time 結合で学習時の未来データ漏洩を防いだ。
- ストリーム特徴量は Kafka トピックを指定するだけでオンラインストアに継続集計し、手書きのストリーミングジョブを不要にした。
- SawtoothWindow で長期ウィンドウの鮮度を保ちつつ全履歴の再計算を避けた。

## 使いどころ

- 金融などでセッション中にオファーを出したいパーソナライゼーションチーム。
- バッチとストリームで特徴量定義が二重化している ML 基盤。
- 低遅延の推薦サービングを短期間で立ち上げたい場面。
