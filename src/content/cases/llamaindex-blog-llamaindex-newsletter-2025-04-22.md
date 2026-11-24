---
type: announcement
title: 'LlamaIndex: LlamaResearcherと階層型マルチエージェント'
title_original: LlamaIndex Newsletter 2025-04-22
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
- document-processing
components:
- Llama 4
- LlamaExtract
- Gemini 2.5 Flash
- GPT-4.1
- A2A
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-04-22
published_at: '2025-04-22'
---

## 概要

Llama4を使ったOSSのDeep Research、決算書から財務指標を抽出する株式調査エージェント、スーパーバイザーによる階層型マルチエージェント、A2A対応を紹介。

## 設計のポイント

- クエリを評価しサブクエリに展開してWeb検索しエッセイを生成する
- 中央のスーパーバイザーがタスクを委譲する階層構造にする
- A2Aプロトコルで異種技術のエージェント間を連携する

## 使いどころ

- 財務分析を非構造化資料から自動化したい場面
- 複数エージェントの委譲設計を検討する場面
