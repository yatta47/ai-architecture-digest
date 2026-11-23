---
type: announcement
title: 'LlamaIndexニュースレター: SemTools CLIと文書分類Classifyベータ'
title_original: LlamaIndex Newsletter 2025-09-09
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- human-in-the-loop
- parallel-execution
components:
- SemTools
- LlamaIndex Classify
- LlamaExtract
- LlamaParse
- vibe-llama
- workflows-py
- Cemex
- Jeppesen
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-09-09
published_at: '2025-09-09'
---

## 概要

LlamaIndexの週次ニュースレター。UnixツールとセマンティックサーチをつなぐSemTools CLI、ルールベースの文書分類Classifyベータ、抽出スキーマの自動生成を紹介している。CemexやJeppesenの導入事例も載り、Jeppesenはエージェント構築時間を512時間から64時間に減らしたとされる。

## 設計のポイント

- 複数ステップ・並列処理・人手確認・エラー処理を備えた文書処理ワークフローを構成する。
- 自作RAG基盤を持たず、CLIとセマンティック検索でコーディングエージェントに文書分析を任せる。
- ルール・信頼度スコア付きの分類を前処理に置き、後段の処理を振り分ける。

## 使いどころ

- 文書の分類と抽出を前処理にしたエージェントを作る企業の開発チーム。
- エージェント構築工数の削減効果を知りたい導入検討者。
