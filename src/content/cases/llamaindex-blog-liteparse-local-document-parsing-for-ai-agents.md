---
type: announcement
title: エージェント向けに最適化したローカル文書パーサー『LiteParse』のオープンソース公開
title_original: 'LiteParse: Local Document Parsing for AI Agents'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
components:
- LiteParse
- LlamaParse
- Tesseract.js
- PaddleOCR
- EasyOCR
- PyPDF
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/liteparse-local-document-parsing-for-ai-agents
published_at: '2026-07-19'
---

## 概要

既存の文書パーサーは高速だが不正確(pypdf等)か、高精度だが低速・クラウド依存(VLM系)のどちらかに偏っており、エージェントは『粗い出力でもすぐ推論を続けたい』というニーズに合っていなかった。LlamaIndexはLlamaParseの中核処理をローカル完結のCLI/TSライブラリ『LiteParse』としてオープンソース化し、テーブル検出をせずテキストを空間グリッドへ投影する方式でLLMにそのまま読ませる設計にした。

## 設計のポイント

- 表を検出してMarkdownに変換する複雑な構造推定はせず、空間関係を保ったテキストをそのままLLMに読ませる(LLMはASCII表やコード整形に既に慣れている)という前提で設計した
- まずテキストで高速に把握し、必要な箇所だけスクリーンショットで詳細なマルチモーダル推論にフォールバックするというエージェントの利用パターンに合わせて機能を絞った
- 複雑なレイアウトの高精度が必要な場合はクラウドのLlamaParseへ、リアルタイム・ローカル実行が必要な場合はLiteParseへと役割を明確に分離した
- 既存のOCRベンチマークがLiteParseの出力形式(非Markdown・レイアウト依存の改行)に合わないと判断し、独自のLLM-as-a-judge評価パイプラインを構築した

## 使いどころ

- PDFを素早く読んで処理を継続したいコーディングエージェント・リアルタイムアプリケーション
- GPUやクラウド接続に依存せず、ローカル環境だけで文書パースを完結させたい開発者
