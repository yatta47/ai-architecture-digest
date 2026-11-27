---
type: guidance
title: レイアウトを保つPDF解析LayoutPDFReaderで文脈を考慮したチャンク分割
title_original: 'Mastering PDFs: Extracting Sections, Headings, Paragraphs, and Tables with Cutting-Edge Parser'
industry: cross-industry
cloud: []
patterns:
- document-processing
- rag
components:
- LayoutPDFReader
- llmsherpa
- LlamaIndex
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/mastering-pdfs-extracting-sections-headings-paragraphs-and-tables-with-cutting-edge-parser-faea18870125
published_at: '2023-10-18'
---

## 概要

PDFの節・段落・表・リストの階層構造を解析するLayoutPDFReaderで、文脈を考慮したチャンク分割を行う方法を紹介する。テキスト層を持つPDFが対象で、OCRには対応していない。

## 設計のポイント

- 固定長ではなく文書構造に沿ってチャンクを分割する。
- 各チャンクに節見出しの階層を文脈として含める。
- 外部の解析APIを使う場合は、データの扱いと自前ホストの要否を確認する。

## 使いどころ

- 契約書や論文など構造を持つPDFをRAGに取り込むチーム。
