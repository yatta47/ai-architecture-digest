---
type: announcement
title: Unity Catalogメトリクスビューを Power BI に公開
title_original: 'Unity Catalog metric views now in Power BI: one unified, governed semantic layer for all your reporting'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- context-engineering
- business-intelligence-resilience
components:
- Unity Catalog
- Power BI
- Databricks Genie
- AI/BI Dashboards
- Lakeflow Jobs
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/unity-catalog-metric-views-now-power-bi-one-unified-governed-semantic-layer-all-your-reporting
published_at: '2026-11-10'
---

## 概要

Unity Catalogのメトリクスビューを、Catalog ExplorerやLakeflow JobのPower BIタスクからPower BIセマンティックモデルとして公開できるようになった。指標を一度定義すればPower BI、AI/BIダッシュボード、Genieで同じ数値が得られ、DirectQueryでアクセス制御も維持される。

## 設計のポイント

- 指標定義をLakehouse側の1か所に置き、各BIで再利用する。
- Power BIタスクで、メトリクスビューの変更を追随させる。
- DirectQueryでUnity Catalogの権限を維持する。

## 使いどころ

- 部門ごとに指標が食い違う組織。
- AIとBIの回答を揃えたい場面。
