---
type: case
title: AgentCoreでSQLスキーマからER図とコードセキュリティ解析を自動生成するAI-DLC実装
title_original: AI-driven development lifecycle using Amazon Bedrock AgentCore
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-agent-orchestration
- ci-cd
- human-in-the-loop
components:
- Amazon Bedrock AgentCore
- AgentCore Runtime
- AgentCore Gateway
- AgentCore Memory
- Strands Agents
- Amazon S3
- AWS Lambda
- Amazon Cognito
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/ai-driven-development-lifecycle-using-amazon-bedrock-agentcore/
published_at: '2026-09-03'
---

## 概要

AI-Driven Development Lifecycle（AI-DLC）をAmazon Bedrock AgentCoreで実装した2つのリファレンス構成を紹介する記事。SQLスキーマからMermaid ER図を自動生成するイベント駆動パイプラインと、AgentCore Gateway/Memoryを使ったマルチエージェントによるコードセキュリティ解析を、人間のレビューを介在させながら構築している。

## 設計のポイント

- S3イベント駆動でLambdaがAgentCore Runtimeを呼び出すサーバーレス構成にし、開発フローにドキュメント生成を組み込む
- 大きなSQLファイルはチャンク分割して個別解析後に統合することでコンテキスト制限を回避する
- AgentCore Memoryで90日保持のセッションコンテキストを持たせ、過去解析のセマンティック検索を可能にする
- OpenTelemetryで各処理ステップにトレースを付与し、処理時間やエラー原因を可観測にする

## 使いどころ

- スキーマ変更のたびにドキュメントが陳腐化するデータベースチームのER図自動更新
- CI/CDパイプラインに組み込むコードのセキュリティ・CVE・ポリシー準拠チェックの自動化
- 人間の意思決定を保ちつつAIにルーチン作業を任せたい開発チーム
