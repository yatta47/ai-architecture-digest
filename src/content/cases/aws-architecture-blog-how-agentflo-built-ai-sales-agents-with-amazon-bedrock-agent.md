---
type: case
title: AgentFloがAmazon Bedrock AgentCoreで構築したAIセールスエージェント基盤
title_original: How AgentFlo built AI sales agents with Amazon Bedrock AgentCore – Part 1
company: AgentFlo (Salesflo)
industry: retail
cloud:
- aws
patterns:
- ai-agent
- llm-gateway
- guardrails
- event-driven
components:
- Amazon Bedrock AgentCore
- Strands Agents SDK
- AWS Fargate
- Amazon DynamoDB
- Amazon Aurora
- Amazon Kinesis
- Amazon S3
- AgentCore Gateway
- AgentCore Identity
- Amazon Bedrock Guardrails
- Amazon Data Firehose
outcome:
  type: revenue
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-agentflo-built-ai-sales-agents-with-amazon-bedrock-agentcore-part-1/
published_at: '2026-08-20'
---

## 概要

eコマース向けエージェント型コマースサービスAgentFlo（Salesflo）は、WhatsAppなどのチャネルで常時稼働するAIセールス・サポート・注文エージェントを、Strands Agents SDKとAmazon Bedrock AgentCore上に構築した。年間3000億ドル超の取引を扱う加盟店基盤を支えるため、速度・標準化・スケーラビリティ・信頼・信頼性の5本柱でアーキテクチャを設計し、テナントごとに隔離されたエージェントランタイムとポリシーベースのガードレールで本番運用を実現している。

## 設計のポイント

- AWS Fargateのメッセージング層で認証・OCR・音声変換・プロンプトインジェクション検知を先に済ませ、検証済みリクエストのみAgentCoreランタイムへ流す
- 各エージェントセッションを専用の軽量VMで実行し、テナント間にハードウェアレベルの隔離境界を設けるAgentCore Runtimeを採用
- AgentCore Gatewayが標準化されたMCP接続でCart/Product/Knowledge BaseのLambda APIをツール化し、IAMベースで認可する
- レシピベースのデプロイモデルにより、ペルソナ・ツールセット・ナレッジ・業務ルールが事前設定された構成をマーチャントが選ぶだけでエージェントを立ち上げられる

## 使いどころ

- WhatsAppなど複数チャネルでカゴ落ちや対応漏れを減らしたいeコマース加盟店
- 業種の異なる複数のエージェント（セールス・受付・サポート・再注文など）をテンプレート的に量産したいプラットフォーム事業者
- ピーク時に平常の10〜50倍のトラフィックが発生するフラッシュセール等に耐えるスケーラブルな会話型コマース基盤が必要な事業者
