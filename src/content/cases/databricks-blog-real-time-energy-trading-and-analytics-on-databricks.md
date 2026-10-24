---
type: case
title: Databricks上でエネルギー取引の運用系と分析系を統合する構成
title_original: Real-time energy trading and analytics on Databricks
company: Databricks
industry: other
cloud: []
patterns:
- unified-transactional-analytical-storage
- event-driven
- decision-execution
components:
- Spark Structured Streaming Real-Time Mode
- Lakebase
- Databricks Apps
- Unity Catalog
- MLflow
- Databricks Model Serving
- Genie One
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/real-time-energy-trading-and-analytics-databricks
published_at: '2026-10-23'
---

## 概要

エネルギー取引で運用系と分析系を分けると、リスクデータの鮮度低下やガバナンスの二重化が起きる。Databricksは、Real-Time ModeでLakebaseに市場データを流し、取引アプリ、MLモデル、ダッシュボード、Genie Oneが同じデータを参照する構成を示す。権限・リネージ・監査はUnity Catalogで一元化する。

## 設計のポイント

- 各コンポーネントが独自のコピーを持たず、Lakebaseとレイクハウスの単一の取り込み経路を共有する。
- MLflowとModel Servingで学習から配信までを同じガバナンス下に置き、モデルの出力を取引アプリに表示する。
- 夜間バッチのリスク計算をリアルタイムのリスクアラートに置き換える。

## 使いどころ

- 15分刻み取引への移行で、リスク計算の鮮度を上げたいエネルギー取引部門。
- 運用DBと分析基盤の同期パイプラインを減らしたいチーム。
