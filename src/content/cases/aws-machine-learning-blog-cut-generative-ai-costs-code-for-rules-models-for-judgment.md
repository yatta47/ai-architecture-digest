---
type: guidance
title: 生成AIコスト削減：ルールはコード、判断だけモデルに
title_original: 'Cut generative AI costs: Code for rules, models for judgment'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- multi-model-routing
components:
- Amazon Bedrock
- Amazon API Gateway
- AWS Lambda
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/cut-generative-ai-costs-code-for-rules-models-for-judgment/
published_at: '2026-11-17'
---

## 概要

ワークフローの各ステップに対し、ルールで判定できるか、モデルでルールを一度作れるか、固定リストから選ぶだけかを順に問い、必要な場合のみ右サイズのモデルを使う判断フローを提示する。不要なモデル呼び出しを減らしてコスト、遅延、非決定性を抑える。

## 設計のポイント

- 各ステップに「モデルが必要か」を最初に問う。
- ルールを高速パスとして先に実行する。
- 固定選択はConstrained decision call、開放的なタスクのみ右サイズモデルへ。

## 使いどころ

- プロトタイプ後に本番コストが膨らんだ生成AIシステム。
- 入力検証やルーティングをLLMに任せている設計の見直し。
