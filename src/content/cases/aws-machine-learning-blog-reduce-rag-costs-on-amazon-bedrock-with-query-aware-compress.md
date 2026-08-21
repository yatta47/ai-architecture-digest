---
type: guidance
title: クエリ適応型コンプレッションでAmazon Bedrock RAGの入力トークンを削減
title_original: Reduce RAG costs on Amazon Bedrock with query-aware compression
industry: cross-industry
cloud:
- aws
patterns:
- rag
- cost-optimization
- inference-optimization
components:
- Amazon Bedrock
- Amazon Bedrock Knowledge Bases
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/reduce-rag-costs-on-amazon-bedrock-with-query-aware-compression/
published_at: '2026-08-21'
---

## 概要

高リコール優先のRAG検索は無関係なチャンクを多く含みがちで、主モデルへの入力トークンコストを増大させる。検索後・生成前の段階で小型で低コストなモデルにクエリとの関連度でチャンクをフィルタさせることで、回答品質を保ったまま入力トークンを大幅に削減する後処理パターンを紹介する。

## 設計のポイント

- 検索フェーズは引き続き高リコール志向のまま、後処理でクエリとの関連性のみをフィルタする責務分離を行う
- フィルタ専用に小型・低コストなモデルを充てることで、フィルタ処理自体のコスト増を最小化する
- 無関係な文脈を削ることでコスト削減だけでなくハルシネーションの発生面も減らす副次効果を得る

## 使いどころ

- Amazon Bedrock Knowledge Bases等でRAGを大規模運用しコストが課題になっているチーム
- 高リコール検索を維持しつつ推論コストだけを下げたいプロダクトチーム
- 回答品質を落とさずにハルシネーションのリスクも下げたい場合
