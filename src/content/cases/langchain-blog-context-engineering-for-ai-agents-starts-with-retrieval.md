---
type: guidance
title: 'エージェントのコンテキストエンジニアリングは検索から始まる: Deep Agentsの設計'
title_original: Context Engineering Starts with Retrieval
company: LangChain
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
- rag
- multi-agent-orchestration
components:
- Deep Agents
- LangChain
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/context-engineering-starts-with-retrieval
published_at: '2026-10-23'
---

## 概要

エージェントの検索は、非効率な探索、一度に大量のコンテキスト、無関係・古い情報の3つで失敗する。Deep Agentsは検索してから読む組み込みファイルツール、大きな結果のファイルへのオフロード、サブエージェントへの委譲(retrieve, offload, delegate)で対処する。

## 設計のポイント

- glob→grep→ページ単位のread_fileと、検索してから読む段階的ツールにして文脈消費を抑える。
- 大きなツール結果はファイルへ退避し、パスとプレビューだけをエージェントに返す。
- RAGなどのカスタム検索は結果をファイル化し、サブエージェントに読ませてメインには関連部分のみ返す。

## 使いどころ

- 長時間タスクでコンテキスト枯渇に悩むエージェント開発者。
- 社内検索ツールをエージェントに接続する設計者。
