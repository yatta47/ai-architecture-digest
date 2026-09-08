---
type: guidance
title: AgentCore×GitHub ActionsによるAIエージェントの自動評価CI品質ゲート
title_original: Automated agent evaluation with Amazon Bedrock AgentCore and GitHub Actions
industry: cross-industry
cloud:
- aws
patterns:
- eval
- ci-cd
- ai-agent
components:
- Amazon Bedrock AgentCore
- Strands Agents
- MCP
- GitHub Actions
- Amazon Cognito
- AWS CDK
- Amazon CloudWatch
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/automated-agent-evaluation-with-amazon-bedrock-agentcore-and-github-actions/
published_at: '2026-09-08'
---

## 概要

GitHub ActionsからAgentCore runtime上のエージェントをデプロイし、AgentCore EvaluateのLLM-as-judge評価で応答品質をスコアリングして、スコアが閾値を下回るとPRをブロックするCI/CD品質ゲートの構築方法を解説する。ロールベースアクセス制御のMCPサーバーに対して、CIからOAuthのM2M認証で疎通する方法も扱う。

## 設計のポイント

- OpenTelemetryトレースをCloudWatch経由でAgentCore Evaluateに渡しHelpfulness等の built-in evaluatorでスコアリングする
- GitHub ActionsのOIDCフェデレーションで長期クレデンシャルを持たずAWS IAMロールを引き受ける
- ユーザーコンテキストのないCIパイプラインはOAuthのclient_credentials(M2M)フローで認証する
- 評価スコアが最低ラインを下回った場合にマージをブロックする品質ゲートをパイプラインに組み込む

## 使いどころ

- システムプロンプトやモデル変更のたびに手動テストせず回帰を自動検知したいチーム
- OAuth保護されたMCPツールを使うエージェントをCIで継続的に評価したい場合
