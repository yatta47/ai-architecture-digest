---
type: guidance
title: Neo4jに画像とテキストを分けて索引するマルチモーダルRAG
title_original: Multimodal RAG pipeline with LlamaIndex and Neo4j
industry: cross-industry
cloud: []
patterns:
- rag
components:
- LlamaIndex
- Neo4j
- CLIP
- text-embedding-ada-002
- GPT-4V
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/multimodal-rag-pipeline-with-llamaindex-and-neo4j-a2c542eb0206
published_at: '2023-12-18'
---

## 概要

記事を画像とテキストに分割し、テキストはada-002、画像はCLIPで埋め込んで別々のベクトルストアに格納する。質問時は両方を類似検索し、結果をマルチモーダルLLMに渡して回答を生成する。

## 設計のポイント

- モダリティごとに適した埋め込みモデルと索引を分ける。
- 検索は両索引に並行して行い、生成段階で統合する。
- テキストは見出し単位で分割して文脈のまとまりを保つ。

## 使いどころ

- 図や画像を含む技術文書のQ&Aを作る開発者。
- テキストのみのRAGでは情報が欠ける場面。
