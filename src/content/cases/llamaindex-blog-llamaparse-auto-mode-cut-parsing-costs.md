---
type: announcement
title: LlamaParse Auto Modeによるパース精度とコストの両立
title_original: Optimize parsing costs with LlamaParse Auto Mode
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- cost-optimization
components:
- LlamaParse
outcome:
  type: cost
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/optimize-parsing-costs-with-llamaparse-auto-mode
published_at: '2026-07-20'
---

## 概要

LlamaParseの新機能Auto Modeは、テーブルや画像、特定文字列、正規表現などのトリガーをページ単位で検知し、必要なページだけ高精度なPremiumモードに自動切り替えする。長文ドキュメント全体を一律で高精度パースするのではなく、コストと精度のバランスをページ粒度で最適化する。

## 設計のポイント

- ページ単位でテーブル/画像/特定文字列/正規表現のトリガーを検知し、必要なページだけPremiumモードに自動切り替えする
- 全ページ一律の高精度パースではなく、コストと精度のバランスをページ粒度で最適化する

## 使いどころ

- 図表や画像が一部ページに偏る長文ドキュメントを扱うRAGパイプライン
- 高精度パースのコストを抑えつつ複雑な表・数式・図を含む文書を大量処理したいチーム
