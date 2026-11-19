---
type: guidance
title: 帳票OCRでテンプレート方式が破綻する理由と対処
title_original: 'OCR for forms: why templates fail and what works'
company: LlamaIndex
industry: financial-services
cloud: []
patterns:
- document-processing
- human-in-the-loop
components:
- LlamaParse
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ocr-for-forms
published_at: '2026-11-18'
---

## 概要

帳票処理でテンプレートやゾーン指定のOCRが本番で壊れる理由と、代わりの構成を解説する。ラベルと値の関係、チェックボックス、手書き、読み順の不安定さが課題になる。取り込みから分類、スキーマ抽出、検証、信頼度スコアによる例外ルーティングまでのワークフローを示す。

## 設計のポイント

- レイアウトに依存せず、ラベルと値の対応を認識層で捉える。
- 信頼度スコアで低確信の項目を人手確認に回す。
- 添付書類や署名・同意の有無も帳票の一部として扱う。

## 使いどころ

- ローン申込書や保険請求書など大量の帳票を処理する業務。
