---
type: guidance
title: Claude Apps GatewayをAWS Fargateでセルフホストしエンタープライズのモデルアクセスを統制
title_original: Deploying Anthropic Claude apps gateway for AWS for enterprise workloads
industry: cross-industry
cloud:
- aws
patterns:
- llm-gateway
- policy-as-code
- guardrails
components:
- Claude apps gateway
- Amazon Bedrock
- Claude Platform on AWS
- AWS Fargate
- Amazon RDS for PostgreSQL
- Application Load Balancer
- Amazon Route 53
- AWS Secrets Manager
- Amazon Cognito
outcome:
  type: risk-compliance
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/deploying-anthropic-claude-apps-gateway-for-aws-for-enterprise-workloads/
published_at: '2026-08-11'
---

## 概要

Claude CodeやClaude Desktopを組織全体に展開する管理者は、認証・モデルアクセス・コスト配賦・支出制御を一元管理する必要がある。Claude apps gatewayはAWS Fargate上でステートレスなコンテナとして稼働し、認証状態や支出カウンタをAmazon RDS for PostgreSQLに保持することでどのタスクでもリクエストを処理できる構成をとる。OIDCプロバイダへの認証委任、グループ単位のYAMLポリシーによるモデルアクセス制御、Bedrock/Claude Platform on AWSへのIAMロールベースの認証などにより、開発者端末に上流の認証情報を配布せずにガバナンスを適用できる。

## 設計のポイント

- 認証状態やセッションをタスクではなくデータベースに持たせることで、ロードバランサーのスティッキーセッションなしで任意のタスクが任意のリクエストを処理できるようにする
- 上流のクレデンシャル(BedrockのIAMロール、Claude Platform APIキー)をゲートウェイ内に閉じ込め、開発者端末には一切配布しない
- モデルアクセス許可をIDプロバイダのグループ単位のYAMLポリシーとして宣言的に管理し、最初にマッチしたルールを適用する
- オフボーディングをIDプロバイダからのユーザー削除だけで完結させ、短命なベアラートークンの有効期限切れに任せる

## 使いどころ

- Claude CodeやClaude Desktopを多数の開発者に展開しつつ利用状況を可視化・統制したい企業
- モデルアクセス権限やコスト配賦をチーム・グループ単位で管理したいプラットフォームチーム
- 自社のOIDC IDプロバイダ(Okta, Entra ID, Cognito等)と統合した認証を求める組織
