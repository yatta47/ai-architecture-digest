---
type: case
title: SlackのITヘルプデスクAgent「Deckhand」(ShipStation Global)
title_original: How ShipStation Global built an AI IT help desk on Amazon Bedrock AgentCore
company: ShipStation Global
industry: logistics
cloud:
- aws
patterns:
- ai-agent
- rag
- human-in-the-loop
components:
- Amazon Bedrock AgentCore
- Strands Agents
- Amazon Bedrock Knowledge Bases
- AWS Lambda
- AgentCore Gateway
- Amazon DynamoDB
- AWS X-Ray
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-shipstation-global-built-an-ai-it-help-desk-on-amazon-bedrock-agentcore/
published_at: '2026-10-13'
---

## 概要

ShipStation GlobalはSlack上で動くITヘルプデスクAgent Deckhandを、Bedrock AgentCore RuntimeとStrandsエージェントで構築した。Confluenceや社内イントラのナレッジから回答し、スクリーンショットを読み、Jiraチケットを作成して、3か月でチャンネル問い合わせの97.5%を解決し肯定評価96%を得た。

## 設計のポイント

- Slack受信サービス(App Runner)とエージェント本体(AgentCore Runtime)を分離し、セッション隔離されたサーバーレス実行にしている。
- ツール群を1つのLambdaにまとめAgentCore GatewayでMCPツールとして公開している。
- 解決できない場合は会話文脈付きのチケットをワンクリックで起票し、人へのエスカレーションを組み込んでいる。
- フィードバックをDynamoDBに蓄積しX-Rayで経路をトレースして改善に使っている。

## 使いどころ

- 社内ヘルプデスクや定型問い合わせをSlackで自己解決させたいIT部門。
- 複数拠点で営業時間外の問い合わせが多い組織。
