---
type: announcement
title: Amazon BedrockでOpenAI GPT-5.6ファミリー(Sol/Terra/Luna)が利用可能に
title_original: Get started with OpenAI GPT-5.6 Sol, Terra, and Luna on Amazon Bedrock
industry: cross-industry
cloud:
- aws
patterns:
- multi-model-routing
- llm-gateway
components:
- Amazon Bedrock
- OpenAI GPT-5.6 Sol
- OpenAI GPT-5.6 Terra
- OpenAI GPT-5.6 Luna
- AWS IAM
- AWS CloudTrail
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/get-started-with-openai-gpt-5-6-sol-terra-and-luna-on-amazon-bedrock/
published_at: '2026-07-24'
---

## 概要

OpenAIのGPT-5.6 Sol/Terra/Lunaの3モデルがbedrock-mantleエンドポイント経由でAmazon Bedrockから利用可能になった。OpenAI Responses APIをそのまま使いつつ、AWSのIAM・VPC・CloudTrailによるセキュリティ制御とリージョン内処理を得られる。

## 設計のポイント

- 用途別に3ティア(自律コーディング向けSol、汎用本番向けTerra、高速低コストのLuna)を用意し、reasoning effortパラメータで同一APIのままコスト/品質を調整できる
- 既存のOpenAI SDKアプリケーションはbase URLとモデルIDの差し替えだけでBedrock上に移行できる
- 全呼び出しがIAMポリシー・VPC内・CloudTrailログの対象となり、リージョン内処理でデータレジデンシー要件を満たせる

## 使いどころ

- 既存のOpenAI SDK資産を活かしつつAWSのガバナンス下でモデルを運用したいチーム
- エージェント型コーディングや長時間推論からレイテンシ重視の高頻度分類まで用途別にモデルを使い分けたい場合
