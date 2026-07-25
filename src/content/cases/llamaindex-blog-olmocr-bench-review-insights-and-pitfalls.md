---
type: opinion
title: OCRベンチマークOlmOCR-Benchの功績と限界を検証する
title_original: 'OlmOCR-Bench Review: Insights and Pitfalls on an OCR Benchmark'
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
components:
- OlmOCR-Bench
- OlmOCR2
- dots.OCR
- PaddleOCR
- DeepSeek-OCR
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/olmocr-bench-review-insights-and-pitfalls-on-an-ocr-benchmark
published_at: '2026-07-19'
---

## 概要

LlamaIndexが多数の顧客向け文書処理で得た知見をもとに、1400件超のPDFと7000件超のバイナリ単体テストからなるOCRベンチマークOlmOCR-Benchを検証している。編集距離やLLM審査のような曖昧な指標より検証可能な単体テストが優れる点を評価しつつ、学術文書偏重で請求書やフォーム、手書き、多言語などの実務データを十分カバーしていない点を指摘している。

## 設計のポイント

- バイナリのpass/fail形式のユニットテストにより、編集距離やLLM審査では見逃されがちな構造的な誤り(読み順崩れなど)を検出できる
- カテゴリ別サブスコアを平均して総合点を出すことで、要素ごとの精度をより粒度細かく可視化できる
- ベンチマークデータが学術論文・書籍中心に偏っており、請求書や複雑な表、手書き、非英語文書など実務でよくある文書種別を十分にカバーしていない

## 使いどころ

- 文書解析システムの精度を定量的に比較検討したいプロダクトチーム
- 学術論文中心ではない請求書・フォームなど業務文書向けにOCR精度を評価する基準を検討しているチーム
