---
type: announcement
title: 顧客VPC内で動くLangSmithマネージド構成(BYOC on AWS)
title_original: LangSmith BYOC is now generally available on AWS
company: LangChain
industry: cross-industry
cloud:
- aws
patterns:
- llmops
- defense-in-depth
components:
- LangSmith
- Amazon EKS
- AWS PrivateLink
- Amazon CloudWatch
- Amazon S3
- Terraform
outcome:
  type: risk-compliance
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-byoc-is-now-generally-available-on-aws
published_at: '2026-08-12'
---

## 概要

LangSmith BYOCは、認証や課金を担うコントロールプレーンをLangChain側に置きつつ、トレースやプロンプトなど機微データを含むデータプレーンを顧客自身のAWSアカウント・VPCに置く二面構成でGA提供された。通信はAWS PrivateLinkに限定され、運用はLangChainが代行するため、規制業界の企業がデータ主権を保ったままエージェントの可観測性・評価基盤をスケールできる。

## 設計のポイント

- コントロールプレーン(認証・課金・UI)とデータプレーン(機微データ含むVPC/EKS)を分離し、機微データがLangChain側のネットワークを一切通過しない設計にした。
- コントロール/データプレーン間の通信をAWS PrivateLinkに限定し、パブリックインターネットを経由させない。
- パブリックAPIエンドポイント無し・ワーカーノードもパブリックIP無しのプライベートEKSクラスタとし、セルフホスト同等の隔離性を保ちつつ運用はLangChainに委譲した。
- Terraformモジュールでプロビジョニング用IAMロールを作成する手順にし、データプレーンの追加を組織・リージョンをまたいで標準化した。

## 使いどころ

- エージェントのトレースやプロンプトに機微なPII/PHIが含まれ、自社のクラウド境界外に出せない金融・医療・セキュリティ業界の企業。
- セルフホストの運用負荷(Kubernetes管理・アップグレード・バックアップ)を減らしつつ、データ主権は維持したいプラットフォームチーム。
- 複数チーム・複数リージョンでエージェント開発をスケールさせたいが、組織ごとに個別の運用モデルを作りたくない企業。
