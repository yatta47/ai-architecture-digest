---
type: announcement
title: 'LlamaIndexニュースレター: パース/抽出の使い分けとLlamaAgents本番展開'
title_original: LlamaIndex Newsletter 2025-10-14
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- event-driven
components:
- LlamaParse
- LlamaClassify
- LlamaAgents
- EmbeddingGemma
- Claude Sonnet 4.5
- AG-UI
- CopilotKit
- Composio
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-10-14
published_at: '2025-10-14'
---

## 概要

LlamaIndexの週次ニュースレター。文書処理をパース（文脈保持）と抽出（スキーマ検証付き）に整理した解説、推論付き分類サービスLlamaClassify、テンプレート付きでワンクリック展開できるLlamaAgentsを紹介している。

## 設計のポイント

- 全文脈を残すパースと、項目指定でスキーマ検証する抽出を目的別に使い分ける。
- 分類結果に判断理由を付けさせ、法務文書などで説明可能性を確保する。
- イベント駆動のエージェントで仕様書から構造化データを抽出し、レポート生成まで自動化する。

## 使いどころ

- 請求書処理や契約レビューの文書エージェントを素早く立ち上げたい開発チーム。
- オンデバイスRAGで軽量な埋め込みモデルを使いたい場面。
