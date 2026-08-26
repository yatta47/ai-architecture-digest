---
type: case
title: GoDaddyのBI基盤刷新：Amazon QuickSightへの移行で実現した高速化と生成AIレポート自動化
title_original: How GoDaddy transformed its analytics with Amazon QuickSight
company: GoDaddy
industry: cross-industry
cloud:
- aws
patterns:
- business-intelligence-resilience
- text-to-sql
- cost-optimization
components:
- Amazon QuickSight
- Amazon Redshift
- Amazon S3
- Amazon RDS
- QuickSight Q
- Data Stories
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-godaddy-transformed-its-analytics-with-amazon-quick/
published_at: '2026-08-26'
---

## 概要

GoDaddyは2年をかけてlegacy BIツールからAmazon QuickSightへ移行し、5,000超あったダッシュボードを2,500未満まで整理しながら、レンダリング時間を15分未満から5秒未満に短縮した。異常検知やNL質問応答、Data Storiesによる自動レポート生成などQuickSightの生成AI機能を活用し、分析チームは年間15,000時間を高付加価値業務にシフトできた。

## 設計のポイント

- 移行をlift-and-shiftにせず、利用実態の低いダッシュボードを廃止してポートフォリオを精査する機会とした
- 財務ダッシュボード『Cash Dash』では自動異常検知を組み込み、検知1分・調査10分・解決60分の『1/10/60』インシデント対応モデルを実現した
- Data Storiesで週次エグゼクティブサマリーを自動生成し、メールで経営層に配信することでレポーティング工数を削減した
- 既存のAWSインフラ（Redshift/S3/RDS）とのネイティブ統合を軸にサーバーレスなBIスタックへ一本化した

## 使いどころ

- 数千規模のダッシュボードを抱え、レンダリング遅延やライセンスコストに悩む大規模組織のBI刷新
- 分析チームへの依頼待ちを解消し、非エンジニアにセルフサービス分析を広げたい場合
- 財務・オペレーション指標の異常を早期検知し、迅速な意思決定サイクルを回したいチーム
