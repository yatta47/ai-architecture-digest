---
type: guidance
title: 生物学基盤モデルのMoE学習をTransformer Engineで高速化する手順
title_original: Efficient MoE Training for Biological Foundation Models
company: NVIDIA
industry: healthcare
cloud: []
patterns:
- cost-optimization
- inference-optimization
components:
- NVIDIA Transformer Engine
- GroupedLinear
- MXFP8
- NVIDIA BioNeMo
- NVIDIA Blackwell GPU
- PyTorch
- Hugging Face Transformers
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/efficient-moe-training-for-biological-foundation-models/
published_at: '2026-09-23'
---

## 概要

生物学基盤モデルをMixture-of-Experts構成で学習する際の3つの課題（エキスパート計算の断片化、モデルとアクティベーションのメモリ、量子化のオーバーヘッド）に対し、NVIDIA BioNeMoレシピとTransformer Engineで対処するチュートリアル。8基のB200でHugging Face実装比最大2.21倍のスループットを示している。

## 設計のポイント

- エキスパートごとのPythonループをGroupedLinearによる単一のグループ化GEMMに置き換え、カーネル起動とスケジューリングのオーバーヘッドを削減する。
- MXFP8（32要素ブロックごとのスケーリング）で重みと活性を8bit化し、メモリ使用量を減らしつつ精度を保つ。
- 量子化・SwiGLU・ルーティング重みのスケーリングを1つの融合カーネルにまとめ、中間テンソルの実体化を避ける。
- 融合MXFP8カーネルはBlackwell GPUが前提で、エキスパート並列には2GPU以上が必要という制約を前提に設計する。

## 使いどころ

- ゲノミクスなど長系列データでMoEの基盤モデルを学習し、GPU効率とメモリを改善したいML基盤チーム。
- Hugging Faceのナイーブな MoE 実装から高速な学習パスへ移行したいとき。
- Blackwell世代GPUで低精度学習を導入する際の参照実装として。
