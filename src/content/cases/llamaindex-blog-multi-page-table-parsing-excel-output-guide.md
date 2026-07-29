---
type: announcement
title: LlamaParseに複数ページ表の連結パースとExcel出力機能を追加
title_original: 'New in LlamaParse: multi-page tables (beta) and Excel spreadsheet output'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LlamaParse
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/new-in-llamaparse-multi-page-tables-beta-and-excel-spreadsheet-output
published_at: '2026-07-28'
---

## 概要

ドキュメントパーサーLlamaParseに、複数ページにまたがる表を1つの表として連結する「Continuous Mode」ベータ機能と、表データをXLSX形式で直接出力する機能を追加したことを発表。

## 設計のポイント

- 表の断片化やヘッダー崩れを解消するため、ページを跨ぐ表を1クリックで連結するContinuous Modeを追加した
- Accurate/Premium/Continuousモードで解析した表をワンクリックでXLSX形式にエクスポートできるようにした

## 使いどころ

- 決算資料や仕様書など複数ページにまたがる表を含むPDFをRAGや分析用に取り込みたいケース
- 解析結果をExcelでそのまま編集・集計したい業務担当者
