---
type: guidance
title: 長コンテキスト推論向けスパースアテンションのGPU共設計
title_original: Co-Designing Sparse Attention for Efficient Long-Context Inference
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
components:
- TensorRT LLM
- FlashInfer
- Tensor Core
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/co-designing-sparse-attention-for-efficient-long-context-inference/
published_at: '2026-11-17'
---

## 概要

長コンテキストでは密アテンションが支配的なコストになるため、クエリごとにキーを絞るスパースアテンションをGPU上で効率よく動かす設計指針を示す。インデクサやTop-kの融合、選択の再利用などで高速化する。

## 設計のポイント

- インデクサのヘッド次元・精度・グループサイズをTensor Core利用率とメモリ転送のバランスで決める。
- Top-kをインデクサカーネルに融合し、ロジットの書き戻しを避ける。
- 直前のデコード選択を推測として再利用しTop-kを加速する。

## 使いどころ

- 長文・コードベース・エージェント向けモデルの推論最適化を行うモデル開発者。
- NVIDIA GPU上のカーネル設計者。
