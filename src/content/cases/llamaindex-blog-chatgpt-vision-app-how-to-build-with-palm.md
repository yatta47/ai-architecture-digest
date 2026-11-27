---
type: case
title: KOSMOS-2とPaLMで作る画像対話アプリの試作
title_original: Building My Own ChatGPT Vision with PaLM, KOSMOS-2 and LlamaIndex
industry: cross-industry
cloud: []
patterns:
- context-engineering
components:
- KOSMOS-2
- Google PaLM API
- LlamaIndex
- Replicate
- Streamlit
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-my-own-chatgpt-vision-with-palm-kosmos-2-and-llamaindex-9f9fdd13e566
published_at: '2023-11-08'
---

## 概要

アップロード画像をKOSMOS-2でキャプション化し、その説明文をPaLMとの会話の文脈にする、画像対話のStreamlit試作アプリの紹介。LlamaIndexがモデルの連携と会話メモリを担う。

## 設計のポイント

- 視覚モデルで画像をテキスト化し、テキストLLMに渡す二段構成でマルチモーダル対話を実現する。
- 会話メモリのトークン上限とセッションあたりのメッセージ数上限で利用量を抑える。

## 使いどころ

- 画像対応APIを使わずに画像対話を試作したい開発者。
