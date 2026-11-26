---
type: announcement
title: LlamaIndexがGeminiのテキスト・マルチモーダルに即日対応
title_original: LlamaIndex + Gemini
company: LlamaIndex
industry: cross-industry
cloud:
- gcp
patterns:
- rag
components:
- LlamaIndex
- Gemini Pro
- Gemini Pro Vision
- Semantic Retriever API
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-gemini-8d7c3b9ea97e
published_at: '2023-12-13'
---

## 概要

GoogleのGemini公開と同時に、テキスト版と画像入力対応版の両方をLlamaIndexで利用可能にした。ストレージ・埋め込み・検索・生成をまとめたSemantic Retriever APIにも対応する。

## 設計のポイント

- マネージドなRAG APIは単体利用だけでなく部品に分解して他の検索手法と組み合わせられる。
- モデル追加に備え、複数画像とテキストを受ける抽象化を用意する。

## 使いどころ

- Geminiを使ったRAGやマルチモーダルアプリを試す開発者。
