---
type: guidance
title: AWS上でEclipse Dataspaceコネクタ（EDC）を本番運用するアーキテクチャパターン
title_original: 'Eclipse Dataspace Components on AWS: Architecture patterns in production'
industry: cross-industry
cloud:
- aws
patterns:
- defense-in-depth
- data-federation
- policy-as-code
- event-driven
components:
- Eclipse Dataspace Components (EDC)
- Amazon ECS
- AWS Fargate
- Amazon Aurora
- AWS Secrets Manager
- Amazon Cognito
- Amazon S3
- Amazon API Gateway
- Network Load Balancer
- Amazon VPC
- AWS IAM
- Amazon ECR
- AWS CDK
- CDK Nag
- Amazon CloudWatch
- AWS Lambda
- Amazon EventBridge
data_sources:
- 共有データ資産
- 第三者受領データ
- OAuth認証情報
- 制御プレーンデータ
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/eclipse-dataspace-components-on-aws-architecture-patterns-in-production/
published_at: '2026-07-17'
---

## 概要

IDSA標準に準拠したEclipse Dataspace Components（EDC）コネクタをAWS上で本番運用するためのアーキテクチャパターンとベストプラクティスを解説する記事。コントロールプレーンとデータプレーンをコンテナ化し、ECS/Fargate・Aurora・Secrets Manager・Cognito・S3・API Gateway等のマネージドサービスで構成する。各コネクタインスタンスを隔離された「アーキテクチャセル」として展開し、AWS Well-Architectedの運用・信頼性・セキュリティ観点で設計判断を整理している。

## 設計のポイント

1コネクタ=1隔離セルを基本単位とし、VPCプライベートサブネット・セキュリティグループ分割・IAM最小権限・保存/転送時の暗号化を独立した層として重ねる多層防御（defense in depth）を採用する。EDCのAPIは内部専用のNetwork Load BalancerをAPI Gatewayで前段化し、SigV4とIAMで保護して意図しない公開露出を防ぐ。インフラはCDKで宣言的にコード化し、CDK Nagで自動検証してデプロイ前に設定ミスとセキュリティ問題を検出（shift-left）する。

## 使いどころ

データスペースに参加して組織間で安全にデータを共有・受領したい企業や、障害分離・データガバナンス・共有/受領データの分離のためユースケース単位でコネクタを隔離運用したいエンタープライズに有効。
