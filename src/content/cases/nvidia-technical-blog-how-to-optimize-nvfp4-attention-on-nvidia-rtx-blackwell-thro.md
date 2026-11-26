---
type: guidance
title: RTX Blackwell向けNVFP4アテンションをレジスタ再利用で高速化
title_original: How to Optimize NVFP4 Attention on NVIDIA RTX Blackwell Through Register Recycling
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
components:
- NVIDIA RTX PRO 6000 Blackwell
- SageAttention3
- FlashInfer
- NVFP4
- Reactor
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-to-optimize-nvfp4-attention-on-nvidia-rtx-blackwell-through-register-recycling/
published_at: '2026-11-25'
---

## 概要

SageAttention3カーネルのスコアタイルを2分割してレジスタを再利用し、次タイルの行列積を現タイルの残り処理と重ねることでTensor Coreの遊休を減らす。カーネルレイテンシは最大1.64倍改善し、Reactorの本番推論でもエンドツーエンドで最大15.34%削減した。

## 設計のポイント

- softmax出力を量子化した直後にスコアレジスタを解放し、第2のフルバッファを確保せずに次タイルを先行実行する。
- アクセラレータの世代ごとに律速（MMAかsoftmaxか）を見極めてカーネルのスケジュールを設計する。
- 最適化版はBF16ベースラインとレイテンシと出力品質の両方を比較して採用する。

## 使いどころ

- ワールドモデルや動画生成の推論をRTX Blackwellで提供するチーム。
- アテンションがボトルネックのリアルタイム推論を低レイテンシ化したい場面。
