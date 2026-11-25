---
type: case
title: 複数製品のドキュメントを横断検索するチャットボットLlamaWorksDB
title_original: Streamlining knowledge work with LlamaIndex, Fireworks and MongoDB
company: Team CLAB
industry: cross-industry
cloud: []
patterns:
- rag
components:
- LlamaIndex
- Fireworks.ai
- MongoDB Atlas Vector Search
- nomic-embed-text
- LlamaWorksDB
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/streamlining-knowledge-work-with-llamaindex-fireworks-and-mongodb
published_at: '2024-04-29'
---

## 概要

ハッカソンのチームが、LlamaIndex・Fireworks・MongoDBの文書を単一のチャットで検索できるRAGボットを構築した。Webとリポジトリから取り込み、MongoDBに本文・メタデータ・埋め込みを格納する。

## 設計のポイント

- Web取り込みではナビゲーション部分を除去し、トークンの浪費を防ぐ。
- 意味ベースの分割で意味のまとまったチャンクを作る。
- 文書とベクトルを同じMongoDBに置き、構成を単純にする。

## 使いどころ

- 複数ツールの公式文書を行き来する開発者向けの社内ボットを作る人。
- RAGの取り込み前処理を改善したいチーム。
