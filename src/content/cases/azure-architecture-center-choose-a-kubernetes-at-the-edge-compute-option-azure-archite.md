---
type: guidance
title: エッジ向けKubernetesの選択肢（ベアメタル/Stack Edge/AKSハイブリッド/Edge Essentials）をコスト・柔軟性で比較
title_original: Choose a Kubernetes at the edge compute option
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/operator-guides/aks/choose-kubernetes-edge-compute-option
published_at: '2026-06-22'
---

## 概要

エッジにコンピュートを拡張するためのKubernetesの選択肢として、ベアメタルKubernetes、Azure Stack Edge Pro上のKubernetes、AKSハイブリッド、AKS Edge Essentialsの4つを、運用コスト・構成の容易さ・柔軟性・混在ノード対応の観点で比較する。既存インフラの制約が強くマネージドサービスが使えない場合はベアメタルが適し、低運用でLinux中心のIoT/機械学習ワークロードにはAzure Stack Edge Proが適するなど、シナリオ別に最適な選択肢を整理している。
