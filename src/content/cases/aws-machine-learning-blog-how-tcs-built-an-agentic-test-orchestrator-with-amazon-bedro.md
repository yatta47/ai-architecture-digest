---
type: case
title: TCSのBFSI向けマルチテナント・エージェント型テスト自動生成基盤
title_original: How TCS built an agentic test orchestrator with Amazon Bedrock AgentCore
company: Tata Consultancy Services
industry: financial-services
cloud:
- aws
patterns:
- multi-agent-orchestration
- multi-tenant-rag
- ai-agent
- context-engineering
components:
- Amazon Bedrock AgentCore
- Strands Agents SDK
- Amazon Bedrock Knowledge Bases
- Amazon EKS
- Amazon ECS
- Amazon Cognito
- AWS KMS
- Amazon DynamoDB
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-tcs-built-an-agentic-test-orchestrator-with-amazon-bedrock-agentcore/
published_at: '2026-11-10'
---

## 概要

TCSは要件(Jira/BRD/Swagger等)からテストシナリオ、Gherkin、実行可能テストを生成・実行するエージェント型テストオーケストレーターをAgentCore上に構築した。タスクごとに専用エージェントを置き、決定論的なスーパーバイザーでルーティングする。テナントごとにデータ・鍵・IDを分離したマルチテナントSaaSである。

## 設計のポイント

- 共有コントロールプレーンとテナント別アプリケーションプレーン(namespace/Cognito/KMS/S3/DynamoDB/Knowledge Base)を分離し、プール型コンピュートとサイロ型データを両立する。
- 検索をテナント・プロジェクト・セッションでフィルタしてからエージェントに渡し、案件固有のコンテキストで生成を接地する。
- タスク別エージェントを決定論的スーパーバイザーと実行ワークフロー(リトライ・エラー分類・永続化)で束ね、単一プロンプトの限界を避ける。
- AgentCoreのmicroVMによるセッション分離で、マルチテナントの分離層を自作せずに済ませる。

## 使いどころ

- 金融系など規制業界でテスト工数を削減したいQAチーム
- マルチテナントSaaSでエージェントを安全に提供したいプラットフォーム担当
- 要件変更で陳腐化するテストスクリプトの保守を減らしたい組織
