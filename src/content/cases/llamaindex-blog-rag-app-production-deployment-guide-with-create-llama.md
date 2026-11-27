---
type: guidance
title: create-llamaで生成したRAGアプリを本番公開する手順
title_original: Shipping your Retrieval-Augmented Generation App to Production with create-llama
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
components:
- create-llama
- Next.js
- Vercel
- Express
- Render
- FastAPI
- OpenAI
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/shipping-your-retrieval-augmented-generation-app-to-production-with-create-llama-7bbe43b6287d
published_at: '2023-11-20'
---

## 概要

create-llamaで生成したフルスタックRAGアプリを、Next.js・Express・Pythonの各バックエンドごとに本番公開する手順を解説する。VercelやRenderにGitリポジトリを接続してデプロイする。

## 設計のポイント

- サーバーレス構成なら成果物を1つにまとめ、デプロイを単純化する。
- フロントとバックエンドを分ける場合は、静的サイトとWebサービスを別々に配置し呼び出し許可を設定する。
- APIキーはコードに含めず環境変数で渡す。

## 使いどころ

- RAGの試作を素早く公開環境に載せたい開発者。
