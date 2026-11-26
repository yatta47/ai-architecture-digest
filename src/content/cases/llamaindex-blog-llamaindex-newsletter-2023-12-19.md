---
type: announcement
title: GeminiとMistralのday-0対応など：LlamaIndex更新（2023-12-19）
title_original: LlamaIndex Newsletter 2023-12-19
company: LlamaIndex
industry: cross-industry
cloud:
- gcp
patterns:
- rag
- eval
components:
- LlamaIndex
- Gemini
- Semantic Retriever API
- Mistral AI
- Docugami
- SharePoint
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2023-12-19-2965a2d03726
published_at: '2023-12-19'
---

## 概要

GoogleのGeminiとMistralAIのモデル・埋め込みへの即日対応、命題単位の検索、SEC 10Qの複数文書評価データセットなどを紹介するまとめ。SharePointのデータローダーも追加した。

## 設計のポイント

- 検索単位を命題まで細かくして索引し、元テキストにリンクして参照する。
- 単一チャンク・複数チャンク・複数文書の難易度別にRAGを評価する。

## 使いどころ

- モデルや検索手法の選択肢を追いたいRAG開発者。
