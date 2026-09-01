---
type: guidance
title: 可観測性を組み込んだエンタープライズ向けエージェント型RAG基盤の構築
title_original: Build observable enterprise agentic retrieval using Managed Amazon Bedrock Knowledge Base with AWS CloudFormation
industry: cross-industry
cloud:
- aws
patterns:
- rag
- ai-agent
- eval
- multi-agent-orchestration
components:
- Amazon Bedrock Managed Knowledge Base
- Amazon Bedrock AgentCore
- Amazon Bedrock AgentCore Gateway
- AWS CloudFormation
- Amazon CloudWatch
- AWS X-Ray
- Amazon S3
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-observable-enterprise-agentic-retrieval-using-managed-amazon-bedrock-knowledge-base-with-aws-cloudformation/
published_at: '2026-08-31'
---

## 概要

複数のナレッジベースにまたがってエージェントが推論・ルーティング・反復検索を行う「エージェント型RAG」を、Managed Knowledge BaseとAgentCoreを組み合わせてCloudFormationで一括構築する記事。OpenTelemetryによる計装で全ステップを可観測化し、7層の観測とオンデマンド/継続的評価をあらかじめ設計に組み込む点が特徴。単発検索型RAGでは対応できない複雑な質問への回答精度向上を狙う。

## 設計のポイント

- エージェントの推論ループ自体をOpenTelemetryスパンで計装し、ブラックボックス化を防ぐ
- ナレッジベースごとに1つの検索ツールを用意し、AgentCore Gatewayがトピックに応じたルーティングをブローカーする
- 可観測性と評価を後付けではなく最初のCloudFormationスタックから設計に組み込む

## 使いどころ

- 複数のナレッジソースを横断する複雑な質問に、根拠付きで回答するRAGシステムが必要な場合
- エージェント型RAGの本番運用で挙動の可視化と継続的な品質評価が求められる場合
