---
type: guidance
title: SageMaker エンドポイント更新時のオートスケーリングをCDKカスタムリソースで制御する
title_original: Orchestrating SageMaker AI endpoint auto scaling with AWS CDK
ai_relevant: false
company: AWS
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/orchestrating-sagemaker-ai-endpoint-auto-scaling-with-aws-cdk/
published_at: '2026-10-23'
---

## 概要

SageMakerエンドポイントの構成変更時は、スケーラブルターゲットの登録解除が必要なためCloudFormation/CDKデプロイが失敗する。登録解除・エンドポイント更新・再登録をカスタムリソースで順序制御する再利用可能なCDK constructを紹介する。
