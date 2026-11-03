---
type: case
title: LlamaIndex OCRia：量子化と投機的デコードで推論を約10倍高速化
title_original: The inference stack behind OCRia
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- document-processing
components:
- OCRia-1
- B200
- speculative decoding
- quantization
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/the-inference-stack-behind-ocria
published_at: '2026-11-03'
---

## 概要

LlamaIndexは文書パースモデルOCRia-1の推論を、単一B200で約285から約2800トークン/秒へ約10倍にした。ワークロードに合わせた量子化、投機的デコード、検証コスト削減、メモリ転送とCPU前処理の改善を積み重ねた。

## 設計のポイント

- デコードがメモリ帯域律速と見て、移動データ量をワークロード認識の量子化で削る
- 投機的デコードでターゲットモデル1回あたりの生成トークンを増やす
- GPU/CPUの細かなオーバーヘッドを一つずつ潰す

## 使いどころ

- レイテンシが重要な文書パースサービス
- 自社モデルの推論スループットを上げたい基盤チーム
