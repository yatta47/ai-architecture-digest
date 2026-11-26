---
type: case
title: MuleSoftの監視基盤を39PB移行しつつ約3,000クラスタから24へ集約
title_original: How MuleSoft Rebuilt a Live Observability Platform While Migrating 39 Petabytes of Customer Data
ai_relevant: false
company: Salesforce
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: cost
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-mulesoft-rebuilt-a-live-observability-platform-while-migrating-39-petabytes-of-customer-data/
published_at: '2026-11-25'
---

## 概要

MuleSoftは監視を稼働させたまま、単一テナント構成をHyperforce上のマルチテナント可観測性基盤へ再構築した。OpenTelemetryでの標準化と変換レイヤーによる既存API互換を保ちつつ、クラスタを約3,000から24に、コンポーネントを153から43に削減した。
