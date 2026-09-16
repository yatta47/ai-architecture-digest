---
type: case
title: 本番トレースからシステムプロンプトを自動改善するAgentCoreの最適化エンジン
title_original: Optimizing agent system prompts with Amazon Bedrock AgentCore
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- prompt-optimization
- ai-agent
- llmops
- guardrails
components:
- Amazon Bedrock AgentCore
- AgentCore Observability
- Strands
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/optimizing-agent-system-prompts-with-amazon-bedrock-agentcore/
published_at: '2026-09-16'
---

## 概要

Amazon Bedrock AgentCoreのシステムプロンプト最適化機能は、本番トレースと報酬シグナルをもとにリフレクターエージェントが改善版プロンプトを提案する仕組み。単一のリフレクターが全トレースを分析するSingle Agent Reflectorに加え、トレースごとにサブエージェントを割り当てて並列分析するSub-Agent Reflectorを実験的に提供し、長さ超過や安全性逸脱を防ぐガードレールで候補を審査してから適用する。

## 設計のポイント

- 評価済みトレース全体をファイルシステム経由でリフレクターに渡し、要約や切り詰めによる情報欠落を避ける
- トレースをサブエージェントに分割して並列分析させることで、少数のトレースに偏った学習を防ぐ
- プロンプトの長さが20%を超えて増加する候補やトレースの文言をそのまま流用する候補をガードレールで却下する
- 評価→内省→ガードレール適用のサイクルをエポックとして繰り返し、追加実行で品質を段階的に高められるようにする

## 使いどころ

- 本番トラフィックのトレースを使ってエージェントのシステムプロンプトを継続的に改善したいチーム
- 手作業でのトレースレビューとプロンプトチューニングに時間がかかっている運用チーム
- A/Bテストで安全に新しい設定を昇格させたいエージェント運用基盤
