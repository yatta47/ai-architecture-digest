---
type: opinion
title: Kubernetesのハードウェア管理を刷新するDynamic Resource Allocation(DRA)開発の舞台裏
title_original: Spotlight on WG Device Management
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/06/24/wg-device-management-spotlight-2026/
published_at: '2026-06-24'
---

## 概要

KubernetesのDevice Management Working Group共同議長3名(NVIDIA・Intel・Google所属)へのインタビュー記事。GPU/TPU等のアクセラレータを単純な整数としてしか扱えない従来のDevice Plugin APIの限界を踏まえ、モデリング・リクエスト・スケジューリング・アクチュエーションの4段階からなるDynamic Resource Allocation(DRA)を設計し、Kubernetes 1.34でGA(正式版)に到達させた経緯と背景を語っている。ワーキンググループの成り立ちや、ResourceSlice/ResourceClaim等のAPI設計思想についても触れている。
