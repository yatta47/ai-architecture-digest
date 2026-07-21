---
type: guidance
title: RAGのチャンク分割戦略をコスト・品質のトレードオフから設計するガイド
title_original: RAG chunking phase
industry: cross-industry
cloud:
- azure
patterns:
- rag
- document-processing
- cost-optimization
components:
- Azure OpenAI
- Azure AI Vision
- Azure AI Content Understanding
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-chunking-phase
published_at: '2026-06-18'
---

## 概要

RAGソリューションにおけるチャンク分割の設計指針として、チャンクが大きすぎるとコスト増とモデルのトークン上限超過を招き、小さすぎると文脈不足で回答精度が落ちるというトレードオフを整理する。画像を含むチャンクの扱いについては、Azure Visionによる事前分類やAzure Content Understandingによる説明生成、キャッシュアサイドパターンによるコスト最適化など、文書種別ごとに異なるチャンク化実装のコスト構造を具体的に示している。

## 設計のポイント

- 文書タイプごとに異なるチャンク化実装のエンジニアリングコストと文書1件あたりの処理コストを分けて見積もり、品質とコストのトレードオフを定量的に判断する。
- 画像を説明文へ変換する前にAzure Visionなどの安価な分類器で処理価値の有無をスクリーニングし、高コストな言語モデル呼び出しを本当に必要な画像だけに絞る。
- 画像のハッシュ値をキーにしたキャッシュアサイドパターンを導入し、同一画像の再処理コストを排除する。

## 使いどころ

- 大量の文書と埋め込み画像を扱うRAGパイプラインで、チャンク化コストが想定以上に膨らんでいるチーム。
- 文書種別ごとに異なるチャンク戦略を設計する必要があり、コストと品質のトレードオフを事前に見積もりたいアーキテクト。
- マルチモーダルコンテンツの前処理をパイプラインに組み込みたいRAGソリューション設計者。
