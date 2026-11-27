---
type: announcement
title: コード分割・Graph RAG・可観測性などの機能更新まとめ（2023-09-06）
title_original: LlamaIndex Update 09/03/2023
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
- llmops
- fine-tuning
components:
- LlamaIndex
- Neo4j
- Zep
- Predibase
- Azure AI Services
- Xinference
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-update-09-03-2023-4a7c21c0f60b
published_at: '2023-09-06'
---

## 概要

コード分割器、Neo4j連携とGraph RAG、ワンクリック可観測性、非同期対応、ファインチューニング用データ収集などを紹介する更新情報。

## 設計のポイント

- 最適なチャンクサイズが定まらない場合は、複数サイズの検索結果を束ねて再ランキングする。
- 上位モデルでRAGを運用しつつ出力を収集し、安価なモデルの調整データにする。
- 知識グラフから部分グラフを取り出して文脈に使う（Graph RAG）。

## 使いどころ

- LlamaIndexの新機能を追いたい開発者向け。
- コードベースや知識グラフを対象にRAGを組みたい場面。
