---
type: guidance
title: GitHub Actions で CDK Python アプリの CodeGuru コードレビューを自動化するパターン
title_original: Automate Amazon CodeGuru reviews for AWS CDK Python applications by using GitHub Actions
industry: cross-industry
cloud:
- aws
patterns:
- ci-cd
- policy-as-code
components:
- Amazon CodeGuru Reviewer
- Amazon CodeGuru Security
- Amazon CodeGuru Profiler
- AWS CDK
- GitHub Actions
- AWS Lambda
- Amazon SQS
- Amazon S3
- AWS IAM
outcome:
  type: quality
source_id: aws-architecture-center
source_name: AWS Architecture Center
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-amazon-codeguru-reviews-for-aws-cdk-python-applications.html?did=pg_card&trk=pg_card
published_at: '2025-01-28'
---

## 概要

AWS CDK（Python）で定義したサーバーレスアプリに対し、GitHub Actions のパイプラインから Amazon CodeGuru によるコードレビューとセキュリティスキャンを自動実行する AWS 規範ガイダンスのパターン。プルリクエスト作成時に CodeGuru Reviewer が欠陥や最適化を、CodeGuru Security が脆弱性・ポリシー違反を検出し、重大な指摘があればパイプラインを即時失敗させ、レビュアーの手動 PR 承認後に CDK デプロイへ進む。

## 設計のポイント

- OIDC 発行の一時クレデンシャル（IAM ロール）を GitHub Secrets 経由で引き受け、リポジトリに認証情報を持たせず最小権限で AWS にアクセスする
- CI/CD に「コード分析 → 重大度による自動ゲート → 人手の PR 承認 → デプロイ」の段階的な品質ゲートを組み込む
- CodeGuru Profiler 用のプロファイルデータは SQS 経由で Lambda を定期起動して生成する
- CodeGuru Reviewer は 2025 年 11 月以降、新規リポジトリ関連付けが不可となっている点に注意する

## 使いどころ

- GitHub 上で AWS CDK Python によるサーバーレス開発を進めるチームに有効。
- コード品質・セキュリティチェックをレビュー工程へ自動で組み込みたい場面で役立つ。
