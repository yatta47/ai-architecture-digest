---
type: case
title: DatacorのQuick Sight埋め込み自然言語レンタル分析
title_original: How Datacor built self-service rental analytics with Amazon Quick Sight
company: Datacor
industry: manufacturing
cloud:
- aws
- azure
patterns:
- multi-tenant-analytics
- data-federation
- text-to-sql
components:
- Amazon Quick Sight
- Amazon Q in Quick Sight
- Azure Data Factory
- Amazon S3
- AWS Glue
- AWS Lambda
- Amazon DynamoDB
- Apache Iceberg
- SPICE
outcome:
  type: revenue
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-datacor-built-self-service-rental-analytics-with-amazon-quick-sight/
published_at: '2026-09-25'
---

## 概要

DatacorはTrackAboutにQuick Sightのダッシュボードと自然言語検索を埋め込み、ガス・溶接販売業者がITを介さずレンタル収益データを分析できるようにした。Azure SQLからS3へのクロスクラウド取り込みと、監査可能なテナント分離を備える。

## 設計のポイント

- Azure Data FactoryでParquet化し差分ロードでS3/Icebergへ取り込み、SPICEを定期更新する。
- 行数検証など地味なデータ品質工程を自然言語クエリ提供の前提にする。
- マルチテナントの分離モデルを監査可能にする。

## 使いどころ

- SaaSに生成AI BIを埋め込み顧客セルフサービスを実現したい事業者。
- クロスクラウドの運用データを分析基盤に集約したい場面。
