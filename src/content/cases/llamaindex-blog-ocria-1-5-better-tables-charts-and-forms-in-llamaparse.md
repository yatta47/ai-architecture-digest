---
type: announcement
title: LlamaParseの文書解析モデルOCRia-1.5
title_original: 'Introducing OCRia-1.5: better tables, charts and forms in LlamaParse'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- inference-optimization
- cost-optimization
components:
- LlamaParse
- OCRia-1.5
- ParseBench-2
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-ocria-1-5
published_at: '2026-11-18'
---

## 概要

LlamaIndexが文書解析モデルOCRia-1.5を公開した。4B版はAgenticティア、新しい2B版はCost Effectiveティアで動く。ParseBench-2で表は86.5から90.1（Agentic）に向上し、チャートとフォームも改善、バウンディングボックスの精度も上がった。

## 設計のポイント

- 精度重視の4Bと低コストの2Bの2段階を用意し、ティアで使い分ける。
- 表の結合ヘッダーやフォームのチェック状態など、構造の保持を重点改善する。
- バウンディングボックスの精度を上げ、抽出値の根拠位置を示しやすくする。

## 使いどころ

- 財務諸表や帳票を大量に構造化するパイプラインで、精度とコストを調整したい場面。
