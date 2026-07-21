---
type: guidance
title: 埋め込みモデルの語彙とドメイン適合性がRAGの検索精度を左右する、埋め込み生成フェーズの設計指針
title_original: RAG generate embeddings phase
industry: cross-industry
cloud:
- azure
patterns:
- rag
- document-processing
components:
- Azure AI Content Understanding
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-generate-embeddings
published_at: '2026-06-18'
---

## 概要

RAGソリューションの埋め込み生成フェーズでは、埋め込みモデルの語彙とデータの単語群がどれだけ重なるかが検索精度を大きく左右する。ドメイン特化データにはBioGPTのようなドメイン特化モデルの利用やファインチューニングを検討し、画像・音声・動画などのマルチモーダルコンテンツはAzure Content Understandingなどで一旦テキスト表現に変換してから埋め込みを生成する流れを整理している。

## 設計のポイント

- ドメイン特化かどうかをまず判定し、一般的なコンテンツなら公開リーダーボード上位モデルを試し、ドメイン特化コンテンツなら専用モデルの有無に応じてファインチューニングか専用モデル採用かを選ぶ。
- 語彙にない単語はサブワードに分割されてベクトルの意味的な近さが劣化するため、対象データの用語が埋め込みモデルの語彙にどれだけ含まれるかを事前に確認する。
- 画像・音声・動画などの非テキストコンテンツはAzure Content Understandingで構造化テキスト表現に変換してから、通常の埋め込みパイプラインに載せる。

## 使いどころ

- 専門用語の多いドメインデータでベクトル検索の精度が思うように出ず、埋め込みモデルの選定を見直したいチーム。
- 画像や動画を含むマルチモーダルなドキュメントをRAGの検索対象に含めたい設計者。
- 汎用埋め込みモデルとドメイン特化モデル、ファインチューニングのどれを選ぶべきか判断基準が欲しいチーム。
