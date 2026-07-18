---
type: guidance
title: データスペース基盤（EDCコネクタ）をAWSで運用するコスト設計と最適化
title_original: 'Eclipse Dataspace Components on AWS: Cost optimization strategies'
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- data-federation
components:
- Eclipse Dataspace Components (EDC)
- Amazon Aurora PostgreSQL
- Amazon ECS
- AWS Fargate
- AWS Fargate Spot
- Network Load Balancer
- AWS Secrets Manager
- Amazon Cognito
- Amazon ECR
- Amazon API Gateway
- Amazon S3
- Amazon EC2 Spot
data_sources:
- 組織間共有データ
- 履歴データ
- バックアップ
outcome:
  type: cost
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/eclipse-dataspace-components-on-aws-cost-optimization-strategies/
published_at: '2026-07-17'
---

## 概要

AWS Well-Architected Frameworkのパフォーマンス効率・コスト最適化・持続可能性の観点から、Eclipse Dataspace Components（EDC）コネクタをAWSに展開する際の月額コストを見積もる手引き。参加者（データ提供者・利用者）側のコネクタ構成を対象に、どのAWSサービスがコストを牽引するかを可視化し、業務クリティカルと非クリティカルの2シナリオで内訳を比較する。

## 設計のポイント

コスト最適化の要点は、最大のコストドライバーであるデータベース（Aurora PostgreSQL）と常時稼働コンテナ（ECS/Fargate）、ロードバランサーの見極めにある。非クリティカル用途ではAuroraをdb.r6g.largeからdb.t4g.mediumへ、FargateをFargate Spotへ差し替えることで、データスループットやAPI容量を保ったまま月額コストを最大58%削減できる。

## 使いどころ

- データ主権を保ちつつ組織間でデータ共有を行うデータスペース基盤をAWSに構築するアーキテクトに有効。
- 構築前にインフラ費用を見積もりたい場面で役立つ。
- ワークロードの重要度に応じてリソースを適正化したいFinOps担当者に有効。
