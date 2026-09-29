---
type: announcement
title: Grok 4.7がAmazon Bedrockで利用可能に
title_original: Grok 4.7 is now available on Amazon Bedrock
company: xAI
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- reinforcement-learning
components:
- Grok 4.7
- Amazon Bedrock
- Artificial Analysis
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/grok-4-7-is-now-available-on-amazon-bedrock/
published_at: '2026-09-28'
---

## 概要

xAIのGrok 4.7がAmazon Bedrockで利用可能になった。500Kトークンの文脈と4段階の推論強度を持ち、長時間のエージェント作業や自己検証を強みとする。ただしタスクあたりの出力トークンは前世代の約2倍で、推論強度を意識して設定する必要がある。

## 設計のポイント

- 長い試行での早期ミスの蓄積を抑えるため、自己検証するモデルを選ぶ。
- 推論強度を明示して品質とトークンコストのバランスを取る。
- クロスリージョン推論プロファイルとResponses・Converse APIなど複数のAPIで利用する。

## 使いどころ

- 長時間のコーディングやナレッジワークのエージェントを構築するチーム。
- Bedrock上で複数のフロンティアモデルを比較する基盤担当者。
- 出力トークンの増加を見込んでコストを見積もる担当者。
