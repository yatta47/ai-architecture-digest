---
type: guidance
title: データのある場所にベクトル検索を追加するAWSのエージェントAI基盤設計指針
title_original: 'AWS vector solutions: Build agentic AI where your data lives'
industry: cross-industry
cloud:
- aws
patterns:
- rag
- full-text-search
- data-federation
components:
- Amazon OpenSearch Service
- Amazon S3
- Amazon Aurora PostgreSQL
- Amazon DynamoDB
- Amazon ElastiCache for Valkey
- Amazon Neptune
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/aws-vector-solutions-build-agentic-ai-where-your-data-lives/
published_at: '2026-08-20'
---

## 概要

エージェントAIの精度はグラウンディングに使う検索層の質に左右されるとして、AWSは新規にベクトルDBを立てるのではなく、既存のデータストア（OpenSearch、S3、Aurora PostgreSQL、DynamoDB、ElastiCache for Valkey、Neptune）にベクトル検索を追加する設計を第一原則として提示する。新規ワークロードではレイテンシ・コスト・アクセスパターンという支配的要件に応じてエンジンを選ぶ判断モデルを示し、バランス重視の場合はAmazon OpenSearch Serviceをデフォルトとして推奨する。

## 設計のポイント

- 既存のAWSデータストアがあるなら新サービスを導入せずそこにベクトルを追加し、データ移動・同期コストとサービス間ホップをなくす
- 新規ワークロードはレイテンシ・コスト・アクセスパターンのうち支配的な要件を1つ特定し、それに最適化されたエンジンを選ぶ判断モデルに従う
- 単一の支配的要件がないバランス型ワークロードには、レキシカル・ベクトル・ハイブリッド・エージェント検索を一つのシステムで扱えるOpenSearch Serviceをデフォルトにする
- RAG・セマンティック検索・ハイブリッド検索・GraphRAGなどユースケースごとに必要な検索方式を整理してから技術選定する

## 使いどころ

- 既存の運用実績があるデータストアを活かしたまま、エージェントのグラウンディング用検索を追加したいチーム
- RAGやマルチモーダルなコンテンツ発見、異常検知など複数のベクトル活用ユースケースを持つ組織のアーキテクト
- ベクトルDB技術選定で迷い、コスト・レイテンシ・アクセスパターンに応じた判断基準が欲しいエンジニア
