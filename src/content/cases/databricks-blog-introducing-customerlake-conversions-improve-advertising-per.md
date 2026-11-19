---
type: announcement
title: CustomerLake Conversionsが顧客価値の信号を広告媒体へ送る
title_original: Introducing CustomerLake Conversions
company: Databricks
industry: media
cloud:
- multi-cloud
patterns:
- ai-agent
- decision-execution
components:
- CustomerLake Campaign Agents
- Unity Catalog
- Conversions API
- Lakeflow Connect
outcome:
  type: revenue
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/customerlake-conversions
published_at: '2026-11-19'
---

## 概要

DatabricksのAgentic CDPにCustomerLake Conversionsが加わった。予測LTVなど自社データから作った価値ベースのコンバージョン信号を、CAPI経由で広告媒体へ送り、成果をUnity Catalogへ戻して一元管理する。

## 設計のポイント

- コンバージョンの数でなく、予測LTVなどの価値で信号を作って広告に送る。
- 配信と計測の結果をUnity Catalogに戻し、権限委譲と監査証跡を一箇所に持つ。

## 使いどころ

- 割引だけの初回購入と優良顧客の購入を区別して広告運用したい企業。
- 複数の広告媒体にまたがる計測を統制したいブランドや代理店。
