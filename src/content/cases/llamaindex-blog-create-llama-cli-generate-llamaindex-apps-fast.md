---
type: announcement
title: フルスタックRAGアプリを生成するCLI create-llama
title_original: create-llama, a command line tool to generate LlamaIndex apps
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
components:
- create-llama
- Next.js
- Express
- FastAPI
- LlamaIndex.TS
- OpenAI
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/create-llama-a-command-line-tool-to-generate-llamaindex-apps-8f7683021191
published_at: '2023-11-14'
---

## 概要

create-llamaは、質問に答えるだけで自分のデータと対話できるフルスタックアプリを生成するCLIである。フロントはNext.js、バックエンドはNext.js・Express・FastAPIから選べる。

## 設計のポイント

- dataフォルダに置いたファイルをビルド時に自動で索引化する。
- コストを考えて既定モデルを安価なものにし、必要に応じて差し替える。

## 使いどころ

- LlamaIndexアプリの雛形をすぐ用意したい開発者。
