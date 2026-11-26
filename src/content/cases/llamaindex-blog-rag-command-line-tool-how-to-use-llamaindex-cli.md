---
type: announcement
title: コードを書かずにローカル文書でRAGを試すllamaindex-cli
title_original: Introducing the LlamaIndex RAG Command Line Tool
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
components:
- llamaindex-cli
- Chroma
- OpenAI
- Ollama
- LlamaIndex
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-the-llamaindex-retrieval-augmented-generation-command-line-tool-a973fa519a41
published_at: '2024-01-26'
---

## 概要

ローカルファイルをChromaに取り込み、端末から質問や対話ができるllamaindex-cliを紹介。既定はOpenAIで、Ollama経由のローカルモデルにも差し替えられる。

## 設計のポイント

- 取り込み・質問・対話をCLIにまとめ、モデルは差し替え可能にする。

## 使いどころ

- 手元の文書でRAGを手早く試したい開発者。
