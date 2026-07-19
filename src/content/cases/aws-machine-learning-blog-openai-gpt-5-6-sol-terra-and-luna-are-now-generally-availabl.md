---
type: announcement
title: OpenAI GPT-5.6ファミリーがAmazon Bedrockで一般提供開始
title_original: OpenAI GPT-5.6 Sol, Terra, and Luna are now generally available on Amazon Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- multi-model-routing
- inference-optimization
- llm-gateway
components:
- Amazon Bedrock
- GPT-5.6 Sol
- GPT-5.6 Terra
- GPT-5.6 Luna
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/openai-gpt-5-6-sol-terra-and-luna-are-now-generally-available-on-amazon-bedrock/
published_at: '2026-07-13'
---

## 概要

OpenAIのGPT-5.6ファミリー(Sol/Terra/Luna)がAmazon Bedrockで一般提供開始。次世代推論エンジンによるプロンプトキャッシュ、ゼロオペレータアクセス(ZOA)によるチップレベルのセキュリティ、リージョン内推論など、エンタープライズ向け要件に対応する。

## 設計のポイント

- Sol(フラッグシップ推論)/Terra(バランス型)/Luna(高速・安価)という3つの能力・コスト層を用意し、ワークロードごとに使い分けられるようにする。
- 明示的なキャッシュブレークポイントでシステム指示やツール定義など繰り返されるコンテキストを90%割引で再利用し、エージェントの連続呼び出しコストを抑える。
- ZOA(zero-operator access)によりチップレベルでAWS運用者からもプロンプト/completionへのアクセスを遮断する。

## 使いどころ

- バースト性の高いエージェントトラフィックを予測可能なコストで捌きたいチーム。
- データレジデンシー要件が厳しい規制業種でフロンティアLLMを利用したい組織。
