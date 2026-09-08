---
type: case
title: HPE Zertoのエージェント型障害トラブルシューティングシステム
title_original: How HPE Zerto built an agentic troubleshooting system with Amazon Bedrock
company: HPE Zerto
industry: cross-industry
cloud:
- aws
- on-prem
patterns:
- ai-agent
- multi-agent-orchestration
- rag
- guardrails
components:
- Amazon Bedrock
- Amazon Bedrock Guardrails
- Amazon Bedrock Knowledge Bases
- Strands Agents
- MCP
- Amazon CloudWatch
- Amazon DynamoDB
- AWS Lambda
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-hpe-zerto-built-an-agentic-troubleshooting-system-with-amazon-bedrock/
published_at: '2026-09-08'
---

## 概要

HPE ZertoがAmazon Bedrock上にオーケストレーターと専門サブエージェントからなるエージェント型トラブルシューティングシステムを構築し、オンプレミス環境のZerto製品内にポッドとして組み込んだ。MCP経由でZVM APIやBedrock Knowledge Basesのドキュメントにアクセスし、自然言語での障害調査・復旧支援を実現する。

## 設計のポイント

- Orchestratorが定型質問には直接回答し、ログの多い深掘り調査は専門サブエージェントに委譲して親のコンテキストを汚染しない
- 内部MCPサーバーでZVM APIへの構造化アクセス、Bedrock Knowledge Basesでドキュメント検索を明確に分離する
- Bedrock Guardrailsを推論の前後に適用し、CloudWatch/DynamoDB/Lambdaでテナント別のクォータとコストを制御する

## 使いどころ

- 複数サイト・大量ワークロードのディザスタリカバリ運用で障害調査を高速化したい場合
- オンプレ製品にAIアシスタントを安全に組み込みたいソフトウェアベンダー
