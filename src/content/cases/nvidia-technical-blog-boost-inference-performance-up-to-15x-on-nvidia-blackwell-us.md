---
type: announcement
title: DFlash投機的デコーディングでBlackwell推論を最大15倍高速化
title_original: Boost Inference Performance up to 15x on NVIDIA Blackwell Using DFlash Speculative Decoding
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
components:
- DFlash
- NVIDIA Blackwell
- NVIDIA TensorRT-LLM
- SGLang
- vLLM
- EAGLE-3
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/boost-inference-performance-up-to-15x-on-nvidia-blackwell-using-dflash-speculative-decoding/
published_at: '2026-07-09'
---

## 概要

DFlashはブロック拡散モデルでトークンブロックを並列にドラフトし、対象モデルが並列検証するオープンソースの投機的デコーディング手法。NVIDIA Blackwell上でgpt-oss-120bを最大15倍高速化し、同一同時実行数でのLlama 3.1 8Bの対話性をEAGLE-3比でほぼ倍増させ、20種類のチェックポイントがSGLang/vLLM/TensorRT-LLMへ組み込み済みで公開されている。

## 設計のポイント

- 従来の逐次ドラフト生成をブロック拡散に置き換え、1回のフォワードパスで候補トークンブロック全体を並列生成する
- ターゲットモデルによる並列検証で出力品質を保証しつつ、Blackwellの高並列コンピュートを効率よく使い切る
- vLLM等ではEAGLE-3のチェックポイントをDFlashへ差し替えるだけで導入でき、アプリケーションのコード変更を必要としない

## 使いどころ

- コーディングや推論など高い対話性を維持しつつ同時接続ユーザー数を増やしたい推論基盤担当者
- 既存のEAGLE-3投機的デコーディング環境から大きな変更なしに高速化したいサービング運用者
