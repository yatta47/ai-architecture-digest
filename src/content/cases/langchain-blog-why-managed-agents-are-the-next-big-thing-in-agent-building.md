---
type: opinion
title: マネージドエージェントの時代——ハーネスとインフラを束ねて本番運用を楽にする
title_original: Why managed agents are the next big thing in agent building
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- unified-runtime
components:
- LangGraph
- Deep Agents
- Managed Deep Agents
- LangSmith Deployments
- LangSmith Sandboxes
- MCP
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/why-managed-agents-are-the-next-big-thing-in-agent-building
published_at: '2026-08-13'
---

## 概要

LangChainがエージェント構築の歴史を振り返りつつ、ハーネス（Deep Agents等）とランタイム・サンドボックス・評価・メモリ・認証といった本番インフラを一括提供する「マネージドエージェント」の潮流を解説。自社の新サービスManaged Deep Agentsを、ビジネスロジック・ハーネス・インフラの3層モデルで位置づける。

## 設計のポイント

- エージェント構築を「ビジネスロジック」「ハーネス」「本番インフラ」の3層に分解し、後者2つをマネージドサービスとして束ねる
- AGENTS.md・MCP・skillsといった共通標準でエージェント挙動を駆動し、ベンダーロックインを避けつつ移植性を保つ
- 耐久実行（durable execution）とサンドボックスで「頭脳と手を分離する」設計を、個別実装せず基盤側が提供する

## 使いどころ

- ローカルでは動くエージェントを本番のランタイム・監視・認証込みでデプロイしたい開発者
- ハーネス選定からインフラ構築まで一つ一つ組み上げる工数を削減したいプラットフォームチーム
