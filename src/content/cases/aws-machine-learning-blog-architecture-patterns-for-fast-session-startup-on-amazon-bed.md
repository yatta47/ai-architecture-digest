---
type: guidance
title: AgentCore Runtime V2でエージェントのセッション起動を高速化する4パターン
title_original: Architecture patterns for fast session startup on Amazon Bedrock AgentCore runtime
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- inference-optimization
components:
- Amazon Bedrock AgentCore Runtime
- Amazon ECR
- microVM
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/architecture-patterns-for-fast-session-startup-on-amazon-bedrock-agentcore-runtime/
published_at: '2026-11-13'
---

## 概要

AgentCore RuntimeのV2は、環境を一度初期化してスナップショット化し、各セッションで復元することで起動を速く安定させる。初期化をapp.run()前に寄せる、ビルドフック、ユーザー操作時の事前ウォームといったパターンで最初のリクエストの待ちを減らす方法を解説する。

## 設計のポイント

- 重い初期化はスナップショット作成時（app.run()前・ビルドフック）に済ませ、初回リクエストに持ち込まない。
- サブ秒が必要なチャットや音声では、ユーザーが操作を始めた時点でセッションをバックグラウンド起動する。
- V1ではイメージサイズに比例した起動時間がV2で一度きりの処理になる点を理解して選ぶ。

## 使いどころ

- ユーザーが初回応答を待つ対話型エージェント。
- チャットや音声UIで起動遅延を2秒未満にしたいチーム。
