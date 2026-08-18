---
type: case
title: Axoniusが構築したBedrock AgentCore上のセキュアなマルチテナントAIエージェント
title_original: How Axonius built secure multi-tenant AI agents on Bedrock AgentCore
company: Axonius
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-tenant-agents
- defense-in-depth
- policy-as-code
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock AgentCore Runtime
- Amazon Bedrock AgentCore Gateway
- Amazon Bedrock Knowledge Bases
- Amazon Cognito
- AWS Lambda
- Amazon VPC
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-axonius-built-secure-multi-tenant-ai-agents-on-bedrock-agentcore/
published_at: '2026-08-18'
---

## 概要

1,400以上のシステムからデータを集約するセキュリティ資産インテリジェンスSaaS企業Axoniusは、既存のテナントごとに専用VPCを割り当てる「サイロ」型構成を維持したままAIエージェントを追加する必要があった。Bedrock AgentCoreが提供するサイロ・プール・ブリッジの3つのマルチテナンシーパターンを比較し、テナント分離・既存ID基盤との統合・テナント単位のコスト計測・大規模なエージェント群の可観測性という要件に沿って構成を検討した。

## 設計のポイント

- テナントごとに専用リソースを割り当てる「サイロ」、単一エージェントを共有しセッションIDで分離する「プール」、両者を部分的に組み合わせる「ブリッジ」という3パターンでマルチテナンシーを整理する
- プール型ではJWTのカスタムクレーム(tenant_id)とAgentCore Runtime組み込みのJWT認可機能でツール呼び出しやデータアクセスをテナントごとにルーティングする
- ブリッジ型ではAgentCore Gatewayでのツール呼び出しにCedarベースのポリシー(決定的なアクセス制御)とLambdaインターセプター(動的な検証・コンテキスト付与)を組み合わせ、ツール層でテナント境界を強制する
- AgentCore Runtimeはセッションごとに専用microVMを割り当てる構造的な分離をどのモデルでも共通の基盤として提供する

## 使いどころ

- 多数の顧客テナントを抱えるSaaS/ISVがAIエージェント機能を追加する際のマルチテナンシー設計の意思決定
- 既存の認証・認可基盤を壊さずにAIエージェントのアイデンティティフローを統合したい場合
- テナント単位でのモデル呼び出しコスト計測や、大規模なエージェント群に対する可観測性・アラートが必要な運用
