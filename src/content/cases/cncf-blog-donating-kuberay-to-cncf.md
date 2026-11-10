---
type: announcement
title: KubeRayのCNCF寄贈とPARKスタック
title_original: Donating KubeRay to CNCF
company: KubeRay
industry: cross-industry
cloud:
- multi-cloud
patterns:
- unified-runtime
- llmops
components:
- KubeRay
- Ray
- Kubernetes
- PyTorch
- Ray Serve
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/11/10/donating-kuberay-to-cncf/
published_at: '2026-11-10'
---

## 概要

KubeRayがCNCFに寄贈され、PyTorch・Ray・Kubernetesを含むPARKスタックがLinux Foundation傘下に揃った。RayCluster、RayJob、RayServiceの3つのCRDで学習、バッチ、オンライン推論を運用する。

## 設計のポイント

- 用途別CRDでクラスタ、ジョブ、推論サービスを分離する。
- RayServiceでゼロダウンタイム更新とフェイルオーバーを行う。

## 使いどころ

- Kubernetes上の分散学習・RL基盤
- オンライン推論の高可用運用
