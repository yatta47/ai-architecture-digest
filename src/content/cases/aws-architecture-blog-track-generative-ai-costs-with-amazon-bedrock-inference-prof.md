---
type: guidance
title: Bedrock application inference profilesで部門別に生成AIコストを可視化する
title_original: Track generative AI costs with Amazon Bedrock inference profiles
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- llm-gateway
components:
- Amazon Bedrock
- Amazon Bedrock Application Inference Profiles
- AWS Cost Explorer
- AWS Billing and Cost Management
- AWS CloudFormation
outcome:
  type: cost
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/track-generative-ai-costs-with-amazon-bedrock-inference-profiles/
published_at: '2026-08-13'
---

## 概要

複数部門が単一の基盤モデルを共有すると、Bedrockの利用料が1行の請求にまとまってしまい部門別の予算管理ができない課題を、タグ付きのapplication inference profileで解決する方法を解説。同一モデルに部門ごとのタグ付きラッパーを作り、Cost Explorerでチーム別の内訳を確認できるようにする。

## 設計のポイント

- 呼び出し元IAMロールが単一でも、inference profileのARNをmodelIdとして渡すだけで部門別コスト帰属ができる
- コスト配分タグをTeamのようなキーで付与し、Billing and Cost Management側で有効化することでCost Explorerに反映させる
- 数十チーム規模ではAWS::Bedrock::ApplicationInferenceProfileのCloudFormationリソースで一括プロビジョニングする

## 使いどころ

- 単一のIAMロール配下で複数部門が同じ基盤モデルを利用しており、チャージバックができていない組織
- 生成AI利用料の部門別予算管理やコスト最適化を行いたいFinOpsチーム
