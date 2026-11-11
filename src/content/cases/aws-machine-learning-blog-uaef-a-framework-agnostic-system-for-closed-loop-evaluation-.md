---
type: guidance
title: フレームワーク非依存でAIエージェントを継続評価するUAEF
title_original: 'UAEF: A framework-agnostic system for closed-loop evaluation of AI agents'
industry: cross-industry
cloud:
- aws
patterns:
- eval
- llmops
- ai-agent
components:
- Amazon DynamoDB
- Amazon S3
- LangGraph
- LangChain
- Strands Agents
- Amazon Bedrock AgentCore
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/uaef-a-framework-agnostic-system-for-closed-loop-evaluation-of-ai-agents/
published_at: '2026-11-11'
---

## 概要

UAEFは、LangGraphやStrands Agentsなど異なるフレームワークのトレースをアダプターで共通形式に変換し、7観点36種の組込みメトリクスで採点する評価基盤。結果はDynamoDBとS3に保存し、バージョン間比較で退行を検知してプロンプトやモデルの改善に繋げる。通信・医療・金融の12組織が利用したとされる。

## 設計のポイント

- アダプターで実行トレースを正規化し、評価ロジックをフレームワークから切り離す。
- 保存前にPIIをスクリーニングする。
- メタデータはDynamoDB、全結果はS3と役割を分け、ベースラインとの比較を容易にする。
- ツール呼び出し・応答品質・RAI・マルチターンなど複数観点で測り、単一の精度指標に頼らない。

## 使いどころ

- 複数のエージェントフレームワークを併用し評価を共通化したいチーム。
- プロンプトやモデル変更の効果をリリース前に比較したい場面。
