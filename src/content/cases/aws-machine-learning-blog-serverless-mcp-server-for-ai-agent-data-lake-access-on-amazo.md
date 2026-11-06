---
type: case
title: データレイクへのエージェント非依存なサーバーレスMCPゲートウェイ
title_original: Serverless MCP server for AI agent data lake access on Amazon ECS Fargate
company: Amazon
industry: logistics
cloud:
- aws
patterns:
- text-to-sql
- llm-gateway
- guardrails
components:
- Amazon ECS
- AWS Fargate
- FastMCP
- Amazon Bedrock
- Amazon Bedrock Guardrails
- Amazon Bedrock Knowledge Bases
- Amazon Athena
- Amazon Redshift
- Amazon DynamoDB
- Amazon Cognito
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/serverless-mcp-server-for-ai-agent-data-lake-access-on-amazon-ecs-fargate/
published_at: '2026-11-06'
---

## 概要

Amazon北米ソートセンターの計画チーム向けに、データレイクへ会話的にアクセスさせるMCPサーバーをECS Fargate上に構築した事例。JSONメタデータを置くだけで新規データセットを公開でき、アクセス制御もMCPサーバー層で一元化する。

## 設計のポイント

- メタデータカタログからスキーマを実行時に参照させ、テーブル定義のハードコードと再デプロイを不要にしている。
- コンテキストマッピングで問い合わせ対象テーブルを絞り、SQL生成精度とレイテンシ(15〜20秒)を改善している。
- クライアント層とMCPサーバー層を別Fargateクラスタに分離し、状態はDynamoDBに置いてステートレスにスケールさせる。
- 権限強制とBedrock Guardrailsをサーバー層に集約し、エージェントごとの実装ばらつきを防ぐ。

## 使いどころ

- 複数エージェントが同じデータ基盤を使う社内でアクセス制御を一元化したい場面。
- 新規データセットの追加を数日から設定ファイル追加へ短縮したいデータ基盤チーム。
- SlackやIDEなど複数クライアントから同じツール群を使わせたい場合。
