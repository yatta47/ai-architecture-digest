---
type: guidance
title: PDF内の表を構造化データに変換するテーブルOCRの設計
title_original: 'OCR for Tables: How to Extract Structured Data from Documents'
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ocr-for-tables
published_at: '2026-07-18'
---

## 概要

PDF上の表は見た目は整っていてもセル間の関係性を持たないただの文字列の集まりであり、単純なOCRでは列のズレや数値の誤対応が起きやすい。LlamaParseは検出・構造認識・データ抽出の3段階に分けて処理し、整合性検証を挟むことで請求書などの表データを信頼できるJSON/CSVへ変換する。

## 設計のポイント

- 表の抽出を「検出」「構造認識」「データ抽出」の3フェーズに分離し、各段階で誤りを検知できるようにする
- 結合セルや複数行にまたがる項目はレイアウト解析で論理的な1レコードとして再構成する
- 抽出後に算術整合性チェック（小計・合計の検算）やデータ型検証を行い、構造的な誤りが下流に伝播するのを防ぐ

## 使いどころ

- 請求書・財務報告書など罫線のない表からの構造化データ抽出
- 金融・物流・医療など表形式の帳票を大量に処理する業務のOCR基盤
