---
type: case
title: CloudWatchのエラーをStrandsエージェントが自動調査するルートコーズ分析基盤
title_original: How TReNDS automates root-cause analysis with Amazon Bedrock
company: TReNDS Center (Georgia State University)
industry: healthcare
cloud:
- aws
patterns:
- ai-agent
- root-cause-analysis
- event-driven
components:
- Amazon Bedrock
- AWS Lambda
- Amazon CloudWatch
- Strands Agents SDK
- Amazon SNS
- Amazon EKS
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-trends-automates-root-cause-analysis-with-amazon-bedrock/
published_at: '2026-08-07'
---

## 概要

TReNDSは、EKS上のアプリケーションがCloudWatchに出力するエラーログをサブスクリプションフィルタで検知し、Bedrock上のStrandsエージェントが自動でルートコーズ分析を行う仕組みを本番運用している。エージェントはGitHubのソースコードを取得するツールを自ら呼び出しながら調査を進め、結果をSNS経由でチームに通知する。HIPAA対象データを扱うため、分析はAWSアカウント内で完結し外部エンドポイントへデータを送らない設計になっている。

## 設計のポイント

- CloudWatchサブスクリプションフィルタでエラーパターンを検知し、Lambda上のエージェントを起動するイベント駆動構成にする
- ソースコード取得ツールをdocstringと型ヒント付きで実装し、モデル自身に調査経路を判断させて固定の調査フローをハードコードしない
- 推論をAWSアカウント内で完結させ、HIPAA相当のデータ残留・コンプライアンス要件を満たす
- Strands Agents公式Lambdaレイヤーを使い、SDKの手動バンドルを不要にする

## 使いどころ

- スタックトレースの解読や関連ソース特定に15〜30分以上かかっている運用チーム
- 医療・研究データなど機密性の高いログを外部に出さずにAI分析したい組織
- EKS/ECS/Lambda/EC2などCloudWatchへログを送る既存環境にそのまま適用したい場合
