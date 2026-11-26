---
type: guidance
title: 文書ごとのエージェントを上位エージェントが束ねるAgentic RAG
title_original: Agentic RAG with LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- multi-agent-orchestration
- ai-agent
components:
- LlamaIndex
- OpenAI
- Cohere Rerank
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/agentic-rag-with-llamaindex-2721b8a49ff6
published_at: '2024-01-30'
---

## 概要

文書ごとに検索と要約ができるエージェントを作り、上位エージェントがツール検索とChain-of-Thoughtで束ねて回答するAgentic RAGの構成を解説する。

## 設計のポイント

- 文書単位のサブエージェントに分け、文書追加はエージェント追加で拡張する。
- 上位エージェントはツール検索で対象を絞ってから推論する。
- 各エージェントには事前知識に頼らずツールを使うよう指示する。

## 使いどころ

- 多数の文書群を横断する質問応答を作る開発者。
