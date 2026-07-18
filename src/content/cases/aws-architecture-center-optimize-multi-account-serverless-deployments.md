---
type: guidance
title: AWS CDK（Go）とGitHub Actions再利用ワークフローで複数AWSアカウントのサーバーレス配信を標準化するパターン
title_original: Optimize multi-account serverless deployments by using the AWS CDK and GitHub Actions workflows
industry: cross-industry
cloud:
- aws
patterns:
- ci-cd
- infrastructure-as-code
- multi-account-deployment
components:
- AWS CDK
- AWS CloudFormation
- Amazon ECR
- AWS IAM
- AWS Lambda
- AWS Systems Manager Parameter Store
- AWS STS
- GitHub Actions
- Docker
- Go
data_sources:
- Dockerイメージ
- イメージタグ
- CloudFormationテンプレート
outcome:
  type: productivity
source_id: aws-architecture-center
source_name: AWS Architecture Center
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/optimize-multi-account-serverless-deployments.html?did=pg_card&trk=pg_card
published_at: '2024-12-14'
---

## 概要

複数のAWSアカウント・環境にまたがるサーバーレス基盤の配信で起きがちなコード重複・手作業・実践のばらつきを解消するAWS公式パターン。AWS CDK（Go）でインフラをコード化し、GitHub Actionsの再利用可能ワークフローでCI/CDを標準化することで、クロスアカウントのリソースを一貫したパイプラインで管理する手法を示す。CIでDockerイメージをビルドして中央アカウントのECRへプッシュし、CDでCDKによりターゲットアカウントのLambdaへデプロイする流れを解説している。

## 設計のポイント

CIとCDを「再利用可能ワークフロー」というモジュール化テンプレートに切り出し、複数リポジトリ/プロジェクト間で共有することで標準化と効率を両立させている。認証はGitHub OIDCロールとAWS STSの一時クレデンシャルを使い、中央アカウントのOIDCロールからCDKブートストラップロールを引き受けてターゲットアカウントへ横断デプロイする多段アサインの構成が要点。CIでビルドしたイメージタグをParameter Storeに保存し、CDでは手動指定したタグを使ってビルドとデプロイを分離している。

## 使いどころ

- サーバーレスをマルチAWSアカウントで運用し、環境ごとに配信手順が乱立して重複や手作業に悩むプラットフォーム/DevOpsチーム
- CDKとGitHub Actionsで一貫したCI/CD基盤を組みたい組織が、設計テンプレートとして参照する場面
