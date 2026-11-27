---
type: announcement
title: LLMアプリを即座に始められる事前構成モジュール集 Llama Packs
title_original: Introducing Llama Packs
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
components:
- Llama Packs
- LlamaHub
- Voyage AI
- Weaviate
- Streamlit
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-llama-packs-e14f453b913a
published_at: '2023-11-22'
---

## 概要

LlamaIndexは、RAGやアプリのひな形をパッケージ化したコミュニティ主導のLlama Packsを公開した。パラメータを渡してそのまま実行することも、ダウンロードしてコードを改造することもできる。

## 設計のポイント

- ユースケース単位の構成を、そのまま実行できる形とソースを改造できる形の両方で配布する。
- 各パックが内部モジュールを取り出すインターフェースを持ち、LLMやインデックスを個別に再利用できる。

## 使いどころ

- RAGの構成要素の選定に迷う開発者が、動く出発点を得たい場面。
- 社内の定番構成をテンプレートとして共有したいチーム。
