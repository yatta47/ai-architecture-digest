---
type: guidance
title: MoE推論のカーネル最適化(Fused MoE・Swap-AB)
title_original: Mixture-of-Experts kernel engineering on Amazon SageMaker AI
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
components:
- Amazon SageMaker AI
- NVIDIA Hopper
- WGMMA
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/mixture-of-experts-kernel-engineering-on-amazon-sagemaker-ai/
published_at: '2026-10-13'
---

## 概要

MoEモデルのFused MoEカーネルに対するSageMaker AIでの最適化を解説する。デコード時はトークン行数Mが極小になりHopperのWGMMA(M=64固定)が遊ぶため、オペランドを入れ替えるSwap-ABで利用率を高める。

## 設計のポイント

- デコード時のM<64というバッチ形状とWGMMAの固定タイルが衝突する点を特定している。
- A/Bを入れ替え、可変の大きい次元をN側に置くことでテンソルコア利用率を改善する。
- ルーティング・シャッフル・エキスパート計算を1つのバッチ演算に融合する。

## 使いどころ

- MoEモデルの推論レイテンシ/コストを下げたい推論基盤チーム。
- GPUカーネルレベルの最適化を検討する場面。
