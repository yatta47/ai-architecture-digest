---
type: case
title: Jane StreetがcuTileでMamba-2の順伝播カーネルを最適化した事例
title_original: Accelerating Mamba-2 with High-Performance Forward Pass Kernels in NVIDIA CUDA Tile
company: Jane Street
industry: financial-services
cloud:
- on-prem
patterns:
- inference-optimization
components:
- NVIDIA CUDA Tile (cuTile)
- Mamba-2
- Tensor Core
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/accelerating-mamba-2-with-high-performance-forward-pass-kernels-in-nvidia-cuda-tile/
published_at: '2026-10-19'
---

## 概要

Jane Streetの機械学習エンジニアがNVIDIAと協力し、PythonベースのDSLであるcuTileで状態空間モデルMamba-2の順伝播用カーネル3つを最適化した。chunk_cumsum、fwd_pass_state、compute_outを実装し、Tensor Coreを活用している。

## 設計のポイント

- タイル単位の高水準プリミティブでスレッド・ワープの制御を隠し、Pythonからカーネルを書く。
- compute_outは複数の項を1つのタイルカーネルに融合し、中間行列をレジスタに保持してTF32で実行する。
- DRAMのレイテンシヒント、オペランド入替、TMA向けの転置レイアウトで最適化する。
- 入力シェイプごとにブロックサイズと占有率を探索するオートチューナーを使う。

## 使いどころ

- 系列モデルを自前の高速カーネルで動かしたい研究・量的分析チーム。
- CUDAを直接書かずにGPUカーネルを開発したい場面。
- Mamba系モデルの学習・推論を高速化したい場面。
