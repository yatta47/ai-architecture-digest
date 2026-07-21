---
type: announcement
title: 'NVIDIA CompileIQ: 進化的アルゴリズムでLLM推論カーネルをコンパイラごとチューニング'
title_original: Extract More Kernel Performance with NVIDIA CompileIQ Auto-Tuning
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- cost-optimization
components:
- NVIDIA CompileIQ
- CUDA 13.3
- PTXAS
- NVCC
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/extract-more-kernel-performance-with-nvidia-compileiq-auto-tuning/
published_at: '2026-06-11'
---

## 概要

LLM推論ではGEMMとAttentionのカーネルだけで計算時間の9割超を占めるため、わずかな性能改善が全体性能に大きく効く。CUDA 13.3に搭載されたNVIDIA CompileIQは、レジスタ割り当てやループ展開などコンパイラ内部の非公開パラメータを進化的・遺伝的アルゴリズムで探索し、ワークロードごとに専用のコンパイラ設定(ACF)を生成することで、既存のデフォルトヒューリスティクスを上回る性能を引き出す。

## 設計のポイント

- ランタイム・コンパイル時間・消費電力を同時に最適化する多目的探索に対応し、Pareto最適なコンパイラ設定群を得られるようにする
- 開発者はベンチマークして評価値を返すobjective関数を定義するだけでよく、探索空間の設定やACFの生成はCompileIQ側が担う
- 生成された設定は再現可能かつ移植可能なACFファイルとして–apply-controlsフラグ経由でコンパイラに適用する

## 使いどころ

- プロファイラ上ではすでにチューニングし尽くしたはずのLLM推論カーネルから、さらに性能を絞り出したいチーム
- CUDA/Triton/Helionなど自作カーネルの各ワークロード専用のコンパイラチューニングを自動化したいパフォーマンスエンジニア
