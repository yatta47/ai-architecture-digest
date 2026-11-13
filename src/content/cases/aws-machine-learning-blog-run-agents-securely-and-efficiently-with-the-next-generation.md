---
type: announcement
title: 次世代AgentCoreランタイムによる安全で効率的なエージェント実行
title_original: Run agents securely and efficiently with the next generation AgentCore runtime
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- defense-in-depth
- cost-optimization
components:
- Amazon Bedrock AgentCore
- AgentCore runtime
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/run-agents-securely-and-efficiently-with-the-next-generation-agentcore-runtime/
published_at: '2026-11-12'
---

## 概要

Amazon Bedrock AgentCoreのランタイムが、セッションごとの強い分離、高速起動、弾力的スケール、利用ベース課金を両立する次世代版として紹介された。事前確保によるアイドルコストとオンデマンドのコールドスタートのトレードオフを解消することを狙う。

## 設計のポイント

- エージェントセッションごとに隔離環境を用意する。
- アイドル費用とコールドスタートの二択を避ける設計を取る。
- マネージドなコンピュート層でサンドボックス自作を不要にする。

## 使いどころ

- 数千の同時エージェントセッションを運用する企業。
- コード実行やブラウザ操作をするエージェントを安全に動かしたいチーム。
