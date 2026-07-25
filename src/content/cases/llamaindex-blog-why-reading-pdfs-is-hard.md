---
type: guidance
title: 'PDFはなぜ機械可読ではないのか: グリフ座標としてのテキストと読み順推定の限界'
title_original: Why Reading PDFs Is Hard
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- Tesseract
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/why-reading-pdfs-is-hard
published_at: '2026-07-19'
---

## 概要

PDFはPostScript由来の描画命令の集合であり、文字や表・読み順といった意味構造を一切持たないため、テキスト抽出・表検出・読み順復元はすべてヒューリスティックによる推測にならざるを得ないと解説する。フォントのサブセット化やToUnicode CMapの欠落によって、見た目は正しくてもコピーすると文字化けするケースがあることも示す。

## 設計のポイント

- PDFの表は罫線とテキストが完全に独立した描画命令であり、線の交点からセル境界を推測し空間的包含関係でテキストを紐づける必要がある
- コンテンツストリーム内の描画命令の順序は視覚的な読み順と無関係なため、座標クラスタリングによる行・列・段の再構築が必須
- Tagged PDF(構造タグ)は仕様上存在するが実際にはほとんど使われておらず、パース時に頼れる仕組みではない

## 使いどころ

- RAGパイプラインやディープリサーチエージェントでPDFを大量に取り込む前に、パーサー選定の判断材料が欲しいエンジニア
- 自前でPDFパース処理を実装しようとしていて、落とし穴を事前に把握したい開発者
