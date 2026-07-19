---
type: guidance
title: マルチテナントAIエージェントのOn-Behalf-Ofトークン交換実装
title_original: Implement on-behalf-of token exchange for multi-tenant agents with Amazon Bedrock AgentCore Gateway
industry: cross-industry
cloud:
- aws
patterns:
- llm-gateway
- defense-in-depth
components:
- Amazon Bedrock AgentCore Gateway
- Amazon Bedrock AgentCore Identity
- Okta
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/implement-on-behalf-of-token-exchange-for-multi-tenant-agents-with-amazon-bedrock-agentcore-gateway/
published_at: '2026-07-13'
---

## 概要

マルチテナントAIエージェントが下流APIを呼ぶ際に生じる「confused deputy」問題に対し、Amazon Bedrock AgentCore GatewayでOAuth 2.0 Token Exchange(RFC 8693)によるon-behalf-of(OBO)トークン交換を実装するガイド。複数テナント向け予約エージェントTravelBotを例に、各ホップでのJWTクレーム変換を具体的に示す。

## 設計のポイント

- subクレームで元の呼び出し者を保持しつつaudクレームだけをテナント別の下流APIに書き換え、最小権限を暗号学的に強制する。
- actクレームでAgentCoreが代行した事実を記録し、認可判断(sub)と監査・レート制限判断(actor)を分離する。
- エージェントコード側には交換ロジックを持たせず、GatewayとIdentityが全てのトークン交換を代行する。

## 使いどころ

- 1つのエージェントが複数テナントの下流サービスを呼び分ける必要があるマルチテナントSaaS。
- ユーザーがその場にいない状態でエージェントが代行アクセスするシステムの権限設計。
