---
type: announcement
title: Llama Packsと会話で作るRAGsなど：LlamaIndex更新（2023-11-28）
title_original: LlamaIndex Newsletter 2023-11-28
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
components:
- LlamaIndex
- Llama Packs
- RAGs
- FuzzyCitationEnginePack
- Zephyr-7B
- bge-base
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-11-28-a31be430a786
published_at: '2023-11-28'
---

## 概要

LLMアプリ用の事前構成モジュールLlama Packs、自然言語でRAGエージェントを組み立てるRAGs、回答と出典文を対応付ける引用パックなどを紹介するまとめ。月間100万ダウンロード到達も報告している。

## 設計のポイント

- 回答の各部分を出典の文に対応付けて引用の精度を高める。
- 設定を担うビルダーエージェントと実行するエージェントを分ける。

## 使いどころ

- RAGアプリの立ち上げを部品の再利用で早めたい開発者。
