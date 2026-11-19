---
type: case
title: Airbnbがタスク当たりコストでコーディングエージェントのモデルを選ぶ
title_original: How Airbnb uses cost per task to operate coding agents on Amazon Bedrock
company: Airbnb
industry: other
cloud:
- aws
patterns:
- llmops
- eval
- llm-gateway
- cost-optimization
components:
- Amazon Bedrock
- Amazon CloudWatch
- AirChat
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-airbnb-uses-cost-per-task-to-operate-coding-agents-on-amazon-bedrock/
published_at: '2026-11-18'
---

## 概要

Airbnbは社内のコーディングエージェント基盤AirChatで、LLMゲートウェイ経由でBedrockを使う。展開前は自社タスクのevalでスコアとタスク当たりコストを測り、展開後はCloudWatchの指標でレイテンシ、スロットリング、支出を見て、モデル選択を見直している。

## 設計のポイント

- 公開ベンチマークでなく、自社タスクでスコアとタスク当たりコストを測る。
- 展開前のevalと展開後のオブザーバビリティを両輪にする。
- LLMゲートウェイを置き、モデル切替を一箇所で行う。
- レイテンシ、スロットリング、トークン消費を継続的に見る。

## 使いどころ

- 新モデルが次々出る中でコーディングエージェントのモデルを選ぶ組織。
- エージェント利用のコストを管理する基盤チーム。
