---
type: guidance
title: Bedrock AgentCore上の7層コンポーザブル・エージェント参照アーキテクチャ
title_original: 'Pluggable Agentic AI Framework: A seven-layer composable enterprise agentic AI reference architecture'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- multi-agent-orchestration
- guardrails
- llmops
- defense-in-depth
components:
- Amazon Bedrock AgentCore
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/pluggable-agentic-ai-framework-a-seven-layer-composable-enterprise-agentic-ai-reference-architecture-on-amazon-bedrock-agentcore/
published_at: '2026-11-09'
---

## 概要

マルチエージェントを本番規模へ載せるための7層の参照アーキテクチャを紹介する。各層は安定した契約を持ち、実装は差し替え可能である。ルーティング、ガードレール、観測を後付けでなく最初から組み込む。

## 設計のポイント

- 層ごとに責務と契約を固定し、実装を差し替え可能にする。
- ガードレールと観測を設計に組み込む。
- 決定論的処理と非決定論的処理を使い分ける。

## 使いどころ

- PoCから本番へ移行するエージェント基盤の標準化
