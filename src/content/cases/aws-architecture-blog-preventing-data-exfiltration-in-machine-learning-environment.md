---
type: case
title: iBusinessのSageMaker AI環境における三層防御データ持ち出し防止アーキテクチャ
title_original: Preventing data exfiltration in machine learning environments with Amazon SageMaker AI
company: iBusiness
industry: financial-services
cloud:
- aws
patterns:
- defense-in-depth
- llmops
components:
- Amazon SageMaker AI
- Amazon SageMaker Studio
- Amazon WorkSpaces Secure Browser
- AWS IAM
- Amazon VPC
- AWS Lake Formation
- Amazon Athena
- Amazon Route 53
- Amazon Route 53 Resolver DNS Firewall
- AWS IAM Identity Center
- Amazon S3
- NATゲートウェイ
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/preventing-data-exfiltration-in-machine-learning-environments-with-amazon-sagemaker-ai/
published_at: '2026-06-29'
---

## 概要

AIドリブンのフィンテック企業iBusinessは、データサイエンティストが機密データを扱いながらモデルを開発できるよう、Amazon SageMaker AIを中心とした三層のセキュリティアーキテクチャを構築した。WorkSpaces Secure BrowserによるアクセスのロックダウンとURL許可リスト、VPCエンドポイントとIAMポリシーによるクロスアカウント遮断、SageMaker AI VPCからのインターネット経路排除を組み合わせ、データ持ち出しリスクを抑えつつ生産性を維持している。従来のair-gapped環境や監視付き仮想デスクトップに比べ、コストと運用負荷を大幅に削減した。

## 設計のポイント

- Secure Browserでダウンロード・アップロード・クリップボード・印刷を無効化し、URL許可リストで外部送信経路を遮断する
- VPCエンドポイントとIAMポリシーでコンソールアクセスを自社アカウントに限定し、クロスアカウントへのデータ移動を拒否する
- SageMaker AI VPCからNATゲートウェイ/インターネット経路を排除し、必要なAWSサービスへのアクセスのみVPCエンドポイント経由で許可する
- Route 53プライベートホストゾーンとDNS Firewallを組み合わせ、DNS経由の情報持ち出しリスクも塞ぐ

## 使いどころ

- 機密データを扱う金融・フィンテック企業のデータサイエンスチームがモデル開発の生産性を維持しつつ情報漏えいを防ぎたい場合
- コストと運用負荷の高いair-gapped環境や監視付き仮想デスクトップから、マネージドなML開発基盤へ移行したい場合
- リモートワーク下でも機密データへのセキュアなアクセスを担保したい場合
