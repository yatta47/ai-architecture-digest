---
type: announcement
title: 自然言語の指示で解析を制御できる文書解析基盤LlamaParse
title_original: Launching the first GenAI-native document parsing platform
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- rag
components:
- LlamaParse
- LlamaIndex
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/launching-the-first-genai-native-document-parsing-platform
published_at: '2024-03-13'
---

## 概要

LlamaParseに自然言語の解析指示機能を追加した告知。複雑な表・漫画・数式を指示に応じて解析でき、JSONモードや画像抽出にも対応する。

## 設計のポイント

- 文書の種類を知る利用者の指示をパーサーに渡し、推測に頼らず解析精度を上げる。
- 構造・表・画像・メタデータをJSONで出力し、独自の索引戦略に使えるようにする。

## 使いどころ

- 複雑なレイアウトの文書をRAGに取り込みたいチーム。
- 数式や表を含む資料を構造化したい開発者。
