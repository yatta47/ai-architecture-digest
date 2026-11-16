---
type: guidance
title: Bedrock GuardrailsのDenied Topicsを意図ベースで書く8つのベストプラクティス
title_original: Best practices for writing Denied Topics in Amazon Bedrock Guardrails
industry: financial-services
cloud:
- aws
patterns:
- guardrails
- eval
components:
- Amazon Bedrock Guardrails
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/best-practices-for-writing-denied-topics-in-amazon-bedrock-guardrails/
published_at: '2026-11-16'
---

## 概要

Denied Topicsは意味で判定するため、主題領域で書くと正当な問い合わせまで遮断する。ユーザーの意図と行為で名前・定義・例を書く8つの指針を、架空の銀行チャットボットで示す。結果は完全には決定的でない点も注意する。

## 設計のポイント

- トピックは主題領域ではなく、拒否したい意図・行為に基づいて命名する
- キーワード列挙の定義を避け、意味で書く
- 例文は言い換えの重複や固有名詞を避け、境界を教える
- トピック同士の重複を避け干渉を防ぐ

## 使いどころ

- 顧客向けチャットボットのガードレール設計
- 過剰遮断と取りこぼしの調整
