---
type: guidance
title: KubernetesでGPUをメモリ上限付きで分割共有する
title_original: Memory-Enforced GPU Sharing in Kubernetes with NVIDIA CUDA 13.4
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- unified-runtime
- cost-optimization
- inference-optimization
components:
- NVIDIA CUDA 13.4
- GPU Fractioning Operator
- KAI Scheduler
- NVIDIA GPU Operator
- Multi-Process Service
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/memory-enforced-gpu-sharing-in-kubernetes-with-nvidia-cuda-13-4/
published_at: '2026-10-27'
---

## 概要

CUDA 13.4がアプリに透過なメモリ境界の強制を導入し、GPU Fractioning OperatorとKAI SchedulerでKubernetes上のワークロードごとにGPUメモリ上限を適用できる。小さなAIワークロードがGPU全体を占有する無駄を減らす。

## 設計のポイント

- Podアノテーションでメモリ量・割合・バースト上限・計算モードを宣言し、オペレータがノード側で強制する。
- time-slicingとsm-sharingの計算モードを選べ、最小保証と最大の範囲指定もできる。
- MIGと比べ、ハードウェア分割に頼らずメモリ超過を失敗として扱える。

## 使いどころ

- GPUの遊休容量が多い推論基盤を運用するプラットフォーム担当。
- 複数チームで限られたGPUを共有する社内AI基盤。
