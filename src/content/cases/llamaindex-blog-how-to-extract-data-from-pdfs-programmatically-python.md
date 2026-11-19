---
type: guidance
title: PDFからPythonでデータを抽出する手順
title_original: How to extract data from PDFs programmatically (Python)
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
components:
- pypdf
- pdfplumber
- PyMuPDF
- LlamaParse
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/how-to-extract-data-from-pdfs
published_at: '2026-11-18'
---

## 概要

PDFのデータ抽出を、テキスト層の有無の確認から始めて整理した手引き。電子生成PDFではpypdf・pdfplumber・PyMuPDFを使い分け、表やスキャンはOCRに回す。最後に、文字列をフィールドへ対応づける工程を含めてLlamaParseで一本化する流れを示す。

## 設計のポイント

- 最初にテキスト層の有無で処理経路を分岐する。
- 抽出した文字列を、スキーマに沿ったフィールドへ対応づける工程を分けて考える。
- 表やスキャンなど難しい約1割の文書が構成選定を左右する。

## 使いどころ

- 請求書や銀行明細など多様なPDFを取り込むパイプラインの設計時。
