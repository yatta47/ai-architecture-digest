---
type: guidance
title: IAMプリンシパル単位でBedrock支出を可視化し上限を設ける
title_original: 'Tokenomics at scale: Track and cap Amazon Bedrock spend per IAM principal with CUR 2.0 and AWS Budgets'
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- llm-gateway
- policy-as-code
components:
- Amazon Bedrock
- CUR 2.0
- AWS Budgets
- AWS IAM
- Cost Explorer
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/tokenomics-at-scale-track-and-cap-amazon-bedrock-spend-per-iam-principal-with-cur-2-0-and-aws-budgets/
published_at: '2026-11-12'
---

## 概要

BedrockがIAMプリンシパルを自動記録することを利用し、コスト配分タグ、CUR 2.0、AWS Budgetsの予算アクションだけで、ユーザー別のコスト可視化と閾値超過時のアクセス制限を実現する構成を示す。

## 設計のポイント

- 帰属・レポート・強制の3段階に分け、コードを書かずAWSネイティブ機能で完結させる。
- 共有ロールにはセッションタグで個人を識別する。
- 予算アクションでDeny IAMポリシーを適用して利用を止める。

## 使いどころ

- 生成AIの利用拡大前に人・チーム別の支出管理を整えたい組織。
- カスタムの強制ループを運用したくないチーム。
