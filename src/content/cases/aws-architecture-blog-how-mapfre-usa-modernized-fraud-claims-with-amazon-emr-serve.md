---
type: case
title: Mapfre USAのグラフ×MLによる保険金請求不正検知基盤
title_original: How Mapfre USA modernized fraud claims with Amazon EMR Serverless
company: Mapfre USA
industry: financial-services
cloud:
- aws
patterns:
- fraud-detection
- event-driven
- ci-cd
components:
- Amazon EMR Serverless
- Amazon S3
- AWS Glue Data Catalog
- AWS Lake Formation
- Neo4j
- Apache Airflow
- Amazon MWAA
- AWS Lambda
- Amazon CloudWatch
- Amazon SNS
- AWS Secrets Manager
- Guidewire
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/how-mapfre-usa-modernized-fraud-claims-with-amazon-emr-serverless/
published_at: '2026-07-14'
---

## 概要

Mapfre USAはグラフベースの特徴量とMLモデルを組み合わせた不正請求検知基盤をAWS上の自社データプラットフォーム「Atenea」に構築。Neo4jによるクレーム間の隠れた関係性分析とGuidewire Claimsへの自動連携により、従来の構造化データ分析だけでは見逃していた不正を検出し、500万ドル超のNPVを実現した。

## 設計のポイント

- Icebergテーブルをsilver/gold/platinumの3層に分け、Feature Store管理のテーブルとして特徴量とモデル予測の再利用性・ガバナンスを両立する。
- Neo4jグラフでクレーム間の疑わしいつながりやプロバイダの不正率など、構造化データだけでは見えない関係性特徴量を生成する。
- Apache Airflowで摂取・学習・推論を一元オーケストレーションし、CI/CDによる環境昇格とデッドレターキュー付きの障害通知を組み込む。
- S3イベント通知→Lambda→Guidewire Predictive Model APIという経路で予測結果を調査担当者向けの説明付きアクティビティに自動変換する。

## 使いどころ

- 構造化データだけでは検知しきれない不正ネットワークを見つけたい保険会社。
- MLの予測結果を既存の業務システム(Guidewireなど)にシームレスに連携したい組織。
