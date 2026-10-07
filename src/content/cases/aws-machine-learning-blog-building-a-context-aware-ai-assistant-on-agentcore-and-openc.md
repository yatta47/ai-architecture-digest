---
type: case
title: AgentCoreとOpenClawによる記憶を持つ文脈対応パーソナルアシスタント
title_original: Building a context-aware AI assistant on AgentCore and OpenClaw
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- memory-consolidation
- context-engineering
- event-driven
components:
- Amazon Bedrock AgentCore
- OpenClaw
- Amazon Bedrock
- Amazon EventBridge Scheduler
- Amazon API Gateway
- AWS Lambda
- Amazon S3
- AWS KMS
- AWS Secrets Manager
- Amazon CloudWatch
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-a-context-aware-ai-assistant-on-agentcore-and-openclaw/
published_at: '2026-10-06'
---

## 概要

OpenClawをAgentCore runtime上で動かし、AgentCore memoryで会話を継続的な知識として蓄積するガーデニングアシスタントSproutを構築する。Telegramとスケジュール実行が同一エージェントを呼び、構造化メタデータで必要な記憶を検索する。

## 設計のポイント

- Webhookと定期ジョブの2つの入口を同じAgentCore runtimeのエージェントに集約する
- 記憶に構造化メタデータを付与して、質問に関係する記録を絞り込む
- ペルソナとスキル定義の差し替えだけで他用途に流用でき、単一CloudFormationで展開できる

## 使いどころ

- 継続的な文脈を保つ個人向け・社内ヘルプデスク向けアシスタント
- 従量課金で小規模に始めたいエージェント基盤
