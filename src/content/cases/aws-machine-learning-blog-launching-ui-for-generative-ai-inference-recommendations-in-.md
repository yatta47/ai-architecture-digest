---
type: announcement
title: SageMaker AIの生成AI推論レコメンデーションUI
title_original: Launching UI for generative AI inference recommendations in Amazon SageMaker AI
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- cost-optimization
components:
- Amazon SageMaker AI
- Amazon SageMaker JumpStart
- Amazon S3
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/launching-ui-for-generative-ai-inference-recommendations-in-amazon-sagemaker-ai/
published_at: '2026-07-13'
---

## 概要

Amazon SageMaker AI Studioに生成AI推論レコメンデーションのローコード/ノーコードUIが追加され、ユースケースプロファイルと最適化目標(レイテンシ/スループット/コスト)を選ぶだけで、最適なインスタンス・コンテナ設定を数分〜数時間で得られるようになった。

## 設計のポイント

- Interact/Generate/Summarizeなどのプリセットユースケースプロファイルにより、トークン分布やコンカレンシーを毎回手動指定せずに済むようにする。
- 最適化目標(レイテンシ最小化/スループット最大化/コスト最小化)を選ぶと、ベンチマークとランキングのロジックが自動的に切り替わる。
- JumpStart・S3・Model Registry・既存デプロイなど複数のモデルソースを同一UIフローで受け付ける。

## 使いどころ

- インフラ専門知識がなくても生成AIモデルの本番デプロイ設定を検証したいMLエンジニア。
- コストとレイテンシのトレードオフを比較して意思決定したい技術リーダー。
