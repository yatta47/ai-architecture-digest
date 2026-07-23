---
type: guidance
title: RAGソリューション開発における準備フェーズの進め方
title_original: RAG preparation phase
industry: cross-industry
cloud:
- azure
patterns:
- rag
- document-processing
components: []
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-preparation-phase
published_at: '2025-11-21'
---

## 概要

RAG(検索拡張生成)ソリューション開発の最初のフェーズである準備フェーズでは、まず対象とする事業ドメインを明確に定義し、それに基づいてドキュメントやマルチメディアコンテンツを収集する。並行して、コンテンツの分類・形式・セキュリティ制約・構造的特徴を分析し、ドメインに関連するテスト用の質問も収集することで、後続のローディング・チャンク戦略の検討に活かす。

## 設計のポイント

- 事業ドメインを先に明確化し、それに答えられる質問とコンテンツの収集範囲を決める
- コンテンツの分類・形式・セキュリティ制約・構造をそれぞれ分析し、ローディングとチャンク戦略の判断材料にする
- 目次・ヘッダー/フッター・注釈など文脈的価値の低い要素は無視してよいか個別に判断する
- マルチカラムレイアウトなど構造上の特徴に応じて前処理の要否とチャンク方式を検討する

## 使いどころ

- 新規にRAGソリューションを設計するチームが、テストデータセットの網羅性を判断する基準を必要とする場面
- PDF・DOCX・動画・音声など多様な形式が混在するコンテンツ群のローディング/前処理戦略を策定する場面
- アクセス制御が必要な機密コンテンツをRAGに組み込む際のセキュリティ要件整理
- ドキュメントのチャンク戦略や前処理方針を検討するアーキテクトやエンジニアの初期設計フェーズ
