---
type: announcement
title: 文書パースに特化した4B VLM「OCRia-1」の公開
title_original: Introducing OCRia-1
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- OCRia-1
- ParseBench
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/parse-ocria-1
published_at: '2026-10-22'
---

## 概要

LlamaIndexは、文書パース用の40億パラメータVLM「OCRia-1」を公開した。ParseBenchで87.4点を記録し、35B未満のパースモデルとして最高、次点より12.1点上回ると主張する。表の評価でも他の3つの外部ベンチマークで首位とする。

## 設計のポイント

- 小型VLMに特化させ、精度・コスト・遅延を同時に狙う。
- 表・グラフ・書式付きテキストを含む財務書類などの複雑な文書の再構成を評価の中心に置く。

## 使いどころ

- エージェント自動化の前段で、財務報告書や保険書類を大量に構造化したい業務。
