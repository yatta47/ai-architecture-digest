---
type: case
title: 臨床ポリシーをマルチテナントAIエージェントで構造化データに変換する仕組み
title_original: How Cohere Health digitizes clinical policies using Amazon Bedrock AgentCore
company: Cohere Health
industry: healthcare
cloud:
- aws
patterns:
- ai-agent
- document-processing
- human-in-the-loop
- llmops
components:
- Amazon Bedrock AgentCore
- AgentCore Gateway
- AgentCore Memory
- LangChain
- Arize AX
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-cohere-health-digitizes-clinical-policies-using-amazon-bedrock-agentcore/
published_at: '2026-08-07'
---

## 概要

Cohere Healthは、健康保険プランの事前承認業務で使われる非構造の臨床ポリシー文書を機械可読データへ変換するため、Amazon Bedrock AgentCore上にマルチテナント型のエージェント基盤「Cohere Policy Studio」を構築した。AgentCore RuntimeのマイクロVM分離でテナントごとのデータ隔離を確保しつつ、Gatewayでツールとスキルへのアクセスを一元化し、Memoryで担当者のフィードバックループを支えている。

## 設計のポイント

- 共通のベースコンテナイメージにチーム固有の設定ファイルを重ねる二層構成にし、ランタイムを再構築せずに複数チームへ横展開する
- AgentCore Runtimeのセッション単位マイクロVM分離で、顧客ごとに厳密なデータ境界を確保する
- AgentCore Gatewayの背後にLambdaベースのツールと社内APIをMCP経由で集約し、エージェント再デプロイなしにツールを追加できるようにする
- 臨床ポリシー専門家と共同でスキルを作成し、標準化された観測基盤で評価してから展開する

## 使いどころ

- 複数の医療保険プラン顧客に同じ基盤を提供しつつ、テナントごとの厳格な分離が必要な場合
- 非構造の規約・ポリシー文書を継続的に構造化データへ変換し、人手レビューを介在させたい業務
- チームごとに異なるエージェント設定を持たせつつ共通ランタイムを維持したいプラットフォームチーム
