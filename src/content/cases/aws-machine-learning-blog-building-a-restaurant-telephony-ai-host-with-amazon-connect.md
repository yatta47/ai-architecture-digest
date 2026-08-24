---
type: case
title: 電話注文をAIホストが完結させるレストラン向け音声注文システム
title_original: Building a restaurant telephony AI host with Amazon Connect
industry: retail
cloud:
- aws
patterns:
- voice-agent
- ai-agent
- realtime-transcription
components:
- Amazon Connect
- Amazon Lex V2
- Amazon Connect Agentic Voice
- Amazon Bedrock AgentCore
- AgentCore Gateway
- Model Context Protocol (MCP)
- Amazon API Gateway
- AWS Lambda
- Amazon DynamoDB
- Amazon Location Service
- Anthropic Claude Haiku 4.5
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-a-restaurant-telephony-ai-host-with-amazon-connect/
published_at: '2026-08-24'
---

## 概要

AWSは、電話をかけてきた顧客の注文をアプリ不要・ログイン不要で完結させるレストラン向け音声注文システムの構築方法を紹介する。Amazon ConnectとAmazon Connect Agentic Voiceで音声認識・合成を行い、Claude Haiku 4.5を使うAIエージェントが会話をオーケストレーションし、AgentCore GatewayとMCP経由でメニュー・注文・店舗検索のバックエンドを呼び出す。電話チャネルとバックエンドロジックを疎結合に保つことで、注文ロジックはチャネルに依存せず再利用できる。

## 設計のポイント

- 電話・音声・AIエージェントの3層をAmazon Connectに統合しつつ、バックエンド(メニュー/カート/注文)はAPI Gateway+Lambdaの別モジュールとして分離する
- OpenAPIスキーマからAgentCore GatewayがMCPツールを自動登録し、バックエンドの変更がエージェント側の変更を必要としない疎結合を実現する
- 発信者の電話番号をLambdaでセッションに注入し、ログイン無しで顧客を識別する
- AI Guardrailでコンテンツフィルタ・禁止トピック・不適切表現を排除し、会話を安全な範囲に保つ

## 使いどころ

- 電話注文の比率が高く、スタッフが対応に追われる飲食店・小売店
- アプリやWebサイトを持たない、または持てない事業者が音声チャネルでAI対応を追加したい場合
- MCP経由で既存の業務システムをエージェントに接続したい場合の参考アーキテクチャとして
