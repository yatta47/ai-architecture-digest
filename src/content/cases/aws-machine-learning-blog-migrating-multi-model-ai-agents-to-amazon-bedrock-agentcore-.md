---
type: guidance
title: マルチモデル医療AIエージェントをAmazon Bedrock AgentCore runtimeへ移行する
title_original: Migrating multi-model AI agents to Amazon Bedrock AgentCore runtime
industry: healthcare
cloud:
- aws
patterns:
- ai-agent
- multi-model-routing
- unified-runtime
- rag
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock
- Amazon SageMaker AI
- Amazon OpenSearch Service
- Hugging Face smolagents
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/migrating-multi-model-ai-agents-to-amazon-bedrock-agentcore-runtime/
published_at: '2026-09-18'
---

## 概要

Amazon ECS/Fargate上で自己管理していた3モデル構成の医療AIエージェント（専門バイオメディカルモデル・FM・自己ホスト型モデルサーバー）を、エージェントロジックを変更せずAmazon Bedrock AgentCore runtimeへ移行する事例。BYOエージェント方式のためコンテナのライフサイクル・スケーリング・ID管理・可観測性をAgentCoreに委譲でき、運用負荷を下げつつトリプルモデルオーケストレーションとベクトル検索によるナレッジ取得を維持できる。

## 設計のポイント

- クエリの性質ごとに専門バイオメディカルモデル・汎用FM・自己ホスト型モデルサーバーの3バックエンドへルーティングし、それぞれをHugging Face Messages API互換にして呼び出し方式を統一する
- AgentCore runtimeのデコレータパターンで既存のsmolagentsベースのコードをそのままラップし、フレームワーク非依存のBYOエージェントとして持ち込む
- ベクトル類似検索によるナレッジ取得はAmazon OpenSearch Serviceに担わせ、モデル選択とは独立させて再利用しやすくする

## 使いどころ

- 自己管理コンテナ基盤（ECS/EKS等）で運用中のマルチモデルエージェントを、ロジックを書き換えずに管理型ランタイムへ移行したいチーム
- 医療・金融など複数の専門モデルとFMを使い分ける必要があるドメイン特化エージェントを構築するチーム
- ID・可観測性・スケーリングの実装を自前で持ちたくないがフレームワークの自由度は維持したいチーム
