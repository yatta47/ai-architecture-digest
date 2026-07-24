---
type: guidance
title: KYC文書処理で標準OCRが限界を迎える理由とエージェント型OCRへの移行
title_original: 'OCR for KYC: Why Standard Text Extraction Falls Short'
industry: financial-services
cloud: []
patterns:
- document-processing
- ai-agent
components: []
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ocr-for-kyc
published_at: '2026-07-18'
---

## 概要

標準的なOCRはホログラムや非ラテン文字、MRZなどの構造化ゾーンを正しく扱えず、KYC(顧客確認)業務で求められるフィールドレベル精度99.9%という基準を満たせないと指摘。信頼度スコアや文書構造理解を備えたエージェント型OCRへの移行が、AML誤検知や手動レビューコストの削減に必要だと論じる。

## 設計のポイント

- フィールドレベル精度99.9%を目標値としてOCR品質を評価する
- MRZなど構造化ゾーンをチェックサム込みで解釈できる専用パーサーを用意する
- 抽出結果に信頼度スコアを付与し低信頼のケースのみ人手レビューに回す

## 使いどころ

- 身分証明書の真正性確認が必要な銀行・フィンテックのオンボーディング
- 大量のKYC文書を処理し誤検知コストを抑えたいコンプライアンスチーム
