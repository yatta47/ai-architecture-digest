---
type: guidance
title: Azure Managed GrafanaでOEEやエネルギー消費をリアルタイム可視化・アラート化する
title_original: Connect Azure Managed Grafana to the reference solution
ai_relevant: false
industry: manufacturing
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/iot/how-to-connect-grafana-to-solution
published_at: '2026-07-30'
---

## 概要

Azure Managed GrafanaをAzure Data Explorerに接続し、マネージドIDによる認証でOEEや不良品数、エネルギー消費などをリアルタイムダッシュボード化する手順を示す。低OEEのしきい値超過を検知するアラートルールも設定し、異常の早期把握を支援する。
