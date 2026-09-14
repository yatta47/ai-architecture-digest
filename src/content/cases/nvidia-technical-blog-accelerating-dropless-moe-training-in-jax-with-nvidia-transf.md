---
type: case
title: JAXでのDropless MoE学習をNVIDIA Transformer Engineで10倍高速化
title_original: Accelerating Dropless MoE Training in JAX with NVIDIA Transformer Engine
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- gpu-fleet-reliability
components:
- NVIDIA Transformer Engine
- JAX
- NVIDIA GB200
- NVIDIA GB300 NVL72
- NCCL EP
- XLA
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/accelerating-dropless-moe-training-in-jax-with-nvidia-transformer-engine/
published_at: '2026-09-14'
---

## 概要

NVIDIA Transformer EngineをJAXと組み合わせ、Mixture of Experts（MoE）の学習でトークンを一切ドロップしないDropless MoEを実用的な速度で実現した。DeepSeek-V3の学習でGPUあたり103TFLOPSから1,068TFLOPSへと10.4倍のスループット改善を達成し、GB300 NVL72上の1,024GPU構成でも97%のスケーリング効率を維持した。

## 設計のポイント

- 各エキスパートが受け取るトークン数が不揃いな『ラギッドテンソル』をパディングやドロップなしで扱うグループGEMMカーネルを使う
- エキスパート並列のdispatch/combineをNCCL EPで融合しトークン重複除去することで通信量を削減する
- デバイス-ホスト間コピーを避け、CUDAグラフを維持できるようトークン数の形状をCPU非依存で扱う
- JAXのホストオフロードとXLAマルチストリーミングでNVLink/InfiniBand間の通信をオーバーラップさせる

## 使いどころ

- 大規模MoEモデル（DeepSeek/Qwen/Mixtral系）を自前で学習し品質と学習効率を両立させたいチーム
- エキスパート並列時の通信オーバーヘッドがボトルネックになっている大規模GPUクラスタ
- トークンドロップによる品質劣化を避けつつ学習コストを抑えたい場合
