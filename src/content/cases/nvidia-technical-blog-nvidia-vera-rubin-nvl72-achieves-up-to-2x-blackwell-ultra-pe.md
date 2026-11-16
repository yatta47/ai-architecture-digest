---
type: announcement
title: MLPerf Training v6.1でVera Rubin NVL72が6/7ベンチマークの最速を記録
title_original: NVIDIA Vera Rubin NVL72 Achieves up to 2x Blackwell Ultra Performance in MLPerf Training v6.1
company: NVIDIA
industry: cross-industry
cloud:
- multi-cloud
patterns:
- reinforcement-learning
- inference-optimization
components:
- NVIDIA Vera Rubin NVL72
- NVIDIA GB300 NVL72
- NVLink 6
- ConnectX-9
- TensorRT-LLM
- vLLM
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-achieves-up-to-2x-blackwell-ultra-performance-in-mlperf-training-v6-1/
published_at: '2026-11-16'
---

## 概要

Vera Rubin NVL72は初参加のMLPerf Training v6.1で7中6ベンチマークの最速を記録し、GB300比で最大2倍の性能を示した。DeepSeek-V3での256→1,024 GPUのスケーリング効率は97%超で、GRPOの強化学習ベンチマークも含む。

## 設計のポイント

- NVLink 6とSuperNICによる高帯域で、スケール時の効率97%超を維持する
- 強化学習後訓練ベンチマークをTensorRT-LLMとvLLMの双方で提出し、ソフトウェア成熟度を示す
- 最適化済みGB300と新世代を併せて評価する

## 使いどころ

- 大規模学習クラスタの調達検討
- RL後訓練を含むトレーニング基盤の性能比較
