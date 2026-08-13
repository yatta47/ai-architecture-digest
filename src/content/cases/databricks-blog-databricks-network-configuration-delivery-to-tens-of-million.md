---
type: case
title: Databricksのサーバーレスネットワーク設定配信をイベント駆動事前計算でp99 5秒→75msに
title_original: Databricks network configuration delivery to tens of millions of serverless VMs
ai_relevant: false
company: Databricks
industry: cross-industry
cloud:
- aws
- azure
- gcp
patterns: []
components: []
outcome:
  type: reliability
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/databricks-network-configuration-delivery-tens-millions-serverless-vms
published_at: '2026-08-12'
---

## 概要

Databricksが1日数千万台起動するサーバーレスVMのネットワーク設定配信を、起動時に複数上流サービスへ同期呼び出しする方式からイベント駆動の事前計算＋スナップショットストア方式へ再設計。RPCのp99レイテンシを5,000msから75msへ98.5%削減し、可用性を99.99%まで高めた。
