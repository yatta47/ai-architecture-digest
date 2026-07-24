---
type: guidance
title: 銀行向け「次に薦める商品」予測をマルチタワー深層学習で説明可能にする設計
title_original: Build an explainable next-best-product recommendation system for banking on AWS
industry: financial-services
cloud:
- aws
patterns:
- generative-recommendation
components:
- Amazon SageMaker AI
- AWS Glue
- AWS Glue Data Catalog
- Amazon S3
- Amazon CloudWatch
- Amazon SageMaker Pipelines
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-an-explainable-next-best-product-recommendation-system-for-banking-on-aws/
published_at: '2026-07-24'
---

## 概要

銀行の顧客データから次に薦める金融商品を予測するNext-Best-Productシステムを、Amazon SageMaker AIとPyTorchで構築するアーキテクチャ解説。4つの専門タワーを学習型アテンションで統合し、精度と顧客単位の説明可能性を両立させる設計を示す。

## 設計のポイント

- 顧客データの種類ごとに専門化した4つのニューラルネットワークタワーを用意し、学習型アテンションで統合することで予測根拠を顧客単位に説明可能にする
- AWS GlueによるETLとSageMaker Processingによる特徴量エンジニアリングを分離し、データ統合とML特徴量生成の責務を分ける
- Parquet+S3で列指向圧縮ストレージを採用し、列プルーニングと述語プッシュダウンで読み取りコストを削減する
- PyTorchの可変長系列処理(pack_padded_sequence)を活かし、研究から本番運用までの反復速度を優先する

## 使いどころ

- 規制上の説明責任が求められる金融機関のレコメンデーションシステム構築
- 異種混合な顧客データ(取引履歴・属性・行動パターン)を扱うドメインでの精度と解釈性の両立
- ルールベースや協調フィルタリングでは捉えきれない時系列的な商品採用パターンのモデリング
