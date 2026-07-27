---
type: case
title: IAM一時委任で実現するセルフホスト音声AIのサポート高速化
title_original: Deepgram enhances Amazon SageMaker AI support with AWS IAM Temporary Delegation
company: Deepgram
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- human-in-the-loop
- policy-as-code
components:
- Amazon SageMaker AI
- AWS IAM
- AWS STS
- AWS CloudTrail
- Amazon SNS
- AWS Marketplace
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/deepgram-enhances-amazon-sagemaker-ai-support-with-aws-iam-temporary-delegation/
published_at: '2026-07-27'
---

## 概要

Deepgramはセルフホスト型音声AIモデルをAmazon SageMaker AI上で提供する一方、サポート時に長期的なクロスアカウントIAMロールを発行する運用負担が課題だった。新しいIAM Temporary Delegation機能と統合し、顧客が自身のIAMコンソールで完全に解決済みの権限内容を確認・承認するだけで、時間制限付きの一時STSクレデンシャルをDeepgramエンジニアに発行できるようにした。この結果、SageMaker AIサポートチケットの初動調査時間が数日から数分に短縮された。

## 設計のポイント

- エンドポイントARN1つに権限範囲を限定した事前登録済みパーミッションテンプレートを用い、ワイルドカードのない完全解決済みの権限を顧客に提示する
- 長期的なクロスアカウントIAMロールや共有シークレットを排除し、承認のたびに短時間のSTSクレデンシャルを発行するモデルに置き換える
- 承認フローをセキュリティチームが使い慣れた顧客自身のIAMコンソールに置き、Amazon SNS経由でサポートチケットシステムと連携する
- すべての委任アクセスをCloudTrailにパートナーのアカウントIDとともに記録し、監査可能性を担保する

## 使いどころ

- データレジデンシーや規制対応のためにAIモデルをセルフホストしつつ、マネージドサービス並みの運用サポートを受けたい企業
- パートナーベンダーにクロスアカウントアクセスを都度発行・棚卸しする監査負担を減らしたいプラットフォームチーム
- GPUエンドポイントの挙動調査など、規制環境で操作の追跡可能性が求められるサポート業務
