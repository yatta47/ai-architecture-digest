---
type: opinion
title: 文書パース評価ベンチマークの設計基準とParseBench-2の重大度ポリシー
title_original: Building Toward a Perfect Document Parsing Benchmark
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
components:
- ParseBench-2
- OmniDocBench
- olmOCR-bench
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-toward-a-perfect-document-parsing-benchmark
published_at: '2026-11-16'
---

## 概要

LlamaIndexは文書パースのベンチマークに必要な6つの基準を整理し、既存指標が誤りの重大度を反映しない問題を示した。ParseBench-2では誤りの種類ごとの重大度ポリシーを定め、決定的な指標をそれに合わせて最適化する。

## 設計のポイント

- テキスト・表・チャート・フォームなど次元ごとに指標を分け、値と見出しの対応ずれも別の誤りとして扱う。
- エラー種別ごとの重大度を明示し、決定的な指標をそれに合わせて調整する。
- 対象文書の部分集合や重みをユーザーが調整できるようにし、自社ワークロードに合わせる。
- 固定データ・版管理でパーサ再実行とevaluator由来の揺れを区別する。

## 使いどころ

- 請求書や財務諸表などのパーサを選定・比較する担当者。
- 文書抽出パイプラインの品質回帰を検知したいチーム。
