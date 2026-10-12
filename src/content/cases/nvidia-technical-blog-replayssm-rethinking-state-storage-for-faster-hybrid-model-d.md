---
type: guidance
title: 'ReplaySSM: SSM入力をキャッシュしてハイブリッドモデルのデコードを高速化'
title_original: 'ReplaySSM: Rethinking State Storage for Faster Hybrid-Model Decoding'
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
components:
- NVIDIA TensorRT-LLM
- vLLM
- FlashInfer
- NVIDIA Blackwell Ultra B300
- Mamba-2
- Nemotron 3
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/
published_at: '2026-10-12'
---

## 概要

SSM層の状態をチェックポイントと直近入力のバッファで表現し、状態の読み書きを約半分に減らすことでデコードカーネルをB300上で1.46〜1.80倍に高速化する手法。投機的デコードのロールバックを単純化し、低精度状態での誤差蓄積も抑える。TensorRT-LLM、vLLM、FlashInferに統合されている。

## 設計のポイント

- 状態そのものではなく入力をキャッシュし、バッファが満杯のときだけチェックポイントを書き出して状態トラフィックを削減する。
- 投機的デコードでは状態をスナップショットせず、ドラフト入力をバッファへ追記するだけでロールバックを簡単にする。
- 再帰計算は高精度のチェックポイント、読み出しは低精度コピーにして量子化誤差の蓄積を抑える。

## 使いどころ

- Nemotron 3やQwen3.5系などのハイブリッドモデルを高バッチで配信する推論基盤の担当者。
- 投機的デコードや量子化をSSM層を持つモデルに適用したい場面。
