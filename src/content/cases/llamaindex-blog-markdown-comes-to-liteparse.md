---
type: announcement
title: LiteParse、モデル不要のヒューリスティックでPDFをMarkdown変換
title_original: Markdown Comes to LiteParse
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- LiteParse
- PDFium
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/markdown-comes-to-liteparse
published_at: '2026-07-18'
---

## 概要

LlamaIndexはLiteParse v2.1で、AIモデルを使わないヒューリスティックのみでPDFをMarkdownに変換するパイプラインを発表。フォントサイズや文字位置などの信号を組み合わせてテーブルや見出しなどの要素を分類し、ParseBench・opendataloader-bench・olmOCR-benchの3ベンチマークでモデルフリー手法として最速かつ高スコアを達成した。

## 設計のポイント

- フォントサイズや文字位置などPDF自体が持つ信号を特徴量として扱いMarkdown要素をルールベースで分類する
- Apache-2.0ライセンスとWASM対応により、ブラウザを含む複数ランタイムで同一エンジンを動かせるようにする
- AIモデルを使わないことで速度の上限を作らず、ms/page単位の高速処理を優先する設計判断を行う

## 使いどころ

- AGPL等のライセンス制約を避けたい商用製品でのPDF→Markdown変換
- 大量のPDFを低コスト・低レイテンシで前処理したいドキュメントパイプライン
