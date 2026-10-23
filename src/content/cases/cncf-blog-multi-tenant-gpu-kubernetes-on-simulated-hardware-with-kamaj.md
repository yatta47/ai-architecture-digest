---
type: guidance
title: KamajiとHAMiで実現するマルチテナントGPU Kubernetes(模擬ハードウェアで検証)
title_original: Multi-Tenant GPU Kubernetes on Simulated Hardware with Kamaji and HAMi
ai_relevant: false
industry: cross-industry
cloud:
- on-prem
patterns: []
components: []
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/10/23/multi-tenant-gpu-kubernetes-on-simulated-hardware-with-kamaji-and-hami/
published_at: '2026-10-23'
---

## 概要

テナントごとのコントロールプレーンをPodとして動かすKamajiと、GPUを分割して割り当てるHAMiを組み合わせ、物理GPUなしの単一マシン上でマルチテナントGPUクラスタを再現した記事。テナント隔離とフラクショナルGPUスケジューリングを検証している。
