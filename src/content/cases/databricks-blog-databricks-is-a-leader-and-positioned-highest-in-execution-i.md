---
type: opinion
title: DatabricksがGartner MQで評価され、AIでレイクハウスとlakebaseが統合されると主張
title_original: Databricks is a Leader and positioned highest in execution in the 2026 Gartner Magic Quadrant for Data Lakehouse
  Platforms
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- unified-transactional-analytical-storage
components:
- Databricks Lakehouse
- Lakebase Postgres
- Unity Catalog
- Genie
- Delta Lake
- Apache Iceberg
outcome:
  type: revenue
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/databricks-leader-and-positioned-highest-execution-2026-gartnerr-magic-quadranttm-data
published_at: '2026-11-14'
---

## 概要

Databricksは、データレイクハウス部門のGartner MQでLeaderとなったと報告し、エージェントが運用データと分析文脈を同時に必要とすることから、レイクにデータを置くトランザクションDB(lakebase)が重要になると主張する。

## 設計のポイント

- オープン形式でレイクに置いたデータを、複数エンジンから使えるようにする
- 運用と分析の間のパイプラインによる遅延・コピー・統治の分断を減らす
- エージェントが必要に応じてDBを作成・破棄できる前提で設計する

## 使いどころ

- エージェントが運用データを読み書きするアプリ基盤の検討
- 分析基盤とOLTPの統合を検討する場面
