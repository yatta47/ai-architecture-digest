---
type: announcement
title: AgentCore harnessがStrands harness・組込ツール・ライフサイクルフックに対応
title_original: Amazon Bedrock AgentCore harness adds Strands harness defaults, built-in tools, and lifecycle hooks
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- context-engineering
- guardrails
components:
- Amazon Bedrock AgentCore
- Strands Agents
- AgentCore runtime
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-harness-adds-strands-harness-defaults-built-in-tools-and-lifecycle-hooks/
published_at: '2026-11-19'
---

## 概要

AgentCore harnessがオープンソースのStrands harnessを基盤にし、推奨モデル、プロンプトキャッシュ、文脈管理、計画・Web取得・ファイル操作・委譲の組込ツールを標準で備えた。エージェントループの要所で決定的な処理を挟むライフサイクルフックも加わった。

## 設計のポイント

- フックで非決定的なエージェント動作に決定的な検査・通知を挟む。
- 文脈のオフロードと自動プロンプトキャッシュで長時間タスクのコンテキスト消費を抑える。
- セッションはカーネル分離のmicroVMで実行する。

## 使いどころ

- 返金など重要な操作を含むエージェントを安全に運用したい開発者に向く。
