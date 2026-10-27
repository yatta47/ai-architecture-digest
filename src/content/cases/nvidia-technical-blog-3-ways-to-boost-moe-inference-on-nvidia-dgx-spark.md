---
type: guidance
title: DGX SparkでMoE推論を42%高速化する3手法
title_original: 3 Ways to Boost MoE Inference on NVIDIA DGX Spark
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
components:
- NVIDIA DGX Spark
- Ling-3.0-flash
- FlashInfer
- Humming
- FP8
- MTP
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/3-ways-to-boost-moe-inference-on-nvidia-dgx-spark/
published_at: '2026-10-26'
---

## 概要

Ling-3.0-flashをDGX Sparkでバッチ1で測り、メモリ律速のデコードに対しHumming MXFP4 MoEカーネル、LMヘッドのFP8量子化、MTP投機的デコードを適用して、精度を保ったままスループットを42.5%向上させた。

## 設計のポイント

- まずプロファイルして律速要因を特定する。
- 重み読み出し量を減らす手段と、1ラウンドで得るトークンを増やす手段を組み合わせる。
- 組み合わせで遅くなる統合問題があり、全体で測定する。

## 使いどころ

- 手元のGPUでMoEモデルを動かす開発者。
- ローカル推論の遅延を下げたいとき。
