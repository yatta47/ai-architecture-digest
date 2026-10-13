---
type: announcement
title: NVIDIA Run:aiのオープンソース化(DSX AI Factory)
title_original: NVIDIA Run:ai Is Now Open Source as Part of NVIDIA DSX AI Factory Platform
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- inference-optimization
components:
- NVIDIA Run:ai
- KAI Scheduler
- Kubernetes
- NVIDIA NGC
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-runai-is-now-open-source-as-part-of-nvidia-dsx-ai-factory-platform/
published_at: '2026-10-13'
---

## 概要

NVIDIAはAIワークロードとGPUのオーケストレーション基盤Run:ai全体をオープンソース化した。KAI Scheduler、GPU Fractioning Operator、KAI Resource Management、Workload Mapの4部品は個別にも採用できる。

## 設計のポイント

- GPU認識のKubernetesスケジューリングと、CUDAネイティブなGPU分割共有で稼働率を上げる。
- 組織・クォータ階層管理を部品として分離している。
- モデルロード高速化(Model Streamer)やマルチコンポーネント推論(Grove)と組み合わせられる。

## 使いどころ

- 共有GPUクラスタを運用するプラットフォームチームやAIクラウド事業者。
- GPU利用率の向上を図りたい場面。
