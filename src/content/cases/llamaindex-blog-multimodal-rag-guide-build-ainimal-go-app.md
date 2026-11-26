---
type: case
title: 画像分類モデルとLLMを組み合わせた動物対話アプリAInimal Go
title_original: 'Multimodal RAG: Building AInimal Go!'
industry: media
cloud: []
patterns:
- rag
components:
- ResNet18
- Cohere
- LlamaIndex
- Streamlit
- Wikipedia
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/multimodal-rag-building-ainimal-go-fecf8404ed97
published_at: '2023-11-27'
---

## 概要

撮影・アップロードした動物画像をResNet18で分類し、その動物になりきったLLMと会話できる個人開発アプリ。約200件のWikipedia記事を知識ベースにし、GPT-4Vを使わず速度とコストを抑える。

## 設計のポイント

- 認識は軽量な専用ビジョンモデルに任せ、LLMには分類結果のテキストを渡す。
- 役割演技の応答も知識ベースの検索結果で裏付ける。

## 使いどころ

- 画像入力の用途が限定的で、汎用マルチモーダルLLMのコストを避けたい開発者。
- 教育・娯楽向けの対話アプリ試作。
