---
type: guidance
title: LlamaIndex.TSでツール呼び出しエージェントを作る手順
title_original: How to Build LLM Agents in TypeScript with LlamaIndex.TS
industry: cross-industry
cloud: []
patterns:
- ai-agent
- rag
components:
- LlamaIndex.TS
- OpenAI
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/how-to-build-llm-agents-in-typescript-with-llamaindex-ts-a88ed364a7aa
published_at: '2024-02-08'
---

## 概要

TypeScriptで関数ツールを持つ計算エージェントと、自前文書をベクトル索引・要約索引で扱うエージェントを作る手順を解説する。

## 設計のポイント

- ツールは名前・説明・引数スキーマを明示し、LLMに選択させる。
- 詳細質問用と要約用の索引を別ツールとして与える。

## 使いどころ

- Node.js環境でエージェントを組みたい開発者。
