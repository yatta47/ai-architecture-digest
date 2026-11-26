---
type: guidance
title: DBとPDFを横断して分析するtext-to-SQL連携エージェント
title_original: 'LlamaIndex + Waii: Combining Structured Data from your Database with PDFs for Enhanced Data Analysis'
company: Waii
industry: cross-industry
cloud:
- on-prem
patterns:
- text-to-sql
- ai-agent
- data-federation
components:
- Waii
- LlamaIndex
- LlamaHub
- Google Search
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-waii-combining-structured-data-from-your-database-with-pdfs-for-enhanced-data-647a9e66be82
published_at: '2023-12-06'
---

## 概要

LlamaIndexのエージェントがWaiiのtext-to-SQL APIや検索ツールを呼び分け、DBの集計結果をPDFの調査レポートと突き合わせる構成を示す。大規模スキーマには知識グラフ、意味ルール、コンパイラで対応する。

## 設計のポイント

- 全スキーマをLLMに渡さず、メタデータとクエリ履歴の知識グラフで対象テーブルを絞る。
- 生成SQLはコンパイラで構文エラーを修正し、意味ルールで正しさを補強する。
- DB照会・文書参照・Web検索をツールとして分け、エージェントに選ばせる。

## 使いどころ

- 数百テーブル規模のDBに自然言語分析を入れたい企業。
- 社内データと外部レポートを突き合わせるアナリスト。
