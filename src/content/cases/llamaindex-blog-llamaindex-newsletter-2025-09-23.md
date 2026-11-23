---
type: announcement
title: 'LlamaIndexニュースレター: LlamaParse 1周年とストリーミング文書処理構成'
title_original: LlamaIndex Newsletter 2025-09-23
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- rag
- event-driven
- ai-agent
components:
- LlamaParse
- Confluent
- MongoDB
- SemTools
- LanceDB
- Dragonfly
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-09-23
published_at: '2025-09-23'
---

## 概要

LlamaIndexの週次ニュースレター。LlamaParse 1周年に合わせ、Confluent・MongoDBと組み合わせたストリーミング型の文書処理パイプライン、LanceDBで埋め込みをキャッシュするSemToolsの高速化、ハッカソンやウェビナーの告知を載せている。

## 設計のポイント

- PDFのパースからリアルタイム埋め込みまでをストリーミング基盤でつなぎ、文書処理を継続的に回す。
- 埋め込みをLanceDBにキャッシュし、大規模文書への検索を分単位から秒単位に短縮する。
- レイアウトや表を考慮したパースと人手確認を組み合わせ、RAGの入力品質を上げる。

## 使いどころ

- 大量の企業文書を継続的に取り込むRAG基盤を作るデータエンジニア。
- 検索の応答時間を縮めたい文書検索の開発者。
