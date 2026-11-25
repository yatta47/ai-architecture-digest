---
type: guidance
title: Agentic CDP向け顧客データモデリング：ID解決と階層データ基盤の設計
title_original: 'Data modeling best practices for an Agentic CDP, Part 1: The data foundation'
company: Databricks
industry: retail
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- CustomerLake
- Unity Catalog
- Lakeflow Connect
- Zerobus Ingest
- Spark Declarative Pipelines
- Lakeflow Jobs
- Genie
- OpenSharing
outcome:
  type: revenue
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/agentic-cdp-data-modeling-data-foundation
published_at: '2026-11-24'
---

## 概要

エージェントが顧客一人ごとに秒単位で判断するCDPに向け、bronze/silver/goldの階層とID解決を軸にしたデータモデル設計を解説する。同意・抑止ルールや施策の反応もデータとして持つ。

## 設計のポイント

- ID解決はsilverの後の1か所で行い、永続的なcanonical_idをgold層の結合キーにする。
- ID突合は決定的ルールを先に適用し、残りを確率的に補う。誤統合を避けて精度を優先し、人がレビューする。
- 同意や抑止などのルールをデータとして保存し、エージェントが行動前に確認する。
- 反応と成果をホールドアウト付きで書き戻し、効果測定の閉ループを作る。

## 使いどころ

- エージェント活用を見据えて顧客データ基盤を設計するデータアーキテクト。
- 自社でIDグラフを所有したいマーケティング組織。
