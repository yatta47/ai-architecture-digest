---
type: announcement
title: 'LlamaIndex週報: エージェントの安全なコード実行とローカル埋め込みなどの追加'
title_original: LlamaIndex Newsletter 2024-05-28
company: LlamaIndex
industry: cross-industry
cloud:
- azure
patterns:
- ai-agent
- rag
- defense-in-depth
components:
- LlamaIndex
- Azure Container Apps
- AzureCodeInterpreterTool
- Nomic Embed
- Vespa
- MyMagic AI
- RAGApp
- LlamaFS
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-05-28
published_at: '2024-05-28'
---

## 概要

LlamaIndexの週次ニュースレター。Azure Container Appsの動的セッションでLLM生成コードを隔離実行する統合、Nomic Embedのローカル実行、Vespaのハイブリッド検索対応などを紹介している。

## 設計のポイント

- LLMが生成したコードはサンドボックス化されたセッションプールで実行する。
- 埋め込みはローカルとリモートを速度に応じて自動選択し、遅延を抑える。
- ベクトル検索にBM25を併用するハイブリッド検索を使う。

## 使いどころ

- エージェントにコード実行を許可したいが、実行環境を隔離する必要があるチーム。
- RAGの埋め込みや検索の構成要素を選定している開発者。
