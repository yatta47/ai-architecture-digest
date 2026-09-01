---
type: case
title: ヘルスケア規制対応のマルチテナントSageMaker基盤で1000人超にアドホック分析を民主化
title_original: How ZS democratized secure ad-hoc analytics with Amazon SageMaker
company: ZS Associates
industry: healthcare
cloud:
- aws
patterns:
- llmops
- cost-optimization
- multi-tenant-analytics
- policy-as-code
components:
- Amazon SageMaker
- Amazon VPC
- JFrog Artifactory
- AWS IAM
- AWS KMS
- Amazon EFS
- Amazon S3
- Amazon ECR
- CrowdStrike
- Splunk
- AWS CloudTrail
- AWS Backup
- AWS Cost Explorer
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-zs-democratized-secure-ad-hoc-analytics-with-amazon-sagemaker/
published_at: '2026-09-01'
---

## 概要

ZS Associatesは、ヘルスケア業界の規制要件を満たしながら開発者の俊敏性を維持するため、テナントごとに分離したAmazon SageMaker Studioドメイン、インターネット非経由構成、3階層IAMロール、タグベースのコスト配賦を組み合わせたセキュアな分析基盤を構築した。200以上のドメイン・500人超の日次利用者規模で本番稼働し、Savings Plansで月間約1万ドルのコスト削減を実現している。

## 設計のポイント

- テナントごとに独立したSageMakerドメイン・EFSボリューム・IAMロールを割り当て、強い分離とコスト可視化を両立する
- Domain/Studio User/Space Executionの3階層IAMロールで最小権限を保ちながら柔軟な上書きを可能にする
- インターネット非経由構成とVPCエンドポイント、パッケージリポジトリのリアルタイムスキャンで内部からの持ち込みリスクを遮断する
- タグベースの自動バックアップとコスト配賦で、運用負荷をかけずに耐障害性とチャージバックを両立する

## 使いどころ

- 規制業界でML/分析基盤を全社展開したいがコンプライアンス部門の承認が壁になっている組織
- 部門・チームごとにコスト配賦とアクセス制御を分けたいマルチテナントML基盤
- セルフサービス分析基盤の運用負荷を自動化で下げたいプラットフォームチーム
