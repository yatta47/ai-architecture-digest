---
type: guidance
title: AgentCore GatewayをハブアンドスポークのプライベートAPIへ中央検査付きで接続
title_original: Connect Amazon Bedrock AgentCore Gateway to private APIs in a hub-and-spoke network with centralized inspection
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- defense-in-depth
components:
- Amazon Bedrock AgentCore Gateway
- Amazon VPC Lattice
- AWS RAM
- AWS CloudFormation
- AWS Organizations
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/connect-amazon-bedrock-agentcore-gateway-to-private-apis-in-a-hub-and-spoke-network-with-centralized-inspection/
published_at: '2026-11-18'
---

## 概要

ネットワークチームがVPCを管理し、すべての通信を中央ファイアウォールで双方向に検査する企業向けに、AgentCore GatewayからプライベートAPIやMCPサーバーへ接続するパターンを示す。VPC Latticeのリソースゲートウェイの置き方、所有区分、6つの設定判断と検証を扱う。

## 設計のポイント

- VPC Latticeのリソースゲートウェイの置き場所を決め、通信を中央ファイアウォール経由にする。
- サブネットの所有をネットワークチームに残す。
- 構成判断と検証手順をテンプレートとテストで再現できるようにする。

## 使いどころ

- 中央ファイアウォールを必須とする企業でエージェントを内部APIに接続するとき。
- MCPサーバーを閉域内に置くとき。
