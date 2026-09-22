---
type: guidance
title: 非構造化証拠データをMCP経由でAgentforceに繋ぐ公共セクター向けパターン
title_original: Extending public sector intelligence with Agentforce and AWS
industry: public-sector
cloud:
- aws
patterns:
- document-processing
- event-driven
- ai-agent
components:
- Amazon Bedrock Data Automation
- Amazon Bedrock AgentCore Gateway
- AWS Lambda
- Amazon S3
- Amazon DynamoDB
- Amazon EventBridge
- Salesforce Agentforce
- MCP
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/extending-public-sector-intelligence-with-agentforce-and-aws/
published_at: '2026-09-22'
---

## 概要

ボディカメラ映像や監視映像、スキャン文書などの非構造化証拠データをAmazon Bedrock Data Automationで自動的に構造化し、Model Context Protocol経由でSalesforce Agentforceの自然言語クエリから参照できるようにするアーキテクチャパターン。Salesforceのコンソールを離れることなく処理済みデータの検索とインサイト取得ができる。

## 設計のポイント

- S3イベント通知起点のイベント駆動パイプラインでBedrock Data Automationによる非同期処理を開始する
- AgentCore GatewayをMCPのフロントに置きAgentforceからの認証付きツール呼び出しをAWS側にルーティングする
- メディア種別ごとに抽出設定を切り替えられるためAgentCore Gatewayの設定変更のみでユースケースを追加できる
- 処理パイプラインと問い合わせ経路を疎結合にし別のエージェントフロントエンドにも同じMCPを接続可能にした

## 使いどころ

- 大量のボディカメラ映像や証拠書類を人手でレビュー・分類している捜査・法執行部門
- 既存のSalesforceワークフローを離れずにAWS側データを検索したい公共セクターの業務システム
- 証拠管理以外の非構造化データ活用にも同じパターンを転用したい場合
