---
type: announcement
title: 自然言語の指示でRAGを構築・調整できるStreamlitアプリ RAGs
title_original: 'Introducing RAGs: Your Personalized ChatGPT Experience Over Your Data'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
components:
- RAGs
- Streamlit
- LlamaIndex
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-rags-your-personalized-chatgpt-experience-over-your-data-2b9d140769b1
published_at: '2023-11-21'
---

## 概要

RAGsは、タスクを自然言語で説明するとRAGパイプラインを組み立てて対話できるStreamlitアプリである。ビルダーエージェントが設定を生成し、利用者はUIでtop-kやチャンクサイズなどを調整できる。

## 設計のポイント

- 構築用ツールを持つビルダーエージェントが設定状態を作り、その設定からRAGエージェントを初期化する。
- 自動生成したパラメータを可視化し、人が編集して即時反映できるようにする。
- ベクトル検索と要約ツールを持たせ、質問に応じてエージェントが使い分ける。

## 使いどころ

- コードを書かずに自分のデータで質問応答を試したい利用者。
- RAGのパラメータを手早く比較したい開発者。
