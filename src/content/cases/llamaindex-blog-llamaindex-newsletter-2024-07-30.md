---
type: announcement
title: 'LlamaIndex週報: LlamaExtractベータと構造化抽出'
title_original: LlamaIndex Newsletter 2024-07-30
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- rag
- ai-agent
components:
- LlamaExtract
- LlamaParse
- Ollama
- Mistral Large 2
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-07-30
published_at: '2024-07-30'
---

## 概要

非構造化文書から構造化データを取り出すLlamaExtractのベータ公開と、Pydanticオブジェクトを使う構造化抽出機能を紹介する週次ニュースレター。Ollamaのツール呼び出し対応も伝えている。

## 設計のポイント

- Pydanticでスキーマを定義し、チャンク単位か文書単位で抽出する。
- 抽出したメタデータで検索と合成の文脈を豊かにする。

## 使いどころ

- ETLやRAGに構造化抽出を組み込む開発者。
- ローカルモデルでエージェントを作りたい場合。
