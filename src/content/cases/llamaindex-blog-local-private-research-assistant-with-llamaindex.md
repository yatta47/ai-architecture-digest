---
type: guidance
title: llamafileとLlamaIndexで完全ローカルのRAG研究アシスタントを作る
title_original: Using LlamaIndex and llamafile to build a local, private research assistant
company: Mozilla
industry: cross-industry
cloud:
- on-prem
patterns:
- rag
components:
- llamafile
- LlamaIndex
- llama.cpp
- TinyLlama
- Mistral-7B-Instruct
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/using-llamaindex-and-llamafile-to-build-a-local-private-research-assistant
published_at: '2024-05-14'
---

## 概要

単一実行ファイルのllamafileをLLMと埋め込みのバックエンドにし、データを外部に送らないローカルRAGを構築するチュートリアル。

## 設計のポイント

- 生成と埋め込みの両方をローカル実行にし、データを第三者へ送らない構成にする。
- モデルを実行ファイルとして配布・差し替えし、導入手順を最小化する。

## 使いどころ

- 機密文書を外部送信せずに検索・質問したい研究者。
- API費用をかけずにLLMアプリを試験したい開発者。
