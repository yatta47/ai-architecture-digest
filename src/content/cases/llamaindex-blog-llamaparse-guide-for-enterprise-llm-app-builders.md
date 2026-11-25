---
type: announcement
title: 企業向けのRAGデータ基盤 LlamaParseの全体像
title_original: 'LlamaCloud: Built for Enterprise LLM App Builders'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- LlamaParse
- LlamaIndex
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamacloud-built-for-enterprise-llm-app-builders
published_at: '2024-07-09'
---

## 概要

データ品質、拡張性、精度、設定の複雑さという本番RAGの課題に対し、解析、マネージド取り込み、高度な検索、プレイグラウンドを備えたデータ基盤を紹介する。ベクトルDBとは競合せず補完する位置付けとしている。

## 設計のポイント

- 解析と取り込みをベクトル保存層から分離し、保存先を選べるようにする。
- ハイブリッド検索、再ランク、メタデータ絞り込みを組み合わせて精度を上げる。
- デプロイ前にプレイグラウンドで取り込みと検索の戦略を試す。

## 使いどころ

- 表や図を含む大量の企業文書でRAGを作るチーム。
- データソース追加のたびの解析開発を減らしたい場合。
