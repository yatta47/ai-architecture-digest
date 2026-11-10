---
type: announcement
title: Amazon BedrockでClaude Fable 5.2とMythos 5.2が利用可能に
title_original: Introducing Claude Fable 5.2 on AWS
company: Anthropic / AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- multi-model-routing
components:
- Claude Fable 5.2
- Claude Mythos 5.2
- Amazon Bedrock
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-claude-fable-5-2-on-aws/
published_at: '2026-11-09'
---

## 概要

Claude Fable 5.2とMythos 5.2がAmazon BedrockとClaude Platform on AWSで利用可能になった。Fable 5.2は長時間の自律作業やコーディングに強く、拒否時のフォールバックは呼び出し側で実装する。

## 設計のポイント

- 拒否時は別モデルへ再試行する処理をアプリ側で持つ。
- フォールバッククレジットでキャッシュ二重課金を避ける。

## 使いどころ

- 大規模コードベースの自律コーディング
- サブエージェントを束ねる長時間エージェント
