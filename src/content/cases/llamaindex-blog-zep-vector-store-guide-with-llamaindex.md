---
type: guidance
title: 長期記憶ストアZepをベクトルストアとして使う
title_original: 'Zep and LlamaIndex: A Vector Store Walkthrough'
company: Zep
industry: cross-industry
cloud: []
patterns:
- rag
- context-engineering
components:
- Zep
- ZepVectorStore
- LlamaIndex
- Docker
- Kubernetes
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/zep-and-llamaindex-a-vector-store-walkthrough-564edb8c22dc
published_at: '2023-08-11'
---

## 概要

文書と会話履歴を保存・検索できるZepを、LlamaIndexのベクトルストアとして使う手順を紹介する。メタデータで絞り込む検索にも対応する。

## 設計のポイント

- 文書本文・埋め込み・メタデータを同じコレクションに同居させる。
- JSONメタデータの絞り込みと意味検索を併用する。
- 文書と会話履歴を1つのAPIから引き、長期記憶としてプロンプトに入れる。

## 使いどころ

- 会話履歴を踏まえて応答するLLMアプリを作る開発者向け。
- 記憶層を自前ホストしたいチーム向け。
