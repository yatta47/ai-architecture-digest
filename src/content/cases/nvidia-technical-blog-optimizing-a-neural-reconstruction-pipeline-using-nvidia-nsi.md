---
type: guidance
title: Nsight Developer Toolsで神経再構成パイプライン(NuRec)を最適化
title_original: Optimizing a Neural Reconstruction Pipeline Using NVIDIA Nsight Developer Tools
industry: other
cloud:
- on-prem
patterns:
- performance-profiling
- cost-optimization
components:
- NVIDIA Nsight Systems
- NVIDIA Nsight Compute
- NVIDIA Omniverse NuRec
- PyTorch
- NVTX
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/optimizing-a-neural-reconstruction-pipeline-using-nvidia-nsight-developer-tools/
published_at: '2026-07-09'
---

## 概要

Gaussian SplattingベースのNuRecはAV/ロボティクス向けに高精細なシーン再構成を行うが、PyTorch学習ループと専用CUDAカーネルの負荷が大きい。Nsight SystemsとNsight Computeでプロファイリングし、小さなカーネルの融合や不要な同期の除去、レンダーバックワードカーネルの分割によりinterpolate関数を約50倍高速化し、稼働率を15%から30-50%へ改善した。

## 設計のポイント

- NVTXアノテーションでフェーズを可視化し、想定と異なりレンダリングではなく前処理段階(interpolate等)がボトルネックであることを特定する
- 多数の小さなカーネル呼び出しを1つの融合カーネルにまとめ、GPU起動オーバーヘッドとメモリ操作を削減する
- cudaStreamSynchronizeなど不要な同期点を取り除き、CPUがGPUへ小さなカーネルを積み残さないようにする

## 使いどころ

- 自動運転・ロボティクス向けデジタルツイン生成の再構成時間を短縮し開発イテレーションを速めたいチーム
- 大量フレームを生成するRL/合成データ生成ワークロードでGPU時間コストを削減したいチーム
