---
type: guidance
title: RAGと他の最適化レバーを組み合わせて精度と一貫性を両立させるパイプライン設計
title_original: Optimizing LLM Accuracy (RAG section)
industry: cross-industry
cloud: []
patterns:
- rag
- fine-tuning
- prompt-optimization
components: []
outcome:
  type: quality
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/optimizing-llm-accuracy#retrieval-augmented-generation-rag
published_at: '2025-07-21'
---

## 概要

同じくOptimizing LLM Accuracyガイドの中で、RAGが果たす役割にフォーカスした部分。まずプロンプトエンジニアリングで『何が正解か』を定義し、精度が足りない場合にRAGで関連コンテキストを補強、その上でfine-tuningにより出力の一貫性を高め、さらにリトリーバルの調整とファクトチェック工程を加えて再学習するという反復的な最適化パイプラインの例を示す。

## 設計のポイント

- コンテキスト不足が原因の精度課題にはRAGで関連情報を補強し、挙動の一貫性課題にはfine-tuningで対処するというように、症状に応じて手を打つ順序を切り分ける。
- RAGの導入後もリトリーバル精度のチューニングとハルシネーション検出のためのファクトチェック工程を組み込み、その結果を学習データにフィードバックして再学習する。

## 使いどころ

- 検索精度だけでなく応答の一貫性にも課題を抱える業務特化型QAシステムの改善。
- RAG単体では精度が頭打ちになり、fine-tuningとの組み合わせを検討しているチーム。
