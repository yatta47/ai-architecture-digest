---
type: guidance
title: Claude DesktopにAgentCore Gatewayで安全なWeb検索を追加する手順
title_original: Add secure Web Search to Claude Desktop with Amazon Bedrock AgentCore
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- defense-in-depth
components:
- Claude Desktop
- Amazon Bedrock
- Amazon Bedrock AgentCore
- AgentCore Gateway
- AWS IAM Identity Center
- Amazon Cognito
- Model Context Protocol
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/add-secure-web-search-to-claude-desktop-with-amazon-bedrock-agentcore/
published_at: '2026-10-02'
---

## 概要

Amazon Bedrock上のClaude Desktopに、AgentCore GatewayのマネージドMCP対応Web Searchを接続して知識カットオフを補う手順の解説。IAM Identity CenterのSAMLをCognito経由でJWTに変換して認証し、クエリはAWS内に留まる構成になっている。

## 設計のポイント

- IAM Identity CenterとCognitoをSAMLとOAuth認可コードフローで連携させ、既存のSSOで認証を完結させる。
- GatewayがリクエストごとにJWTを検証し、外部APIキーや別IdPを不要にする。
- Web SearchをMCPターゲットとして公開し、クライアント側はマネージドMCPサーバーとして接続するだけにする。

## 使いどころ

- 社内規程上、検索クエリを外部に出せない企業でAIアシスタントに最新情報を使わせたい場面。
- 既存のSSO基盤でエージェントのツールアクセスを統制したい情報システム部門。
