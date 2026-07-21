---
type: guidance
title: GEMMマイクロベンチマークで見極めるTransformerモデルの低精度(FP8/NVFP4)学習高速化
title_original: How to Optimize Transformer-Based Models for Low-Precision Training
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- low-precision-training
- cost-optimization
components:
- NVIDIA Transformer Engine
- NVIDIA Hopper
- NVIDIA Blackwell
- ESM2-15B
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-to-optimize-transformer-based-models-for-low-precision-training/
published_at: '2026-06-29'
---

## 概要

NVIDIA HopperやBlackwell GPUが対応するFP8・NVFP4などの低精度フォーマットはTransformer学習の中核であるGEMM演算を高速化できるが、実際の高速化幅は量子化オーバーヘッドやカーネル選択の影響で理論値より小さくなる。本記事はモデル構成とバッチサイズから実行される具体的なGEMM形状を導出し、BF16・MXFP8・NVFP4を横断してベンチマークするツールの使い方を、ESM2-15BやCodonFM 5Bを例に解説する。オートキャスト(動的量子化込み)と事前量子化(カーネル単体)の両方を計測することで、量子化オーバーヘッドがどれだけ速度を削っているかを切り分けられる。

## 設計のポイント

- 隠れ層サイズやバッチサイズなどのモデル設定値から実際に実行されるGEMMの行列形状(M×K×N)を導出したうえでベンチマークし、構成ごとの最適な精度の当たりをつける。
- Fprop・Dgrad・Wgradを個別にベンチマークし、行列のアスペクト比によるカーネル選択・速度差の影響を捉える。
- オートキャスト(学習時と同じ動的量子化込み)と事前量子化(カーネル単体の性能)の両モードで計測し、量子化オーバーヘッドの寄与分を切り分ける。
- FP8 DelayedScalingはamax履歴に依存し常にオートキャストでしか動作しないため、事前量子化との比較対象からは除外する。

## 使いどころ

- 大規模Transformerモデルの学習を計画するチームが、本番の学習ジョブを走らせる前にBF16/FP8/NVFP4のどれを採用すべきか事前に見積もりたい場合。
- GPU学習コストを削減したいが、量子化によるオーバーヘッドや効果がGEMMサイズ次第で変わるリスクも把握したいMLインフラ担当者。
- ESM2やCodonFMのような多様なモデル構成に対して、低精度学習の効果が層やGEMMの種類によって異なることを理解したい研究者・エンジニア。
