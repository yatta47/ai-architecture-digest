---
type: guidance
title: 'BEVPoolV3: Physical AI向けBEVプーリングのGPU高速化'
title_original: Accelerating BEV Pooling on NVIDIA GPUs for Physical AI Applications
industry: other
cloud:
- on-prem
patterns:
- inference-optimization
- physical-ai
components:
- BEVPoolV3
- NVIDIA RTX A6000
- NVIDIA RTX PRO 6000 Blackwell
- NVIDIA Nsight Compute
- NVIDIA TensorRT
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/accelerating-bev-pooling-on-nvidia-gpus-for-physical-ai-applications/
published_at: '2026-07-09'
---

## 概要

自動運転やロボティクスのBird's-Eye-View知覚では、複数カメラの特徴量をdepthで重み付けしてBEVグリッドへscatter-reduceするBEVプーリングがレイテンシのボトルネックになりやすい。BEVPoolV3は重複ロード削減・5配列INT32スキャッタマップ・事前計算インデックス・区間所有出力書き込みという4つの改善で、DRAM-boundパスで最大22倍、L2常駐パスで最大42倍の高速化を実現した。

## 設計のポイント

- 作業セットがGPUのL2キャッシュに収まるかどうかで最適化方針(DRAM-boundかL2-residentか)を分岐させる
- ランタイムの整数除算を事前計算したインデックスに置き換え、重複するdepthロードを削減してスキャッタトラフィックを減らす
- Nsight Computeでボトルネックを実測検証しながら、GPUアーキテクチャごとにカーネル実装をマッピングし直す

## 使いどころ

- マルチカメラ知覚モデルをエッジGPUでリアルタイム実行したい自動運転・ロボティクス開発者
- 同種のgather/scatter系カーネルの最適化ワークフローを汎用的に確立したいGPUエンジニア
