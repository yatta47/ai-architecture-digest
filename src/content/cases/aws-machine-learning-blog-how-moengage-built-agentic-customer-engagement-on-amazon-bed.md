---
type: case
title: MCPコネクタとAgentCoreで作るエージェント型カスタマーエンゲージメント
title_original: How MoEngage built agentic customer engagement on Amazon Bedrock AgentCore
company: MoEngage
industry: retail
cloud:
- aws
patterns:
- ai-agent
- multi-tenant-rag
- guardrails
components:
- Amazon Bedrock AgentCore
- Model Context Protocol
outcome:
  type: revenue
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-moengage-built-agentic-customer-engagement-on-amazon-bedrock-agentcore/
published_at: '2026-11-16'
---

## 概要

MoEngageはテナント単位のアクセス制御付きMCPコネクタを提供し、ClaudeなどのアシスタントやMerlin AIから、セグメントやキャンペーン履歴、コンテンツを使って施策を一つの会話で作れるようにした。Glanceではプッシュ通知のCTRが38%向上した。

## 設計のポイント

- 既存APIをエージェントのツールとして公開し、MCPで外部アシスタントとつなぐ。
- テナントスコープでデータ分離と認可を保つ。
- UIとAPIに続く第三の層として、成果を言語で指示する層を設ける。

## 使いどころ

- 複数ツールを行き来するマーケティング運用。
- API群をエージェント向けに開放するSaaS事業者。
