---
type: announcement
title: NVIDIA AICRに実行時のAI部品表（AIBOM）を追加
title_original: Validating GPU Platforms with Runtime AI Inventory via the NVIDIA DSX AI Factory
company: NVIDIA
industry: cross-industry
cloud:
- gcp
patterns:
- gpu-fleet-reliability
- policy-as-code
components:
- NVIDIA AI Cluster Runtime
- k8s-aibom
- CycloneDX
- GKE
- vLLM
outcome:
  type: risk-compliance
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/validating-gpu-platforms-with-runtime-ai-inventory-via-the-nvidia-dsx-ai-factory/
published_at: '2026-11-10'
---

## 概要

NVIDIA AI Cluster Runtimeに、k8s-aibomによる実行時のAI部品表が加わった。Kubernetes上のAIワークロードを観測しCycloneDX 1.6形式で記録する。検証ではAPIサーバー要求は毎分約4回、平均CPU 2.2ミリコアで、負荷は小さい。

## 設計のポイント

- 名前空間単位のオプトインで記録対象を制御する。
- 信頼度階層と証跡の位置を付けて記録する。
- 推論ランタイムやモデル、イメージ情報を自動分類する。

## 使いどころ

- GPU基盤上のAI資産を棚卸ししたい運用チーム。
- 監査向けにAIワークロードを追跡する場面。
