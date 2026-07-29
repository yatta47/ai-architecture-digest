---
type: guidance
title: Amazon Bedrock AgentCoreエージェントの秘密鍵JWT認証基盤
title_original: Authenticate with Private Key JWT using Amazon Bedrock AgentCore Identity
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- defense-in-depth
components:
- Amazon Bedrock AgentCore Identity
- AWS KMS
- AWS CloudTrail
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/authenticate-with-private-key-jwt-using-amazon-bedrock-agentcore-identity/
published_at: '2026-07-29'
---

## 概要

Amazon Bedrock AgentCore Identityが、共有クライアントシークレットの代わりに署名付きJWTクライアントアサーションでダウンストリームIdPに認証するPrivate Key JWT方式をサポートした。秘密鍵はAWS KMSに保管されたまま外に出ず、AgentCoreがKMSに署名を委任してアサーションを発行する。M2M・OBO(ユーザー代理)・ユーザー委任の3つのグラントフローに対応する。

## 設計のポイント

- 秘密鍵をAWS KMSに保管し、AgentCore IdentityがKMSへ署名を委任することで秘密鍵自体は一切外部に出さない
- kms:ViaService条件でAgentCore Identity経由のリクエストのみに鍵利用を制限し、最小権限を担保する
- M2M・OBO(ユーザー代理)・ユーザー委任(認可コード)の3グラントフローを1つの認証方式でカバーする
- CloudTrailにエージェントのトークン取得イベントを記録し、監査証跡を残す

## 使いどころ

- 共有シークレットの漏えいリスクを避けたいエージェント間(M2M)のバックエンド連携
- 既存ユーザートークンを引き継いでダウンストリームAPIを呼び出すOBOシナリオ
- 監査・証跡要件が厳しい規制業界でのエージェント認証基盤の構築
