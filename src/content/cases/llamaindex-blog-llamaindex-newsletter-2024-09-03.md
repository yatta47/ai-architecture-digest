---
type: announcement
title: 'LlamaIndex週報: 動的RAG検索・Workflows解説・GymNationのエージェント事例'
title_original: LlamaIndex Newsletter 2024-09-03
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- ai-agent
- event-driven
components:
- LlamaIndex
- LlamaParse
- Cerebras
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-09-03
published_at: '2024-09-03'
---

## 概要

動的に検索粒度を切り替えるRAGやレポート生成エージェントのガイド、Workflowsのチュートリアルをまとめた週次ニュースレター。GymNationが営業・会員対応にAIエージェントを導入した事例も紹介している。

## 設計のポイント

- 質問に応じてチャンク単位と文書単位の検索をルーターで切り替える。
- ループ・分岐・状態管理が必要な処理はイベント駆動のワークフローで組む。

## 使いどころ

- LlamaIndexの新機能やガイドを短時間で把握したい開発者。
- 文書全体の取得が必要なRAGの設計例を探すとき。
