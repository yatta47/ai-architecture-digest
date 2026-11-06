---
type: guidance
title: Claude CodeをAgentCoreのリモートセッションで安全に動かす構成
title_original: Extend Claude Code to remote sessions on Amazon Bedrock AgentCore with security controls
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-model-routing
- guardrails
- human-in-the-loop
components:
- Claude Code
- Amazon Bedrock AgentCore
- AgentCore runtime
- AgentCore Identity
- AgentCore memory
- Amazon Bedrock Guardrails
- Amazon API Gateway
- Amazon SQS
- Amazon DynamoDB
- AWS Lambda
- GitHub
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/extend-claude-code-to-remote-sessions-on-amazon-bedrock-agentcore-with-security-controls/
published_at: '2026-11-06'
---

## 概要

Claude CodeをAgentCore runtimeのmicroVMセッションで走らせ、コーディングタスクをリモートに任せてPRで受け取るサンプル構成の解説。Bedrockのデータ保護や監査ログを保ったまま、タスクごとに隔離環境で実行する。

## 設計のポイント

- タスクごとにmicroVM隔離のセッションを割り当て、手元の資格情報から切り離す。
- 計画と評価に上位モデル、実装に別モデルを使い分け、レビューで最大3回まで再計画する。
- AgentCore memoryにリポジトリ固有の学びを蓄積し、後続タスクで再利用する。
- エージェントはマージせず、検証結果付きのPR(未検証はドラフト)で人のレビューに渡す。

## 使いどころ

- 並行して複数のコーディングタスクをオフロードしたい開発チーム。
- IAM/PrivateLinkなど既存のAWS統制の下でコーディングエージェントを使いたい組織。
- 信頼できるリポジトリの機能追加・バグ修正・テスト追加。
