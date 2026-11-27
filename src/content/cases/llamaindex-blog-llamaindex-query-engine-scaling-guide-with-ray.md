---
type: guidance
title: LlamaIndexとRayで取り込みを並列化しクエリエンジンを配備する
title_original: Build and Scale a Powerful Query Engine with LlamaIndex and Ray
company: Anyscale
industry: cross-industry
cloud: []
patterns:
- rag
- parallel-execution
components:
- LlamaIndex
- Ray Datasets
- Ray Serve
- Unstructured
- Sentence Transformers
- LangChain
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/build-and-scale-a-powerful-query-engine-with-llamaindex-and-ray-bfb456404bc4
published_at: '2023-06-27'
---

## 概要

Rayのドキュメントとブログを対象に、読み込み・分割・埋め込みをRay Datasetsで並列化し、Ray Serveでクエリエンジンを配備するチュートリアル。

## 設計のポイント

- 取り込み・分割・埋め込みを段階ごとの並列パイプラインにして、ハードウェア利用率を上げる。
- データ源ごとに索引を分け、横断する複雑な問いに対応する。
- 配備とスケールはRay Serveに任せる。

## 使いどころ

- 大量文書の索引化に時間がかかっているチーム向け。
- RAGを試作から本番配備へ進めたい開発者向け。
