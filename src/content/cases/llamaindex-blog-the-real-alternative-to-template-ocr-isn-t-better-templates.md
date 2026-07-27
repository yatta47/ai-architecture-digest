---
type: guidance
title: 座標ベースのテンプレートOCRから意味理解ベースの抽出へ
title_original: The Real Alternative to Template OCR Isn't Better Templates
industry: cross-industry
cloud: []
patterns:
- document-processing
components: []
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/alternative-to-template-ocr
published_at: '2026-07-21'
---

## 概要

テンプレート型OCRはデモでは機能するが、実運用ではベンダーごとの請求書レイアウトの微妙な変化などに弱く、座標ベースのマッピングに依存する限り本質的に壊れやすいと指摘する。解決策は『より賢いテンプレート』ではなく、人間が読むように文書の内容を意味的に理解して抽出する、テンプレート不要のアプローチへの転換であると論じる。

## 設計のポイント

- 抽出ロジックをページ上の座標位置ではなく、データが『何であるか』という意味的な理解に基づかせる
- テンプレートライブラリの継続的なメンテナンスコストをなくし、レイアウト変更への追従を不要にする

## 使いどころ

- 多数のベンダーから届く請求書・発注書（AP）など、フォーマットが揺れる文書群の処理
- 支払通知（remittance advice）や医療のEOB、物流・通関書類など、フォーマットの標準化が難しい書類の抽出
