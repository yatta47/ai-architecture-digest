---
type: guidance
title: 法律文書OCRで『まあまあの精度』が訴訟リスクになる理由とエージェント型OCRの対処
title_original: 'OCR for Legal Documents: Automating Accuracy and Compliance'
industry: other
cloud: []
patterns:
- document-processing
components:
- LlamaParse
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ocr-for-legal-documents
published_at: '2026-07-19'
---

## 概要

法律文書は印刷本文・手書き注記・押印・署名・複雑な引用形式が混在し、従来型OCRが最も苦手とする領域である。eディスカバリでのキーワード見落としや契約書の数字誤読は訴訟リスクや懲戒リスクに直結するため、98%の精度でも5万ページ規模では1,000ページの誤りが生じると指摘し、エージェント型OCRによる対処を論じる。

## 設計のポイント

- 法律文書の精度要件は他業界と非対称で、わずかな誤読が制裁動議や免責放棄リスクに直結するため精度閾値の考え方自体を変える必要がある
- OCRの誤りは処理ログ上に現れず『処理済み』に見えるため、キーワード検索のヒット漏れが静かに発生する
- 本文・注記・押印・別紙(異なるスキャン品質)など複数の異種コンテンツを単一パスで同一に扱わない設計にする

## 使いどころ

- eディスカバリで数百万ページのキーワード検索精度を担保したい訴訟支援チーム
- 契約書のデューデリジェンスで金額・期日などの誤読を防ぎたい法務部門
