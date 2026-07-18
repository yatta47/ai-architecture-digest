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

- コスト最適化はコストドライバーの見極めから始める。Aurora PostgreSQL、常時稼働のECS/Fargateコンテナ、ロードバランサーが最大の対象。
- 非クリティカル用途では、Auroraをdb.r6g.largeからdb.t4g.mediumへダウンサイズする。
- 同じく非クリティカル用途では、FargateをFargate Spotへ差し替える。
- これらの差し替えでデータスループットやAPI容量を保ったまま、月額コストを最大58%削減できる。

## 使いどころ

- データ主権を保ちつつ組織間でデータ共有を行うデータスペース基盤をAWSに構築するアーキテクトに有効。
- 構築前にインフラ費用を見積もりたい場面で役立つ。
- ワークロードの重要度に応じてリソースを適正化したいFinOps担当者に有効。
