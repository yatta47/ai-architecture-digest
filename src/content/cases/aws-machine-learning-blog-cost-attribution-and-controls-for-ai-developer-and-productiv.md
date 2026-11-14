---
type: guidance
title: Bedrockの推論呼び出しをIAMプリンシパル単位でコスト帰属し統制する
title_original: Cost attribution and controls for AI developer and productivity tools on Amazon Bedrock
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- cost-optimization
- policy-as-code
components:
- Amazon Bedrock
- AWS IAM Identity Center
- CUR 2.0
- AWS Cost Explorer
- Amazon Athena
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/cost-attribution-and-controls-for-ai-developer-and-productivity-tools-on-amazon-bedrock/
published_at: '2026-11-13'
---

## 概要

Bedrockは推論呼び出しを呼び出し元のIAMプリンシパルに紐づけ、CUR 2.0とCost Explorerに反映する。IAM Identity Centerとセッションタグ（チーム、コストセンター）を使い、Claude CodeやCodexなどツールを問わずユーザー単位のコスト可視化と利用上限制御を行う方法を示す。

## 設計のポイント

- エンドポイント層で帰属するため、ツール側の計装なしに全ツールで同じ可視化が得られる。
- IdP連携とセッションタグでチーム・コストセンター軸の集計を可能にする。
- CURにはリクエスト単位コストが無いので、必要に応じて呼び出しログで補う。

## 使いどころ

- AIコーディングツールの導入拡大でFinOpsを求められる企業。
- 来年度のAI予算を人数・利用率から見積もりたい部門。
