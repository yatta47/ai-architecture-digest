---
type: guidance
title: GPT Imageによる画像生成・編集の実践ガイド
title_original: Generate images with GPT Image
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- generative-image-editing
components:
- GPT Image (gpt-image-1)
- OpenAI Images API
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/generate_images_with_gpt_image/
published_at: '2025-04-23'
---

## 概要

OpenAIのcookbookが、新しい画像生成モデルGPT Image(gpt-image-1)を使った画像生成・編集の実装方法を解説する。詳細な指示に忠実な画像生成、品質・サイズ・圧縮率・透過背景などの出力パラメータのカスタマイズ、複数画像の合成やマスクを使った部分編集まで、Python SDKのコード例とともに示している。

## 設計のポイント

- quality(low/medium/high/auto)やsize、圧縮率、透過背景の有無など出力パラメータを用途に応じて細かく制御できるAPI設計になっている。
- images.editエンドポイントで最大10枚の入力画像を合成でき、マスクを与えれば画像の一部だけを保持したまま編集できる。
- マスク画像にはアルファチャンネルが必須であり、手動作成時にはこの点を明示的に扱う必要がある。

## 使いどころ

- 詳細なキャラクター設定やプロダクト画像などをテキスト指示だけで生成したいコンテンツ制作。
- 既存の複数画像を組み合わせて新しい合成画像を作る、あるいは画像の一部分だけをピンポイントで編集したいワークフロー。
- ファイルサイズや透過背景の要件が厳しいWeb/アプリ向けアセット生成。
