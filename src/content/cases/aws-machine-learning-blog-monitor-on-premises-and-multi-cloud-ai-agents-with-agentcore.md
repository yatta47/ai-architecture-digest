---
type: guidance
title: 非AWS環境で動くAIエージェントをAgentCore Observabilityで一元監視する
title_original: Monitor on-premises and multi-cloud AI agents with AgentCore Observability
industry: cross-industry
cloud:
- aws
- multi-cloud
patterns:
- ai-agent
- llmops
components:
- Amazon Bedrock AgentCore
- Amazon Bedrock AgentCore Observability
- AWS Distro for OpenTelemetry (ADOT)
- Amazon CloudWatch
- AWS IAM
- Strands Agents
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/monitor-on-premises-and-multi-cloud-ai-agents-with-agentcore-observability/
published_at: '2026-08-13'
---

## 概要

オンプレミスや他クラウドで動くStrands Agents/LangGraph/CrewAI製エージェントに、AWS Distro for OpenTelemetry(ADOT)の自動計装を組み込みAgentCore Observabilityへテレメトリを送る方法を解説。IAM資格情報によるSigV4署名でCloudWatchのOTLPエンドポイントに送信し、AWS外で動くエージェントも単一ダッシュボードで可視化できるようにする。

## 設計のポイント

- ADOTの自動計装でboto3呼び出しとエージェントフレームワークの推論スパンをコード変更なしに取得する
- 非AWS環境ではIAMアクセスキーによるSigV4署名でOTLPエンドポイントを認証する
- OTel Gen AIセマンティック規約に沿ってツール呼び出し・トークン使用量まで記録し、既存のAgentCore Observabilityダッシュボードにそのまま統合する

## 使いどころ

- オンプレミスや他クラウド上のエージェントを含め、組織全体のAIエージェント挙動を単一ダッシュボードで監査したい場合
- ハルシネーションや有害出力を検知し、トークン使用量からコストを追跡したいプラットフォームチーム
