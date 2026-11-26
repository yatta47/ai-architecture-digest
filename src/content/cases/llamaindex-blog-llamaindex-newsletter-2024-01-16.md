---
type: announcement
title: Chain-of-Tableと並列取り込みなどの週次アップデート
title_original: LlamaIndex Newsletter 2024-01-16
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- parallel-execution
- document-processing
components:
- LlamaIndex
- Chain-of-Table
- TogetherAI
- AgentSearch
- Azure Cosmos DB
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-01-16-752195bed96d
published_at: '2024-01-16'
---

## 概要

表を段階的に操作して推論するChain-of-Table、埋め込み類似度による意味的分割、最大15倍速い並列取り込み、TogetherAI埋め込み対応などを紹介する週次ニュースレター。

## 設計のポイント

- 取り込み処理は並列化してスループットを上げる。
- 文の埋め込み類似度を使って文書の分割位置を決める。

## 使いどころ

- 大量文書の取り込み時間を短縮したいチーム。
- 表データへの質問応答を作る開発者。
