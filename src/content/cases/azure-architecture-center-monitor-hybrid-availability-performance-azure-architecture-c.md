---
type: guidance
title: Azure Monitorによるハイブリッド環境の可用性・パフォーマンス監視
title_original: Hybrid availability and performance monitoring
ai_relevant: false
industry: cross-industry
cloud:
- azure
- on-prem
- multi-cloud
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/hybrid/hybrid-perf-monitoring
published_at: '2026-05-04'
---

## 概要

本社オンプレミス、支社、サードパーティクラウドにまたがるVM群にLog AnalyticsエージェントとDependencyエージェントを配置し、Log Analyticsゲートウェイ等を経由して中央のLog Analyticsワークスペースに集約するハイブリッド監視構成を示す。インターネット非接続のVMも含めてOS/アプリの可用性とパフォーマンスを一元監視する。
