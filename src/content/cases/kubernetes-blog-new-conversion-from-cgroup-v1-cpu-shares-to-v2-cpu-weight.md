---
type: announcement
title: cgroup v1 CPUシェアからv2 CPUウェイトへの新しい変換式
title_original: New Conversion from cgroup v1 CPU Shares to v2 CPU Weight
ai_relevant: false
company: Red Hat
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/01/30/new-cgroup-v1-to-v2-cpu-conversion-formula/
published_at: '2026-01-30'
---

## 概要

Kubernetesがcgroup v1からv2へ移行する際に使われていた線形の変換式には、Kubernetes以外のプロセスに対する優先度低下と、サブcgroup向けの粒度不足という2つの問題があった。Red Hatのエンジニアが提案した二次関数ベースの新しい変換式により、1CPU要求時のweightがデフォルト値100に近い102となり優先度の整合性が改善し、細かいCPU要求でも粒度を確保できるようになった。この新方式はKubernetes本体ではなくOCIランタイム層(runc 1.3.2、crun 1.23以降)で実装されている。
