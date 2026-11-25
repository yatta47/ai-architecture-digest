---
type: announcement
title: 'LlamaIndex週報: チャット・データコネクタ追加と人間参加型エージェント'
title_original: LlamaIndex Newsletter 2024-07-23
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- human-in-the-loop
- document-processing
components:
- LlamaParse
- LlamaAgents
- Claude 3.5 Sonnet
- GPT-4o
- RabbitMQ
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-07-23
published_at: '2024-07-23'
---

## 概要

LlamaParseのチャット機能とNotionやSlack等のコネクタ追加、Scaleport AIの事例、スライド向けマルチモーダルRAGなどを紹介する週次ニュースレター。llama-agentsで人を介在させる実装例も含む。

## 設計のポイント

- 人が担当する問い合わせはHumanServiceとしてエージェントと同じ仕組みに組み込む。
- 図表を含むスライドはテキストと画像を組み合わせて解析する。

## 使いどころ

- LlamaIndexの更新と事例を追う開発者。
- 人の確認を挟むマルチエージェントを検討する場合。
