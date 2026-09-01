---
type: case
title: Bedrock利用のリアルタイム個人単位支出制御によるAIコストガバナンス
title_original: 'Tokenomics at scale: How Jamf built real-time spend enforcement for Amazon Bedrock'
company: Jamf
industry: other
cloud:
- aws
patterns:
- llmops
- cost-optimization
- policy-as-code
- guardrails
components:
- Amazon Bedrock
- AWS IAM
- Amazon Athena
- AWS Lambda
- Amazon EventBridge
- Amazon DynamoDB
- Amazon S3
- Slack
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/tokenomics-at-scale-how-jamf-built-real-time-spend-enforcement-for-amazon-bedrock/
published_at: '2026-09-01'
---

## 概要

Jamfは、エンジニアごとのAmazon Bedrock利用コストをAthenaでリアルタイム集計し、予算の80%/100%到達時にIAM Customer Managed Policyでモデルアクセスを段階的に制限するサーバーレスの支出ガバナンス基盤を構築した。制限は15分間隔のLambdaで再計算され、再認証なしに即時反映・自動解除される。

## 設計のポイント

- IAM Customer Managed Policyのバージョン更新で権限を即時反映させ、再認証や再プロビジョニングを不要にする
- 毎回その日の累積支出から制限対象ユーザーを全量再計算する冪等設計にし、実行の重複・欠落があっても収束させる
- 未登録モデルは最上位の高額レートで課金計算するfail-safeをデフォルトにし、価格未登録のモデルが制御をすり抜けないようにする
- モデルを一律停止せず低コストモデルへの縮退のみ許可し、業務継続性を保つ

## 使いどころ

- 生成AI利用を全社解放しつつ個人単位のコスト暴走を防ぎたいプラットフォーム/FinOpsチーム
- 従量課金AIサービスのコストガバナンスを事後精算でなくリアルタイム制御にしたい組織
- 予算超過時も完全停止でなく段階的縮退にしたいエンジニアリング組織
