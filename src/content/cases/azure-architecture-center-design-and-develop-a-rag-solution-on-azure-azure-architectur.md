---
type: guidance
title: RAGソリューションの設計と評価ガイド
title_original: Design and develop a RAG solution
industry: cross-industry
cloud:
- azure
patterns:
- rag
- document-processing
- eval
- context-engineering
components:
- Azure AI Search
- Microsoft Agent Framework
- Semantic Kernel
- Azure AI Agent service
- LangChain
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide
published_at: '2026-06-30'
---

## 概要

独自データを扱うRAG(検索拡張生成)アプリケーションを設計・評価するためのシリーズ記事の導入編。オーケストレーターがAzure AI Searchへの問い合わせを行い、上位の検索結果をプロンプトのコンテキストとして言語モデルに渡す標準的なRAGアプリケーションフローと、チャンキング・メタデータ付与・埋め込み・永続化から成るデータパイプラインフローを示す。準備、チャンキング、チャンク拡張、埋め込み、検索、言語モデル評価という各フェーズで検討すべき設計・評価の観点を整理する。

## 設計のポイント

- オーケストレーターが検索実行の有無やインデックス選択を固定シーケンスで制御する標準RAGパイプラインを起点とする。
- 文書はチャンク分割・メタデータ付与(エンリッチ)・埋め込み・検索インデックスへの永続化という4段階のデータパイプラインで処理する。
- チャンキング手法や埋め込みモデルの選定は検索結果の関連性を左右するため、用途に応じて比較評価する。
- グラウンド性・完全性・関連性などの指標でエンドツーエンドの言語モデル応答を評価するプロセスを組み込む。

## 使いどころ

- 独自データや専有データを扱うLLMアプリケーションを一から設計するチームの意思決定指針として使える。
- 単一の検索・単一インデックスで解決できる定型的な質問応答には標準RAGが適する。
- チャンキング戦略や埋め込みモデル選定など、RAG設計の各フェーズで体系的な評価プロセスを整備したい場合に役立つ。
