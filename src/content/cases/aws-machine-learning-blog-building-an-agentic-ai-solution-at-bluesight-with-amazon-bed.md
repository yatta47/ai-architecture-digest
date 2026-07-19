---
type: case
title: Bluesightの医療コンプライアンス向け統合エージェントAI「Prism」
title_original: Building an agentic AI solution at Bluesight with Amazon Bedrock
company: Bluesight
industry: healthcare
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- llm-gateway
components:
- Amazon Bedrock AgentCore
- Strands Agents
- AWS Lambda
- Amazon Bedrock AgentCore Gateway
- Amazon Bedrock AgentCore Runtime
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-an-agentic-ai-solution-at-bluesight-with-amazon-bedrock/
published_at: '2026-07-13'
---

## 概要

病院・薬局向けコンプライアンスSaaSのBluesightは、Amazon Bedrock AgentCoreを用いて単一製品向けAIプロトタイプから6製品を横断する統合エージェントAI「Prism」へと発展させた。ControlCheck向けPrism Assistantは2026年5月にローンチし、既に20の医療システムで利用されている。

## 設計のポイント

- AgentCore Gatewayで既存製品(ControlCheck等)のAPIをMCP互換ツールへ変換し、認証・暗号化込みでエージェントに公開する。
- コーディネーティングエージェントが専門ワーカーエージェント(CostCheck/ShortageCheck/340BCheck担当)に委譲するagent-to-agentパターンで、複数製品にまたがる証跡を横断集約する。
- AIの推論とデータ層を分離し、既存APIをLambdaでラップして構造化データを返すことでクエリレイテンシを5分から10秒に短縮する。

## 使いどころ

- HIPAA等の規制下で複数システムを横断する証跡が必要なコンプライアンス業務。
- 単一製品向けAIプロトタイプを複数製品共通の再利用可能な基盤に拡張したいSaaS事業者。
