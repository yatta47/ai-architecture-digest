---
type: guidance
title: Image APIとResponses APIの使い分けで画像生成・編集フローを設計する
title_original: Image generation guide
industry: cross-industry
cloud: []
patterns:
- image-generation
components:
- Image API
- Responses API
- GPT Image
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/image-generation
published_at: '2025-07-18'
---

## 概要

GPT Imageモデルによる画像生成・編集は、単発生成に向くImage APIと、複数ターンでの高精度編集や会話内画像入出力に向くResponses APIの2経路で提供される。用途に応じてどちらのAPIを軸に据えるかが設計上の分岐点になる。

## 設計のポイント

- 単発の生成・編集で完結するならImage API、会話の中で反復編集したいならResponses APIを選ぶ、という基準でAPIを使い分ける。
- Responses APIはFile IDでの画像入力やprevious_response_idによるマルチターン編集など、対話的な画像編集体験に必要な機能を追加で提供する。
- 品質・サイズ・フォーマット・圧縮率などの出力パラメータは両APIで共通してカスタマイズ可能にしておく。

## 使いどころ

- チャット型UIの中でユーザーと一緒に画像を反復編集していくプロダクトを作る場合。
- 単発のプロンプトから決まった枚数の画像をバッチ生成したいユースケース。
