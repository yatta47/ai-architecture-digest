---
type: guidance
title: Bedrock AgentCore上のエンタープライズ向けエージェント基盤の参照設計
title_original: Building an Agentic AI Platform on Amazon Bedrock AgentCore
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- llm-gateway
- guardrails
- eval
- policy-as-code
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock
- Amazon Bedrock Guardrails
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-an-agentic-ai-platform-on-amazon-bedrock-agentcore/
published_at: '2026-10-28'
---

## 概要

多数のチームがエージェントを開発するためのプラットフォームを、Bedrock AgentCoreとエンタープライズ向けブループリントで構築する方法を示す。マルチアカウント運用、推論とツールのゲートウェイ分離、本番昇格前の評価パイプラインを扱う。

## 設計のポイント

- 推論ゲートウェイでガードレール、利用可能モデルとリージョン、レート制限、トークン上限を強制する。
- プラットフォームチームとワークストリームチームの責務を分け、チームごとのデプロイを再利用可能なパターンにする。
- 評価パイプラインを本番昇格のゲートにし、ロールバック、テレメトリ、コスト帰属も標準装備にする。

## 使いどころ

- 複数のドメインチームが共通基準でエージェントを作る社内基盤を設計する場面。
- 統制のずれと所有者不明を避けたい規制対応の強い組織。
