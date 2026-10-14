---
type: guidance
title: AgentCore上のスーパーバイザーエージェントによるPowerPoint自動生成
title_original: Generate presentations with Amazon Bedrock AgentCore
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- rag
- document-processing
components:
- Amazon Bedrock AgentCore
- Strands Agents
- Claude Sonnet 4.6
- Amazon Titan Text Embeddings v2
- Amazon OpenSearch Serverless
- AWS Lambda
- Stability AI Stable Image Inpaint
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/generate-presentations-with-amazon-bedrock-agentcore/
published_at: '2026-10-14'
---

## 概要

四半期レポートなどからクライアント向けPPTXを作る作業を、AgentCore runtime上の単一スーパーバイザーエージェントが生成・要約ツールを切り替えて自動化する構成。OpenSearch ServerlessによるRAGで出典に基づく内容とし、社内テストでは90秒未満で完了する。

## 設計のポイント

- モノリシックな関数にせず、スーパーバイザーが生成・要約ツールへ振り分けるツールベース構成にする
- RAGのベクトル保管にOpenSearch Serverlessを使い、マルチモーダルな内容を検索可能にする
- VPC分離・KMS暗号化・IAM最小権限と.NETのREST APIで既存業務アプリに接続する

## 使いどころ

- 金融機関などでレポートから資料を量産する担当者
- 既存の業務システムにエージェント機能をAPIで組み込みたい開発チーム
