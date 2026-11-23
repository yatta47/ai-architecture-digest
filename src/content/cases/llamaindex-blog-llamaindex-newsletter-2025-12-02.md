---
type: announcement
title: LlamaSheetsベータとLlamaExtractテーブル行モード（LlamaIndexニュースレター 2025-12-02）
title_original: LlamaIndex Newsletter 2025-12-02
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- context-engineering
components:
- LlamaSheets
- LlamaExtract
- LlamaClassify
- LlamaAgents
- Claude Code
- Cursor
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-12-02
published_at: '2025-12-02'
---

## 概要

LlamaSheetsのベータ公開、請求書や財務報告書の行単位抽出を可能にするLlamaExtractのテーブル行モードなどを紹介している。長い文書で繰り返しエンティティが欠落する問題に対し、文書を分割してエンティティごとに抽出し網羅性を確保する。コーディングエージェントに適切な文脈を与えてLlamaSheets活用エージェントを作らせるチュートリアルもある。

## 設計のポイント

- 長文書は分割してエンティティ単位で抽出し、取りこぼしを防ぐ。
- 領域分類と多段処理でスプレッドシートを構造化する。
- コーディングエージェントに製品固有の文脈を与えて実装を支援させる。

## 使いどころ

- 請求書・在庫一覧など行数の多い表を抽出する業務。
- 学習資料などを自動分類・要約するアプリを作る開発者。
