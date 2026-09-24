---
type: case
title: AgentCore GatewayとMCPで複数AWSアカウントのデータを横断するエージェント基盤
title_original: Build a multi-account AI agent with AgentCore Gateway and MCP
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- llm-gateway
- guardrails
- policy-as-code
components:
- Amazon Bedrock AgentCore Gateway
- Amazon Bedrock AgentCore Runtime
- AgentCore Identity
- Amazon Bedrock
- Amazon Bedrock Guardrails
- Amazon Bedrock Knowledge Bases
- Okta
- Model Context Protocol
- Amazon CloudFront
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-multi-account-ai-agent-with-agentcore-gateway-and-mcp/
published_at: '2026-09-24'
---

## 概要

各事業部(LOB)のデータを各アカウントに残したまま、プラットフォームアカウントのエージェントがAgentCore Gateway経由でMCPサーバーを横断的に呼び出す構成を示す。認証はAgentCore IdentityとOkta、認可はCedarベースのPolicyで行い、データを複製せず問い合わせ時に必要な結果だけを流す。

## 設計のポイント

- LOBは生のリソースでなくMCPサーバーとしてツールを公開し、インターフェースが保たれる限り内部実装を自由に変えられるハブ&スポーク構成にする。
- AgentCore Gatewayを単一のMCPエンドポイントとして、ツール発見(セマンティック検索)・認証・認可・可観測性を集約する。
- GuardrailsとCedarのPolicyをGateway層で適用し、エージェントのコード外でガバナンスを強制する。
- LLM推論はプラットフォームアカウントに集約して、モデル管理と課金境界を一本化する。

## 使いどころ

- データがアカウントごとに分散した大企業で、データを集約せずに横断的なエージェントを作りたい場合。
- 金融など、データ所有権や権限分離が厳格な組織でエージェント基盤を標準化したい場合。
- 複数エージェントやA2Aサービスを単一の統制されたエンドポイントにまとめたい場合。
