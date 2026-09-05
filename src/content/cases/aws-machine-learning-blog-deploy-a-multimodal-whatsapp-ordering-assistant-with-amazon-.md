---
type: case
title: WhatsAppひとつでテキスト・音声・通話を横断するマルチモーダル注文アシスタント
title_original: Deploy a multimodal WhatsApp ordering assistant with Amazon Bedrock AgentCore
industry: retail
cloud:
- aws
patterns:
- ai-agent
- voice-agent
- multi-agent-orchestration
- memory-consolidation
components:
- Amazon Bedrock AgentCore
- Amazon Nova 2 Lite
- Amazon Nova 2 Sonic
- Amazon Bedrock
- AWS Lambda
- Amazon API Gateway
- Amazon SQS
- Amazon DynamoDB
- Amazon Location Service
- Amazon Kinesis Video Streams
- Amazon VPC
- AWS Secrets Manager
- AWS Systems Manager Parameter Store
- Amazon ECR
- AWS CodeBuild
- Amazon S3
- Amazon CloudWatch
- AWS KMS
- AWS CDK
- Model Context Protocol (MCP)
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/deploy-a-multimodal-whatsapp-ordering-assistant-with-amazon-bedrock-agentcore/
published_at: '2026-09-04'
---

## 概要

飲食店のテキスト・音声メモ・音声通話という3チャネルを1つのWhatsApp Business番号に統合し、Amazon Bedrock AgentCore上のエージェントが注文を最初から最後まで処理するアーキテクチャ。チャネルとバックエンドの注文ロジックを分離し、AgentCore memoryでチャネル横断の顧客履歴を共有することで、テキストで注文した客を翌日の電話でも同一人物として認識できる。

## 設計のポイント

- チャネル（WhatsApp）とバックエンドの注文ロジックを分離し、チャネルの追加・削除でバックエンドを変更不要にする
- AgentCore GatewayでバックエンドREST APIをMCPツールとして公開し、複数エージェントから名前で統一的に呼び出す
- AgentCore memoryでハッシュ化した顧客IDをキーにチャネル横断の会話履歴を1つの記録として共有する
- Webhookは即座に200 ACKを返しSQSで非同期処理することで、後続処理が応答をブロックしないようにする

## 使いどころ

- アプリ・Web・電話・店頭で顧客体験と履歴が分断されている小売・飲食チェーン
- テキストと音声（メモ・通話）を同じ会話として扱うマルチモーダルなエージェント型接客を構築したい場合
- 既存の1つのバックエンドに複数のメッセージングチャネルを追加していきたい場合
