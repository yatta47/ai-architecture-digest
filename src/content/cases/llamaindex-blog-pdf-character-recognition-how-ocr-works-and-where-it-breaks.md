---
type: guidance
title: PDFのOCR要否の見分け方と、レイアウトが複雑になるとOCRが崩れる理由
title_original: 'PDF Character Recognition: How OCR Works and Where It Breaks'
industry: cross-industry
cloud:
- aws
patterns:
- document-processing
components:
- Adobe Acrobat
- Tesseract
- ABBYY FineReader
- AWS Textract
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/pdf-character-recognition
published_at: '2026-07-18'
---

## 概要

スキャンPDFはテキストではなく画像であり、OCRによって検索・選択可能なテキスト層に変換する必要がある。従来型OCRは単純な単一カラム文書には強いが、複数カラムや表、チャート、手書き文字など複雑なレイアウトでは読み順の破壊や表構造の消失といった失敗が起きやすいと解説する。

## 設計のポイント

- PDFにテキスト層があるかはテキスト選択を試すだけで判定でき、OCRが必要かどうかの最初の切り分けになる
- OCR出力は元のスキャン画像に隠しテキスト層を重ねる『検索可能PDF』と、フォント文字に置き換える『編集可能PDF』の2種類があり、用途で使い分ける
- 従来型OCRはページを平坦な文字グリッドとして扱うため、多カラム・表・チャートなど構造を持つレイアウトで読み順や列構造が崩壊する

## 使いどころ

- スキャン文書をアーカイブ・検索可能にしたいバックオフィス業務
- スクリーンリーダー対応など、視覚障害者向けのアクセシビリティ対応が必要な文書処理
- 多カラム・表を含む複雑な文書をAIエージェントで自動処理したい開発者(単純OCRでは不十分と判断する材料に)
