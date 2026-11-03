---
type: guidance
title: NVIDIA AICR：Vera Rubin向けKubernetes構成をレシピ化して初日から検証
title_original: Making Kubernetes AI-Ready for NVIDIA Vera Rubin on Day One
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- inference-optimization
- policy-as-code
components:
- NVIDIA AI Cluster Runtime
- GPU Operator
- DRA driver
- Dynamo
- NCCL
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/making-kubernetes-ai-ready-for-nvidia-vera-rubin-on-day-one/
published_at: '2026-10-30'
---

## 概要

NVIDIA AICRは調整済みの構成を再利用可能なレシピとして保存し、デプロイバンドル生成とクラスタ検証を行う。Vera Rubin NVL72向けレシピはドライバ・カーネル等を規定し、NCCL all-reduceで744.71 GB/sを達成。早期検証でDRAドライバのクラッシュも発見・修正された。

## 設計のポイント

- 検証済み構成をレシピとして宣言管理し再現性を確保
- デプロイ・適合性・性能ゲートまで一貫して検証し署名付き証跡を残す
- 新ハードの早期検証で上流不具合を先に発見する

## 使いどころ

- 新世代GPUクラスタの立ち上げを短縮したい基盤チーム
- 学習用と推論用の構成を標準化したい組織
