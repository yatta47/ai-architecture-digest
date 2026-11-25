---
type: guidance
title: インデックス複製と可視化で進めるRAGのチャンクサイズ調整
title_original: Efficient Chunk Size Optimization for RAG Pipelines
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- eval
- document-processing
components:
- LlamaParse
- LlamaTrace
- Traceloop
- Langfuse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/efficient-chunk-size-optimization-for-rag-pipelines-with-llamacloud
published_at: '2024-08-21'
---

## 概要

チャンクサイズの実験は再索引の手間、保存容量、可視性の不足が障壁になる。正解を知っている質問で基準構成を試し、取得チャンクを確認してから複製インデックスで設定を変えて比較する手順を示す。

## 設計のポイント

- 索引段階のパラメータは、インデックスを複製して設定違いを並べて比較する。
- 回答が不完全なときは、まず取得チャンクと元文書の分割位置を確認する。
- 手早い確認の後は、正解付きの評価セットと自動テストで体系的に評価する。

## 使いどころ

- RAGの回答漏れの原因を調べている開発者。
- 文書種別ごとにチャンク設定を決めたいチーム。
