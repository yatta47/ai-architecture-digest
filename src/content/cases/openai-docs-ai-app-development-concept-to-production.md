---
type: guidance
title: 基礎理解→評価→最適化の4フェーズで本番AIアプリまで導くラーニングトラック
title_original: 'AI application development: concept to production'
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- rag
- fine-tuning
components:
- Agents SDK
- Evals API
outcome:
  type: reliability
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/tracks/ai-application-development/
published_at: '2025-07-11'
---

## 概要

OpenAIの開発者向けラーニングトラックは、エージェント・evalsといった基礎概念の理解、コード例による実践、evalsとガードレールによる安全性確保、コスト・レイテンシ最適化という4フェーズで、本番投入可能なAIアプリケーションを構築するための学習パスを提供する。

## 設計のポイント

- コアロジック(エージェント)と品質評価(evals)を対で扱い、機能実装と並行して評価基盤を整備することを前提にする。
- プロンプトエンジニアリング・RAG・ファインチューニングを『基本テクニック』として並置し、知識注入にはRAG、振る舞い最適化にはファインチューニングという役割分担を明示する。
- 非決定的な出力を本番で扱うため、user-facing応答以外はできる限りStructured Outputsで型を固定することを推奨する。

## 使いどころ

- エージェント開発の全体像を体系的にキャッチアップしたい開発者。
- プロトタイプから本番運用への移行時に、何を評価・最適化すべきか順序立てて把握したい場合。
