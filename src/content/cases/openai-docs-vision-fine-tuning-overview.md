---
type: guidance
title: 画像入力を用いたVision Fine-tuningガイド
title_original: Vision fine-tuning
industry: cross-industry
cloud: []
patterns:
- fine-tuning
components:
- gpt-4o-2024-08-06
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/vision-fine-tuning
published_at: '2025-07-21'
---

## 概要

Vision fine-tuningは画像入力を用いた教師ありファインチューニングで、画像分類や複雑なプロンプトでの指示追従の失敗を修正するのに向く。JSONLトレーニングデータにimage_urlメッセージを含める形式で、detailパラメータでトークン数とコストを制御できる。OpenAIはファインチューニングプラットフォームの提供終了を進めており、新規ユーザーは利用できない。

## 設計のポイント

- detailをlowに設定すると画像は512x512にリサイズされ85トークン固定になり学習コストを抑えられる
- 人物・顔・子供・CAPTCHAを含む画像は学習前のコンテンツモデレーションで自動的に除外される
- ファインチューニング後は13カテゴリの安全性評価を行い、閾値を下回るとデプロイがブロックされる

## 使いどころ

- 画像分類や画像内容の説明生成の精度を業務ドメインに合わせて改善したい場合
- 複雑なプロンプトでの画像理解の指示追従を改善したいアプリケーション
