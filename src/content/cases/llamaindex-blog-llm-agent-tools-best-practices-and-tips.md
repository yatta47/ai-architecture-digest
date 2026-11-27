---
type: guidance
title: LLMエージェントが使いやすいツールを設計するコツ
title_original: Building Better Tools for LLM Agents
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- LlamaIndex
- LlamaHub Tools
- Wolfram Alpha
- BaseToolSpec
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-better-tools-for-llm-agents-f8c5a6714f11
published_at: '2023-07-17'
---

## 概要

LlamaHub Toolsの開発経験をもとに、エージェントが理解して呼び出しやすいツールの作り方を紹介する。Python関数をツール仕様として公開する抽象を説明する。

## 設計のポイント

- LLMが苦手な計算などは外部ツールに任せ、結果だけを返させる。
- 公開する関数を明示的に列挙し、エージェントが理解できる形で定義する。

## 使いどころ

- エージェント用のAPI連携ツールを実装する開発者向け。
- ツール呼び出しの失敗を減らしたいチーム向け。
