---
type: case
title: SageMaker AIとBedrock AgentCoreを組み合わせたマルチエージェント個人金融アシスタント
title_original: Building agentic workflows with SageMaker AI and Bedrock AgentCore
industry: financial-services
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- multi-model-routing
components:
- Amazon SageMaker AI
- Amazon Bedrock AgentCore
- Amazon Bedrock
- Strands Agents
- Qwen 3.5 9B
- Claude Haiku 4.5
- Claude Sonnet 4.6
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/building-agentic-workflows-with-sagemaker-ai-and-bedrock-agentcore/
published_at: '2026-08-14'
---

## 概要

Bedrock上のClaudeモデルとSageMaker AIにホストした独自モデル(Qwen 3.5 9B)を、Strands Agentsの「agents as tools」パターンで束ねたマルチエージェント構成をBedrock AgentCoreランタイムにデプロイする方法を示す。オーケストレータがユーザー意図を分類し、予算エージェントと金融分析エージェントにルーティングすることで、タスクごとにコストとモデル特性を最適化する。SageMaker OpenAI互換エンドポイントにはデフォルトでトークン計測が効かないため、独自にオブザーバビリティを補う手順も扱う。

## 設計のポイント

- 汎用タスクはBedrockのマネージドFM、コスト最適化やドメイン特化が必要なタスクはSageMaker AIの自前モデルというようにモデルホスティング先をタスクごとに使い分ける
- Strands Agentsのagents-as-toolsパターンでオーケストレータ配下に専門エージェントをツールとして接続し、フレームワークを書き換えずに複数モデルを統合する
- SageMakerのOpenAI互換APIはベアラートークンが失効するため、httpx.Authサブクラスでリクエスト毎にトークンを自動更新する
- Bedrock呼び出しは自動でOpenTelemetryのトークン計測が付くが、SageMakerエンドポイントは計測が欠落するため独自の計装が必要になる

## 使いどころ

- マネージドFMとコスト最適化された自前モデルを1つのエージェントシステムに共存させたいチーム
- データレジデンシーやコストの理由で特定タスクだけ自前ホスティングモデルに切り出したい場合
- AgentCoreランタイムでマルチエージェントを本番運用しつつコストとレイテンシを可視化したいプラットフォームチーム
