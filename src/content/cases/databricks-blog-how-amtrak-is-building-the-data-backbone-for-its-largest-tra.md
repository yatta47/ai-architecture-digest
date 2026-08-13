---
type: case
title: AmtrakがDatabricksで全社的な鉄道インテリジェンス基盤『Rail Intelligence』を構築
title_original: How Amtrak is building the data backbone for its largest transformation in over 50 years
company: Amtrak
industry: logistics
cloud: []
patterns:
- data-federation
- ai-agent
components:
- Databricks
- Lakeflow Connect
- Delta Lake
- Unity Catalog
- MLflow
- Databricks Model Serving
- Genie
- Databricks Apps
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-amtrak-building-data-backbone-its-largest-transformation-over-50-years
published_at: '2026-08-12'
---

## 概要

全米最大の旅客鉄道網を持つAmtrakが、車両テレメトリ・予約システム・保守データなどサイロ化していたデータをDatabricks上の単一ガバナンス層『Rail Intelligence』に統合。Unity Catalogによるガバナンスとレイクハウス上のML異常検知・遅延確率スコアリングにより、故障の事後対応から予兆保全への転換を進めている。

## 設計のポイント

- Lakeflow Connectとストリーミングで車両IoT・分岐器検知器・予約系・運行系などのシグナルを単一の統治された環境に集約する
- 生イベントをDelta Lakeに取り込みメダリオンアーキテクチャで整形し、Unity Catalogでリネージとドメインアクセス制御・品質契約を管理する
- MLflowとModel Servingで異常検知・コンピュータビジョンによる欠陥検出・遅延確率スコアリングを運用し、車両健全性から要員配置まで一つの意思決定基盤にまとめる

## 使いどころ

- 複数の新型車両導入と大規模改修を同時に進める中で、サイロ化したデータを統合基盤に載せたい交通インフラ事業者
- 設備の事後対応から予兆保全（predictive maintenance）へ転換したい鉄道・重工業のメンテナンスチーム
