---
type: case
title: エアギャップ工場のデータをIceberg＋Unity Catalogで顧客に安全公開
title_original: 'Air-gapped, not data-dark: How Bright Machines gives customers live factory dashboards without opening inbound
  access'
ai_relevant: false
company: Bright Machines
industry: manufacturing
cloud:
- aws
patterns: []
components: []
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/air-gapped-not-data-dark-how-bright-machines-gives-customers-live-factory-dashboards-without
published_at: '2026-11-11'
---

## 概要

Bright Machinesは、エアギャップの工場からDebeziumでPostgreSQLの変更を取得してIcebergで出力し、単一の外向き経路で送出、Unity Catalog連携でDatabricksから直接参照する構成に移行した。9サービスのパイプラインが1つのガバナンス基盤になり、書込みから1〜2分で照会でき、最初の顧客向けダッシュボードは約2か月で公開された。
