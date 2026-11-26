---
type: announcement
title: RankGPTとComposable Retrieversなどの週次アップデート
title_original: LlamaIndex Newsletter 2024-01-23
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- rag
- text-to-sql
- eval
components:
- LlamaIndex
- RankGPT
- Tonic Validate
- LlamaIndex.TS
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2024-01-23-11ee2c211bab
published_at: '2024-01-23'
---

## 概要

LLMで再ランキングするRankGPT、複数の検索器を組み合わせるComposable Retrievers、表データQAのチュートリアル、長文脈埋め込みなどを紹介する週次ニュースレター。

## 設計のポイント

- 多数の候補はスライディングウィンドウでLLMに再ランキングさせる。
- 検索器やRAGパイプラインは合成可能な部品にする。

## 使いどころ

- 検索精度の改善手法を探すRAG開発者。
