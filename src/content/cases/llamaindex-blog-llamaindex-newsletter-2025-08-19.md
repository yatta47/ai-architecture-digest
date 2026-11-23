---
type: announcement
title: 'LlamaIndexニュースレター: GPT-5対応と法務ナレッジグラフ・Text2SQLルーター'
title_original: LlamaIndex Newsletter 2025-08-19
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- text-to-sql
- document-processing
- ai-agent
- human-in-the-loop
components:
- LlamaParse
- LlamaExtract
- GPT-5
- Neo4j
- AstraDB
- Claude
- CopilotKit
- Bright Data
- Cursor
- Streamlit
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-08-19
published_at: '2025-08-19'
---

## 概要

LlamaIndexの週次ニュースレター。GPT-5のLlamaParseプレビュー対応、LlamaParseとNeo4jで法務文書から作るナレッジグラフ、SQLとベクトル検索を振り分けるハイブリッドRAG+Text2SQLルーター、AstraDBのデータシンク対応などを紹介している。SkySQLと11x AIの事例も載っている。

## 設計のポイント

- 問い合わせの種類を分類してSQLとベクトル検索へ振り分け、応答を評価する。
- 非構造の契約文書から当事者・場所・条件の関係を取り出し、グラフDBで問い合わせ可能にする。
- Claudeの検索結果コンテンツブロックで、エージェントの回答に出典付き引用を持たせる。

## 使いどころ

- 構造化データと文書が混在する社内検索を作る開発チーム。
- 契約文書などの関係性を分析したい法務・金融の担当者。
