---
type: guidance
title: AgentCoreからSnowflake Cortex AIを呼ぶ際のOAuth 3パターン
title_original: Secure OAuth patterns for Snowflake Cortex AI through Amazon Bedrock AgentCore
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- defense-in-depth
components:
- Amazon Bedrock AgentCore
- AgentCore Identity
- AgentCore Gateway
- Snowflake Cortex
- MCP
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/secure-oauth-patterns-for-snowflake-cortex-ai-through-amazon-bedrock-agentcore/
published_at: '2026-11-17'
---

## 概要

AgentCore上のエージェントがSnowflake管理MCPサーバーを呼ぶ際の認証として、Snowflake OAuth、3-legged OAuth（社内SSO）、2-legged OAuth（共有サービスユーザー）の3構成を検証した。ユーザー単位の権限か共有かで選び、OBOグラントも選択肢となる。

## 設計のポイント

- ユーザー単位のIDを保つか共有サービスアカウントかを要件で選ぶ。
- Gatewayで複数ターゲットのツールを単一カタログに集約する。
- 無人ワークロードではOBOでユーザー権限を維持する。

## 使いどころ

- エージェントに広いサービスアカウント権限を持たせたくない企業。
- Snowflakeデータへのエージェント連携の認可設計を行う担当者。
