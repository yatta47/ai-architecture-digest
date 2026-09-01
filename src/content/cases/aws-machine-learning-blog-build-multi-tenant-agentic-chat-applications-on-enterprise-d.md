---
type: guidance
title: マルチテナント対応のエンタープライズ文書チャットアプリケーションの構築
title_original: Build multi-tenant agentic chat applications on enterprise data with Amazon Bedrock Managed Knowledge Base
industry: cross-industry
cloud:
- aws
patterns:
- multi-tenant-rag
- rag
- document-processing
- ai-agent
components:
- Amazon Bedrock Managed Knowledge Base
- Amazon API Gateway
- AWS Lambda
- Amazon Cognito
- Amazon SQS
- Amazon DynamoDB
- Amazon S3
- Amazon CloudFront
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-multi-tenant-agentic-chat-applications-on-enterprise-data-with-amazon-bedrock-managed-knowledge-base/
published_at: '2026-08-31'
---

## 概要

ユーザーがアップロードした文書に対して質問できるマルチテナント型エージェントチャットの参照アーキテクチャを解説する記事。検証済みJWTからサーバー側でuser_idフィルタを組み立てることで、エージェントが複数回の検索を行っても各ホップでテナント分離が破れないようにしている。Managed Knowledge Baseがベクトル管理・埋め込み・エージェント型検索を肩代わりし、アプリ側はアップロードUIと認証・分離ロジックのみを担う。

## 設計のポイント

- テナント分離のフィルタ値はクライアント入力ではなく検証済みJWTからサーバー側で導出する
- アップロードとインジェストをSQSで疎結合にし、失敗メッセージをデッドレターキューへ退避してアップロードAPIの応答性を保つ
- DynamoDBでインジェスト状態を追跡し、received→processing→readyの遷移をUIにポーリングで反映する

## 使いどころ

- 顧客ごとに契約書・レポートなどを個別にアップロードして質問できるSaaS型ドキュメントチャットを提供したい場合
- 多段階の検索が発生してもテナント境界を厳格に維持する必要があるマルチテナントRAGを構築する場合
