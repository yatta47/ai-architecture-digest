---
type: announcement
title: GPUクラスタ構成を再現可能にするNVIDIA AICR v1.0
title_original: 'AICR v1.0: Open, stable, and verifiable GPU cluster configuration'
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
- multi-cloud
patterns:
- gpu-fleet-reliability
- policy-as-code
- ci-cd
components:
- NVIDIA AI Cluster Runtime
- Kubernetes
- Helm
- Argo CD
- Flux
- Helmfile
- Pulumi
- k0rdent
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/aicr-v1-0-open-stable-and-verifiable-gpu-cluster-configuration/
published_at: '2026-10-06'
---

## 概要

GPU搭載Kubernetesクラスタ向けに、互換性が検証済みのコンポーネント組み合わせを固定した「レシピ」を提供するAICRのv1.0リリース。Snapshot/Recipe/Bundle/Validationの4機能とCLI・API等の安定契約を定め、署名付き検証証跡を伴う。

## 設計のポイント

- ドライバ・OS・Kubernetes等のバージョン組み合わせをレシピとして固定し、構成差異による障害を減らす。
- 観測状態・望ましい構成・配布成果物・検証を独立機能に分け、Helm/Argo CD/Flux等に出力する。
- 署名付きの検証証跡でコミュニティ提供レシピの信頼性を担保する。

## 使いどころ

- 複数世代のGPUとKubernetesを運用するAI基盤チーム。
- IaCツールからGPUクラスタ構成を再利用したい統合ベンダー。
