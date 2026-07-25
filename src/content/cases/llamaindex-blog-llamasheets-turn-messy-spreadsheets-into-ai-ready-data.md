---
type: announcement
title: 乱れた表計算シートをAI利用可能なデータへ変換するLlamaSheets
title_original: 'Announcing LlamaSheets: Turn Messy Spreadsheets into AI-Ready Data (Beta)'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LlamaSheets
- LlamaParse
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/announcing-llamasheets-turn-messy-spreadsheets-into-ai-ready-data-beta
published_at: '2026-07-19'
---

## 概要

太字ヘッダーや色分け、結合セルなど視覚的書式で意味を表現する「乱れた」スプレッドシートを、セル単位の特徴量抽出とクラスタリング、領域分類、階層構造保持からなる多段階パイプラインで型付きParquetデータに正規化するLlamaSheetsのベータ提供を発表している。出力はエージェントや下流アプリケーションにそのまま利用できる。

## 設計のポイント

- セル単位で40以上の特徴量(位置・書式・データ型)を抽出しクラスタリングして領域を分類する
- 領域間の境界品質をスコアリングし、反復的に補正するAdaptive Table Segmentationで表の切れ目を特定する
- 複数レベルのヘッダーやマージセルなど階層構造を保持したまま型付きParquetとして出力する

## 使いどころ

- 結合セルや色分けなど視覚的な書式で意味を表現している複雑な財務モデルを自動構造化したい場合
- 書式がバラバラな複数拠点の売上シートを統合してエージェントに分析させたい場合
