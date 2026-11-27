---
type: announcement
title: テキストと画像を横断検索するマルチモーダルRAGの抽象化
title_original: Multi-Modal RAG
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
components:
- LlamaIndex
- GPT-4V
- CLIP
- Qdrant
- Replicate
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/multi-modal-rag-621de7525fea
published_at: '2023-11-10'
---

## 概要

LlamaIndexは、テキストと画像を索引化・検索して回答を合成するマルチモーダルRAGの抽象化を公開した。画像はCLIPで埋め込み、テキストとは別のコレクションに格納する。

## 設計のポイント

- テキストと画像は別の埋め込みモデルを使えるようコレクションを分ける。
- 検索はモダリティごとに行い、両方の結果をノードとしてまとめて合成に渡す。
- マルチモーダルLLMはテキスト専用LLMとは別の基底抽象にしてモデル差を吸収する。

## 使いどころ

- 画像と文書が混在するナレッジに質問応答したいチーム。
