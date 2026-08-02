---
type: guidance
title: OPC UAテレメトリをAzure Data Explorerでリアルタイム分析する基盤構成
title_original: Connect Azure Data Explorer to the reference solution
ai_relevant: false
industry: manufacturing
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/iot/how-to-connect-azure-data-explorer-to-solution
published_at: '2026-07-30'
---

## 概要

毎秒数百万イベント規模のOPC UAテレメトリをAzure Data Explorerに取り込み、KQLで状態監視やOEE計算、異常検知を行うリファレンス構成を示す。I3X APIによるBasic認証保護や、サンプルダッシュボードによるISA-95資産階層の可視化も含む。
