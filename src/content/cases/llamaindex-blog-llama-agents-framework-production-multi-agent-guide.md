---
type: announcement
title: エージェントをマイクロサービス化する llama-agents
title_original: Introducing llama-agents
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
- event-driven
components:
- llama-agents
- LlamaIndex
- OpenAI
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-llama-agents-a-powerful-framework-for-building-production-multi-agent-ai-systems
published_at: '2024-06-26'
---

## 概要

各エージェントを独立したマイクロサービスとして動かし、LLM駆動のコントロールプレーンがタスクを振り分けるOSSフレームワークllama-agentsをアルファ公開した。メッセージキューでの通信と監視ツールを備える。

## 設計のポイント

- エージェントを個別サービスにし、独立して起動・拡張・監視する。
- コントロールプレーンとメッセージキューで通信を一元化する。
- 順序を明示する流れと、オーケストレータに任せる流れを使い分ける。

## 使いどころ

- 試作したエージェントを本番サービスにしたい開発者。
- エージェントごとに拡張要件が異なるシステム。
