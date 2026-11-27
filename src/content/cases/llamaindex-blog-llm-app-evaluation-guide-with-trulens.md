---
type: guidance
title: TruLensでLlamaIndexアプリを追跡・評価して改善する
title_original: Build and Evaluate LLM Apps with LlamaIndex and TruLens
company: TruEra
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
- rag
components:
- TruLens
- LlamaIndex
- OpenAI
- Hugging Face
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/build-and-evaluate-llm-apps-with-llamaindex-and-trulens-6749e030d83c
published_at: '2023-06-23'
---

## 概要

TruLensでLlamaIndexアプリをラップし、入出力・LLM呼び出し・検索チャンク・遅延を追跡して、フィードバック関数で自動評価する方法を解説する。

## 設計のポイント

- 回答の関連性と取得チャンクの関連性を分けて測り、失敗箇所を特定する。
- チャンク関連性の低さは幻覚の兆候として扱う（事実性そのものは別途確認が必要）。
- プロンプト・モデル・分割方式の版ごとに指標を比較して反復改善する。

## 使いどころ

- RAGの回答品質を継続的に監視したい開発チーム向け。
- 改善施策の効果を版比較で示したい場面。
