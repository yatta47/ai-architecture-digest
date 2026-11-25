---
type: announcement
title: 'LlamaIndex週報: Workflows公開と文書単位の動的検索'
title_original: LlamaIndex Newsletter 2024-08-06
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- event-driven
- rag
- multi-agent-orchestration
components:
- LlamaIndex
- LlamaParse
- MLflow
- LlamaExtract
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-08-06
published_at: '2024-08-06'
---

## 概要

イベント駆動でマルチエージェントを組むWorkflowsの公開、チャンク単位とファイル単位を使い分ける動的検索、LongRAGパックを紹介する週次ニュースレター。

## 設計のポイント

- 各エージェントをイベントの購読・発行を行う部品にする。
- 検索、再ランク、合成を独立したイベント駆動のステップに分ける。

## 使いどころ

- Workflowsの導入を検討する開発者。
- 質問の性質で検索方式を変えたいQAアシスタントの設計。
