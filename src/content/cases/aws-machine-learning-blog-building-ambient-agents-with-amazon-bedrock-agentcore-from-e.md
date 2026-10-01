---
type: guidance
title: Bedrock AgentCoreでイベント駆動のアンビエントエージェントを構築しHITLを組み込む
title_original: 'Building ambient agents with Amazon Bedrock AgentCore: From event-driven signals to human-in-the-loop workflows'
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- event-driven
- human-in-the-loop
components:
- Amazon Bedrock AgentCore
- AgentCore Runtime
- Amazon S3
- AWS Lambda
- Amazon DynamoDB
- Amazon SQS
- Amazon API Gateway
- Amazon Cognito
- AWS CDK
- Claude Sonnet 4.5
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-ambient-agents-with-amazon-bedrock-agentcore-from-event-driven-signals-to-human-in-the-loop-workflows/
published_at: '2026-10-01'
---

## 概要

S3イベントやスケジュールなどのシステムイベントをトリガーに、チャットを介さずエージェントが動き出す「アンビエントエージェント」のパターンを、Amazon Bedrock AgentCoreのリファレンス実装で解説した記事。イベントはシグナルとしてジョブ化され、AgentCore Runtime上のエージェントが処理し、承認や確認が必要な時だけ単一のask_humanツールで人に問い合わせて再開する。Lambda、DynamoDBと組み合わせたサーバーレス構成になる。

## 設計のポイント

- イベントソースとエージェントを対応づけるシグナルという設定単位を設け、イベントが来ると自動でジョブが作られるようにした。
- autoExecuteのfalse(既定)で人がレビューしてから実行するフローにし、不明なイベントでも安全に運用できるようにした。
- 単一のask_humanツールと標準の応答エンベロープだけで、多様なHITL対話を扱える。
- AgentCore Runtimeのセッション分離と長時間実行を利用し、Lambda、DynamoDBで状態管理するサーバーレス構成にした。

## 使いどころ

- ファイルがストレージに届くたびに人手でトリアージしている文書処理パイプライン。
- 監視アラートへの一次対応を自動化しつつ、重要な判断だけ人に委ねたい運用。
- 承認ゲートを含む複数ステップのワークフロー。
