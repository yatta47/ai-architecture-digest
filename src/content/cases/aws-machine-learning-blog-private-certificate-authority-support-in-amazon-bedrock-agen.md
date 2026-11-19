---
type: guidance
title: プライベートCAのIdPにAgentCore Identityから接続する
title_original: Private certificate authority support in Amazon Bedrock AgentCore Identity
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- defense-in-depth
components:
- Amazon Bedrock AgentCore
- AgentCore Identity
- AgentCore Runtime
- AWS Private CA
- AWS Secrets Manager
- Keycloak
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/private-certificate-authority-support-in-amazon-bedrock-agentcore-identity/
published_at: '2026-11-18'
---

## 概要

AgentCore Identityが、プライベートCA証明書を使うセルフホストのIdP(KeycloakやPingFederate)へ接続できるようになった。CA証明書をSecrets ManagerかS3に置き、認証情報プロバイダから参照し、CAのローテーションとアクセス保護も扱う。

## 設計のポイント

- CA証明書(公開部分のみ)を保管して参照し、IdPの証明書検証を行う。
- CAローテーションを、ダウンタイムを抑えて行う。
- CA証明書の変更権限をIdP担当チームに限定する。

## 使いどころ

- 社内ネットワーク内のIdPで認証するエージェントを動かす企業。
- プライベートCAを使う閉域環境でエージェントを運用するとき。
