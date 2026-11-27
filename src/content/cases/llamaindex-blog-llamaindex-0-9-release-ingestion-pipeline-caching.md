---
type: announcement
title: LlamaIndex 0.9：キャッシュ付き取り込みパイプラインの導入
title_original: Announcing LlamaIndex 0.9
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
- cost-optimization
components:
- LlamaIndex
- IngestionPipeline
- Redis
- Qdrant
- OpenAI Embeddings
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/announcing-llamaindex-0-9-719f03282945
published_at: '2023-11-15'
---

## 概要

LlamaIndex 0.9は、データの取り込みと変換を担うIngestionPipelineと変換の自動キャッシュを導入した。ノード分割やメタデータ抽出のインターフェースも単一の変換抽象に整理した。

## 設計のポイント

- 分割・メタデータ抽出・Embeddingを同じ変換インターフェースに統一して組み替え可能にする。
- 入力と変換のハッシュで結果をキャッシュし、再実行時の処理を省く。
- 取り込みパイプラインから直接ベクトルストアへ書き込む。

## 使いどころ

- 文書を繰り返し取り込み直すRAG基盤の運用者。
- ユーザーがデータを随時アップロードするアプリ。
