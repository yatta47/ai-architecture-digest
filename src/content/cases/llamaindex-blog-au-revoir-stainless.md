---
type: opinion
title: LlamaIndexがSDK生成基盤StainlessからのPost-Anthropic移行で学んだこと
title_original: Au revoir, Stainless
ai_relevant: false
company: LlamaIndex
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/au-revoir-stainless
published_at: '2026-05-18'
---

## 概要

LlamaIndexはLlamaParseの公式SDK(Python/TypeScript/Go等)をOpenAPI仕様から生成するためにStainlessを採用してきたが、StainlessチームがAnthropicに参加しホステッドSDK生成サービスが終了することになり、移行を迫られた。同社はStainless採用の理由(言語ネイティブなSDK、1つのAPI定義から多言語生成、生成コードの所有権、API設計の改善圧力)と、生成SDKの利用者が依存するのはOpenAPI仕様ではなく生成後のインターフェース自体だという教訓を振り返っている。
