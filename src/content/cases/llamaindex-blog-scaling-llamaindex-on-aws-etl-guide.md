---
type: case
title: EKSとRabbitMQで文書の埋め込み取り込みを並列化するRAG用ETL
title_original: Scaling LlamaIndex with AWS and Hugging Face
company: LlamaIndex
industry: cross-industry
cloud:
- aws
patterns:
- rag
- parallel-execution
- event-driven
components:
- Amazon EKS
- AWS Lambda
- RabbitMQ
- Hugging Face Text Embeddings Inference
- LlamaIndex
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/scaling-llamaindex-with-aws-and-hugging-face-e2c71aa64716
published_at: '2024-01-02'
---

## 概要

3万文書の再インデックスに10〜20分かかる問題に対し、AWS上にスケーラブルな取り込みパイプラインを構築して約5分に短縮した。埋め込みサーバーをGPUノードに配置し、文書はキュー経由で処理する。

## 設計のポイント

- 埋め込みは専用の推論サーバーとして切り出し、GPUと連続バッチの恩恵を受ける。
- 遅い取り込み処理はREST接続を保持せず、メッセージキューに投入して非同期化する。
- 取り込み側はレプリカ数で水平に拡張する。

## 使いどころ

- 大量文書の再インデックスを繰り返すRAG開発チーム。
- 手元の取り込み処理を本番基盤へ移したい場面。
