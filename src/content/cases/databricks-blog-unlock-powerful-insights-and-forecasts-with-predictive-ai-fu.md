---
type: announcement
title: SQLだけで予測・異常検知ができるDatabricksの予測AI関数
title_original: Unlock powerful insights and forecasts with Predictive AI Functions
company: Databricks
industry: cross-industry
cloud: []
patterns:
- text-to-sql
- business-intelligence-resilience
components:
- Databricks
- ai_forecast
- ai_top_drivers
- ai_detect_anomalies
- ai_predict_value
- ai_predict_class
- Genie
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/unlock-powerful-insights-and-forecasts-predictive-ai-functions
published_at: '2026-10-14'
---

## 概要

Databricksは予測系AI関数5種（ai_forecast、ai_top_drivers、ai_detect_anomalies、ai_predict_value、ai_predict_class）をベータ公開した。SQL・Genie・ダッシュボードから使え、モデルは基盤側で一元管理される。ai_forecastは時系列基盤モデルを採用している。

## 設計のポイント

- モデル構築・運用をデータ基盤側に持たせ、分析者はSQL関数で呼ぶ
- Genieの自然言語やダッシュボードにも同じ関数を組み込む
- 時系列基盤モデルでチューニング不要にする

## 使いどころ

- データサイエンスチームの待ち行列なしに予測や異常検知を行いたい業務分析者
