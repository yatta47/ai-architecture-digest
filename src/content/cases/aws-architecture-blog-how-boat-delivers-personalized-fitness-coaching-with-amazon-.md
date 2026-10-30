---
type: case
title: boAtのスマートウォッチ向けBedrock利用パーソナライズAIコーチ
title_original: How boAt delivers personalized fitness coaching with Amazon Bedrock
company: boAt (Imagine Marketing Limited)
industry: retail
cloud:
- aws
patterns:
- cost-optimization
- event-driven
components:
- Amazon Bedrock
- AWS Lambda
- Amazon RDS for MySQL
- Amazon DocumentDB
outcome:
  type: revenue
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-boat-delivers-personalized-fitness-coaching-with-amazon-bedrock/
published_at: '2026-10-29'
---

## 概要

boAtはスマートウォッチの歩数・活動・睡眠データと利用者の好みや目標、履歴をもとにAmazon BedrockとLambdaでパーソナライズされたコーチングプランを生成するAIコーチを構築した。6か月以上本番稼働しインド全土の数百万ユーザーに提供しており、個別最適化・低コスト・スケーラビリティを設計原則とした。

## 設計のポイント

- 端末とアプリで集めたデータ、履歴、ユーザーの希望する伝え方をプロンプトの文脈として組み合わせて個別化する。
- Lambdaなどサーバーレスで構成し、利用量に応じたコストとスケーラビリティを確保する。
- 生成AIによる推奨を、ユーザーが実行しやすく価値が伝わる形に整える。

## 使いどころ

- 消費者向けデバイスで大量ユーザーに個別提案を提供したい事業者。
- コストに敏感な環境で生成AI機能を本番運用したい場面。
