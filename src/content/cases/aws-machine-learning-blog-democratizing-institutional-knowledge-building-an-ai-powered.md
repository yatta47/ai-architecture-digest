---
type: guidance
title: 音声アバター×RAGで属人化した組織知を検索可能にするAWSナレッジ管理アクセラレータ
title_original: 'Democratizing Institutional Knowledge: Building an AI-Powered Knowledge Management System with AWS'
industry: cross-industry
cloud:
- aws
patterns:
- rag
- voice-agent
- cost-optimization
- document-processing
components:
- Amazon Bedrock Knowledge Bases
- Amazon Titan Text Embeddings
- Amazon OpenSearch Serverless
- Amazon DynamoDB
- AWS Lambda
- Amazon Cognito
- Amazon API Gateway
- Amazon S3
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/democratizing-institutional-knowledge-building-an-ai-powered-knowledge-management-system-with-aws/
published_at: '2026-08-24'
---

## 概要

AWSは、退職・異動で失われがちな『属人化した組織知(tribal knowledge)』を、音声対応のAIアバターとRAGで検索可能にするアクセラレータを紹介する。Amazon Bedrock Knowledge Basesがチャンク化・埋め込み(Titan Text Embeddings)・検索を担い、OpenSearch Serverlessをベクトルストアとして使う一方、DynamoDBによる回答キャッシュで再質問時の推論コストを50〜70%のキャッシュヒット率で削減する。CloudFormationで数時間でプロトタイプをデプロイできる設計になっている。

## 設計のポイント

- 非技術者の現場作業者向けに、テキストチャットではなく音声対話・アバターをフロントに据えることで学習コストと導入障壁を下げる
- ナレッジ保有者はS3にドキュメント(Word/PDF/Markdown/JSON等)をアップロードするだけで、リトリーバルパイプラインを自分で組む必要がない
- 頻出質問に対するDynamoDBキャッシュを挟み、可変の推論コストを削減しつつOpenSearch Serverlessの常時起動固定コストを別枠として把握する
- アバター技術自体は特定ベンダーに固定せず差し替え可能にし、Bedrock Knowledge Basesを介したRAGの根拠付けと分離する

## 使いどころ

- 熟練技術者が退職する前に、製造現場の手順書や保守プロトコルをハンズフリーで引き継ぎたい製造業
- 医療・金融・官公庁など、複数リポジトリに散在する規程・手順を自然言語で即座に参照したい現場
- 自前でBedrockベースの音声+RAG基盤を組む工数（数週間〜数か月）をかけずに、数時間でプロトタイプを立てたい場合
