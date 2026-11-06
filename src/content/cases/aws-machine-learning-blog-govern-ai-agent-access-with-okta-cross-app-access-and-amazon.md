---
type: case
title: AgentCore GatewayとCedarでエージェントのアクセスを一元統治する構成
title_original: Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore – Part 2
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- policy-as-code
- guardrails
components:
- Amazon Bedrock AgentCore
- AgentCore Gateway
- AgentCore Identity
- Okta Cross App Access
- Cedar
- Amazon EKS
- Amazon CloudWatch
- Amazon EventBridge
- OpenTelemetry
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-access-with-okta-cross-app-access-and-amazon-bedrock-agentcore-part-2/
published_at: '2026-11-06'
---

## 概要

Part 1の1エージェント構成を、AgentCore Gatewayを単一の入口とする構成へ拡張する解説。Gatewayが Okta のグラントを引き換え、Cedarのデフォルト拒否ポリシーをツール実行前に評価し、EKS上の別エージェントも同じ経路で統治する。

## 設計のポイント

- エージェントが各MCPサーバーを直接呼ぶN×Mの配線をやめ、Gatewayのターゲット登録に集約している。
- トークン交換権限と秘密情報をエージェントのロールから外し、Gatewayが引き換えを担う。
- デフォルト拒否のCedarポリシーをGatewayで一括評価し、サーバーごとの認可コード重複とドリフトを避ける。
- 全ホップのOpenTelemetryスパンとOktaのシステムログをCloudWatchに集め、判断を一箇所で監査できる。

## 使いどころ

- 数百のエージェントと数千のツールを持つ企業でアクセス統制を中央化したいとき。
- 実行基盤(AgentCoreとEKS)が混在するエージェントを同一の認可で扱いたい場合。
- 監査担当がエージェントの認可判断を横断的に追跡したいとき。
