---
type: guidance
title: AgentCore GatewayでエージェントのユーザーIDをServiceNow APIまで伝播するOBOトークン交換
title_original: ServiceNow on-behalf-of token exchange with Bedrock AgentCore Gateway
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- defense-in-depth
- guardrails
components:
- Amazon Bedrock AgentCore Gateway
- Microsoft Entra ID
- ServiceNow
- MCP
- Amazon Bedrock Guardrails
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/servicenow-on-behalf-of-token-exchange-with-bedrock-agentcore-gateway/
published_at: '2026-11-03'
---

## 概要

エージェントが企業APIを呼ぶ際にユーザーIDを維持するため、AgentCore GatewayでEntra IDとのOBOトークン交換を設定する方法を示す。ゲートウェイのターゲット側でトークン交換を行い、ServiceNowはユーザー権限でAPIを処理する。

## 設計のポイント

- トークン交換をゲートウェイのターゲット設定に寄せ、エージェント側コードにID処理を持たせない
- audience違いをOBOフローで橋渡しし、元ユーザーのpreferred_usernameを下流に渡す
- OAuth保護された他のREST APIにも同じパターンを適用でき、Guardrailsと併用できる

## 使いどころ

- 監査証跡とユーザー単位のアクセス制御が必須の社内業務エージェント
- ServiceNowなど既存SaaSをMCP経由でエージェントに公開したい基盤チーム
