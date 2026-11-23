---
type: announcement
title: 文書抽出・スプレッドシート解析・フォーム入力エージェントの新機能紹介（LlamaIndexニュースレター 2026-01-13）
title_original: LlamaIndex Newsletter 2026-01-13
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- human-in-the-loop
components:
- LlamaSheets
- LlamaSplit
- LlamaExtract
- LlamaParse
- LlamaAgent Workflows
- Claude Code SDK
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2026-01-13
published_at: '2026-01-13'
---

## 概要

LlamaIndexの週次ニュースレターで、自然言語でスキーマを定義する文書抽出、LlamaSplitによる履歴書束の分割とLlamaExtractでの構造化抽出、フォーム自動入力アプリを紹介している。LlamaSheetsはベータ公開で、崩れたExcelをセル単位の特徴量付きParquetに変換する。

## 設計のポイント

- 束ねられた文書をまず分割し、その後カスタムスキーマで抽出する二段構成で繰り返し要素の取りこぼしを防ぐ。
- 抽出結果に信頼度スコアを付けて後段のマッチング処理に渡す。
- スプレッドシートはParquet化してpandas/polars/DuckDBで扱えるようにする。

## 使いどころ

- 履歴書や財務書類など長い束ね文書を処理する人事・経理部門。
- 結合セルや多段ヘッダーを持つ複雑なExcelを解析したいデータチーム。
- 領収書から経費精算書を自動作成したい業務。
