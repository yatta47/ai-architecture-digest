---
type: guidance
title: OpenAI Responses APIのFile SearchでPDFのRAGを構築する
title_original: Doing RAG on PDFs using File Search in the Responses API
industry: cross-industry
cloud: []
patterns:
- rag
- document-processing
components:
- OpenAI Responses API
- OpenAI Vector Store
- File Search
- GPT-4o mini
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/file_search_responses/
published_at: '2025-03-11'
---

## 概要

PDFをOpenAIのベクトルストアにアップロードし、Responses APIのfile_searchツールで検索と生成を単一のAPI呼び出しに統合するRAG構築手順を紹介するクックブック。従来のチャンク分割・埋め込み生成・ベクトルDB構築を自前で行う手間を省略できる。

## 設計のポイント

- チャンク分割・埋め込み計算・ベクトルDB運用をOpenAIのマネージドVector Storeに任せ、自前実装を不要にする
- 検索単体（vector_stores.search）と生成統合（file_searchツール付きresponses.create）の両方を使い分けられるようにする
- 検索結果には関連度スコアが付与されるため、上位k件のしきい値調整で精度を制御する
- レスポンスのannotationsから引用元ファイル名を抽出し、回答の根拠を追跡できるようにする

## 使いどころ

- 自前のベクトルインフラを構築せず素早くPDF/文書Q&Aを実現したいチーム
- 社内ナレッジベースや製品ドキュメントに基づくサポート・FAQシステム
- 複数レポートを横断して質問応答するリサーチ用途
