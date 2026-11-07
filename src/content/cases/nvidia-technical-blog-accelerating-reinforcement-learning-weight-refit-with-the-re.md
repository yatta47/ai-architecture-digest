---
type: guidance
title: RL後学習の重み同期をReshardコレクティブで高速化
title_original: Accelerating Reinforcement Learning Weight Refit with the Reshard Collective
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- reinforcement-learning
- inference-optimization
components:
- NCCL M2N Reshard
- NeMo RL
- PyTorch DTensor
- DGX GB200
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/accelerating-reinforcement-learning-weight-refit-with-the-reshard-collective/
published_at: '2026-11-06'
---

## 概要

RL後学習で学習GPUから推論GPUへ重みを送るrefitを、DTensor間のリシャードとして再定式化し最小限のデータ転送にするNCCL M2N Reshardを紹介。NeMo RLのベンチマークで従来のgather-broadcastに対し2.7〜5.7倍高速化した。

## 設計のポイント

- 並列構成の違う学習側と推論側の転送をDTensorのレイアウト変換として抽象化する。
- シャードの交差を厳密に求め、NVLinkドメイン内のレプリカをまとめて冗長転送を排除する。
- 主要な重みだけReshardを使い、小さい重みは従来方式を残すハイブリッドで互換性を保つ。

## 使いどころ

- 数千億〜兆パラメータ級モデルを学習・推論分離構成でRL後学習する基盤。
- refitが学習ステップのボトルネックになっているRLパイプライン。
