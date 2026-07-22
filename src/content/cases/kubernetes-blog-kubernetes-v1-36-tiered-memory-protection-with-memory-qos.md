---
type: announcement
title: Kubernetesの階層型メモリ保護『Memory QoS』アップデート
title_original: 'Kubernetes v1.36: Tiered Memory Protection with Memory QoS'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/04/29/kubernetes-v1-36-memory-qos-tiered-protection/
published_at: '2026-04-29'
---

## 概要

Kubernetes v1.36でMemory QoS機能(アルファ)を拡張し、memoryReservationPolicyによってメモリスロットリング(memory.high)と予約(memory.min/low)を分離。QoSクラスに応じてGuaranteed Podはハード予約、Burstable Podはソフト保護という階層型のメモリ保護を実現し、可観測性メトリクスやカーネルバージョン警告も追加した。
