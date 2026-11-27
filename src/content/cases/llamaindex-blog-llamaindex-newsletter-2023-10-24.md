---
type: announcement
title: QueryFusionRetrieverやルーター調整の週次まとめ（2023-10-24）
title_original: LlamaIndex Newsletter 2023-10-24
company: LlamaIndex
industry: cross-industry
cloud:
- aws
patterns:
- rag
- fine-tuning
- text-to-sql
components:
- LlamaIndex
- QueryFusionRetriever
- SQLRetriever
- Amazon Bedrock
- AI21 Labs
- Gradient AI
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-10-24-4a76204eeaa3
published_at: '2023-10-24'
---

## 概要

複数クエリ生成と順位融合を行うQueryFusionRetriever、ルーターのファインチューニング、Text-to-SQLとRAGを組み合わせるSQLRetrieverなどを紹介する週次ニュースレター。Amazon Bedrockなどとの統合も含む。

## 設計のポイント

- LLMで複数クエリを作り、検索結果をreciprocal rank fusionで統合する。
- 経路選択の判断は専用にファインチューニングして精度を上げる。

## 使いどころ

- RAGの検索品質を上げる手法を探す開発者。
