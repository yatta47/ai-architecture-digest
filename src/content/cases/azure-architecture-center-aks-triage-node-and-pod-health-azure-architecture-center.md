---
type: guidance
title: AKSワーカーノードとPodの健全性トリアージ手順
title_original: Examine node and pod health
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/operator-guides/aks/aks-triage-node-health
published_at: '2026-07-20'
---

## 概要

Azure Kubernetes Service (AKS) のクラスタ診断シリーズの一環として、ワーカーノードとPodの健全性を確認する6つの手順を解説する記事。ノード不良の主因（制御プレーンとの通信断、リソース逼迫、DNS解決失敗)を挙げ、AKS Diagnose and Solve Problems、Azure Copilot for AKS、Kubernetesイベント、Azure Monitorコンテナ正常性ビュー、Prometheus/Grafanaなど複数の切り分け手段を紹介している。
