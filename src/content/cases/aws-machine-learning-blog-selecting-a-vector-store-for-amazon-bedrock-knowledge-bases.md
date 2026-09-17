---
type: guidance
title: Bedrock Knowledge Baseのベクトルストア選定ガイド
title_original: Selecting a vector store for Amazon Bedrock Knowledge Bases
industry: cross-industry
cloud:
- aws
patterns:
- rag
- cost-optimization
components:
- Amazon Bedrock Knowledge Bases
- Amazon OpenSearch Service
- Amazon Aurora PostgreSQL
- pgvector
- Amazon S3 Vectors
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/selecting-a-vector-store-for-amazon-bedrock-knowledge-bases/
published_at: '2026-09-17'
---

## 概要

Amazon Bedrock Knowledge Basesのカスタマーマネージド構成で選べる3つのベクトルストア(OpenSearch Service、Aurora PostgreSQL+pgvector、S3 Vectors)を、ユースケースごとの性能・コスト要件で比較する。ECサイトの商品検索のようにハイブリッド検索と低レイテンシが必要な場合はOpenSearchが適しており、大規模データをコスト効率よく扱いたい場合はS3 Vectorsが有効である。

## 設計のポイント

- ハイブリッド検索(キーワード+ベクトル)や低レイテンシのファセット検索が必要ならOpenSearch Serverlessを選ぶ。
- リレーショナルデータとベクトル検索を同一DBで扱いたい場合はAurora PostgreSQL+pgvectorが適する。
- 大規模データをコスト最優先で保存・検索したい場合はS3 Vectorsで従来比最大90%のストレージコスト削減が見込める。
- インデックス方式や距離指標などの設定次第で検索精度とコストが大きく変わるため、ユースケースごとにベンチマークして選定する。

## 使いどころ

- ピーク時に大量の同時検索が発生するECサイトの商品検索。
- 数千万件規模のドキュメントをRAGで扱う際のコスト最適化。
- 既存のリレーショナルDB運用にベクトル検索を統合したいシステム。
