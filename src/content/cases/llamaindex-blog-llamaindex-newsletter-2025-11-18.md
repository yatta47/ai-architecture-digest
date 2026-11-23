---
type: announcement
title: エージェント型OCRとPathwork保険書類処理事例（LlamaIndexニュースレター 2025-11-18）
title_original: LlamaIndex Newsletter 2025-11-18
company: LlamaIndex
industry: financial-services
cloud: []
patterns:
- document-processing
- ai-agent
- event-driven
components:
- LlamaParse
- LlamaClassify
- LlamaExtract
- LlamaAgents
- Resend
outcome:
  type: speed
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-11-18
published_at: '2025-11-18'
---

## 概要

折れ線グラフの輪郭を追って数値を抽出する実験的なチャートパース、エージェント型OCRで90%超のパススルー率を目指すDocument AI構成を紹介している。Pathworkの生命保険書類処理は週5,000ページから40,000ページへ拡大しスループットが8倍になったと報告されている。受信メールをトリガーに分類・抽出・返信するワークフローも示す。

## 設計のポイント

- OCRにLLMワークフローを組み合わせ、人手を介さず通過する割合を高める。
- メールのWebhookをトリガーに分類・抽出・自動返信まで一貫して処理する。
- 古いスキャンPDFや医療記録など難しい入力を想定して基盤を選ぶ。

## 使いどころ

- 保険の申込・医療記録など大量の紙由来文書を扱う業務。
- 請求書や経費のメール受付を自動化したい財務部門。
