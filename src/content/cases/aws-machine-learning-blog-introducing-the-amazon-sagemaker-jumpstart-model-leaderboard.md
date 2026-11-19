---
type: announcement
title: JumpStart Model Leaderboardで品質・速度・コストを同条件で比較
title_original: Introducing the Amazon SageMaker JumpStart Model Leaderboard
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- eval
- inference-optimization
components:
- Amazon SageMaker JumpStart
- Amazon SageMaker Studio
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-sagemaker-jumpstart-model-leaderboard/
published_at: '2026-11-18'
---

## 概要

SageMaker JumpStartに、70以上のLLMを品質、速度、コストで横並び比較できるModel Leaderboardが追加された。品質はAWSが3つの公開ベンチマークを同一条件で実行し、性能とコストは標準ワークロードで計測している。

## 設計のポイント

- 全モデルを同一の評価設定と計測方法で比べ、数値の比較可能性を確保する。
- 品質とあわせて、デプロイ構成別の速度とコストを見せる。
- 一覧から絞り込みデプロイまでを同じ画面で進める。

## 使いどころ

- オープンウェイトモデルの候補選定を行うとき。
- 用途に対する費用対効果を事前に見積もりたいとき。
