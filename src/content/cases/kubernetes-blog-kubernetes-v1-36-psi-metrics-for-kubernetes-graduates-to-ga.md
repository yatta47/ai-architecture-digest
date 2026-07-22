---
type: announcement
title: Kubernetes PSI(Pressure Stall Information)メトリクスがGAへ、リソース逼迫の早期検知を標準化
title_original: 'Kubernetes v1.36: PSI Metrics for Kubernetes Graduates to GA'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/05/12/kubernetes-v1-36-psi-metrics-ga/
published_at: '2026-05-12'
---

## 概要

Linuxカーネルの機能であるPressure Stall Information(PSI)を、ノード/Pod/コンテナ単位で観測できる安定インターフェースとしてKubernetes v1.36でGAに到達させた。CPU使用率だけでは見えないタスクの停滞を10秒/60秒/300秒の移動平均で可視化し、80 Pod規模の高密度クラスタでもKubeletとカーネル双方のオーバーヘッドが数%以内に収まることを性能検証で確認、/metrics/cadvisorやSummary API経由で取得できる。
