---
type: guidance
title: OpenTelemetryを共通言語にしてどのエージェントフレームワークでも評価できるBedrock AgentCore Evaluations
title_original: Evaluate any agent framework with Amazon Bedrock AgentCore Evaluations
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- eval
- llmops
- multi-agent-orchestration
components:
- Amazon Bedrock AgentCore
- OpenTelemetry
- Amazon CloudWatch
- AWS Distro for OpenTelemetry (ADOT)
- LangGraph
- LlamaIndex
- Strands Agents
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/evaluate-any-agent-framework-with-amazon-bedrock-agentcore-evaluations/
published_at: '2026-08-26'
---

## 概要

Amazon Bedrock AgentCore Evaluationsは、評価対象のエージェントがどのSDK/フレームワーク(LangGraph、LlamaIndex、OpenAI Agents SDK、Google ADK、Claude Agent SDK、Strands Agentsなど)で作られていても、OpenTelemetryの標準テレメトリさえ出していれば評価できるようにする。OpenTelemetryのGenAI規約やOpenInferenceのスパン種別を共通言語として使うことで、評価をフレームワーク選定から切り離している。

## 設計のポイント

- 評価をフレームワーク実装から疎結合にし、OpenTelemetryという業界標準の計装形式だけに依存させる
- モデル呼び出し・ツール呼び出し・検索・リランク・埋め込み・メモリ操作などをスパン種別として明確に区別し、粒度別に評価できるようにする
- ADOT経由でCloudWatchにスパンを集約し、名前付きフレームワーク以外のOTel準拠エージェントにもカバレッジを広げる

## 使いどころ

- 複数のエージェントフレームワークを併用している組織の評価基盤を一本化したい場合
- AgentCore runtime上で異なるSDKで構築されたエージェントを横断的に品質モニタリングしたい場合
