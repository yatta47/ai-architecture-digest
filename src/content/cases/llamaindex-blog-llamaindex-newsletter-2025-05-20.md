---
type: announcement
title: 'LlamaIndex: Memory APIとターミナル型コーディングエージェントTig'
title_original: LlamaIndex Newsletter 2025-05-20
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- memory-consolidation
- ai-agent
- event-driven
components:
- LlamaIndex Memory
- LlamaParse
- LlamaExtract
- Workflows
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-05-20
published_at: '2025-05-20'
---

## 概要

短期チャット履歴と長期記憶を組み合わせる新Memory API（Static/FactExtraction/Vectorブロック）、LlamaParseの改善、Workflows製のTigを紹介するニュースレター。

## 設計のポイント

- 短期メモリと長期メモリをプラグ可能なブロックとして組み合わせる
- 事実抽出ブロックやベクトルブロックで長期記憶を構成する
- イベント駆動ワークフローでオーケストレーターが検索と集約を担うマルチエージェントを構成する

## 使いどころ

- 文脈を跨いだ会話をするエージェントを作る場面
- コーディングエージェントをOSSで自作したい場面
