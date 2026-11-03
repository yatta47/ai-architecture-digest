---
type: guidance
title: Amazon Quickで構造化・非構造化データを1つのチャットエージェントから横断検索
title_original: Bring structured and unstructured data together with Amazon Quick
industry: cross-industry
cloud:
- aws
patterns:
- rag
- text-to-sql
- ai-agent
components:
- Amazon Quick
- Amazon S3
- SPICE
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/bring-structured-and-unstructured-data-together-with-amazon-quick/
published_at: '2026-11-03'
---

## 概要

Amazon QuickでS3ベースのナレッジベース（非構造化）と拡張データセット（構造化）をSpaceに束ね、カスタムチャットエージェントから横断的に質問する手順を解説する。エージェントが知識ベース・データセット・両方のどれを引くか判断し、引用付きで回答する。

## 設計のポイント

- データ層・ワークスペース層・エージェント層の3層に分け、Spaceでデータソースを集約する
- データセットに意味的な説明やカスタム指示を付与し、自然言語からSQLへの変換精度を高める
- 新しいデータソースをSpaceに足すだけでエージェントが利用でき、回答は質問者の権限を尊重する

## 使いどころ

- 社内文書と売上KPIを同時に参照して回答させたいビジネス部門
- BIとドキュメント検索を別ツールで往復している分析担当者
