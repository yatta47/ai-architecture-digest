---
type: announcement
title: OCRベンチマーク分析と非同期PDF処理・ワンクリックデプロイ（LlamaIndexニュースレター 2025-12-09）
title_original: LlamaIndex Newsletter 2025-12-09
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- eval
- parallel-execution
- ai-agent
components:
- LlamaParse
- LlamaSheets
- OlmOCR-Bench
- LlamaAgents
- Claude
- Cursor
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-12-09
published_at: '2025-12-09'
---

## 概要

OlmOCR-Benchのバイアスやテスト脆弱性を分析し、次世代の文書パース評価のあるべき姿を論じている。ほかに非同期PDF一括パース、コーディングエージェントでLlamaSheets出力を自動分析する手順、SEC財務分析などのテンプレートを3分未満でデプロイする機能を紹介する。

## 設計のポイント

- ベンチマークのバイアスと脆さを理解したうえで、自社文書での評価を設計する。
- セル単位メタデータ付きParquetをコーディングエージェントに渡し、スプレッドシート分析を自動化する。
- テンプレートとシークレット設定だけで自動ビルド・ホスティングする構成にする。

## 使いどころ

- 文書パース製品を比較評価する担当者。
- 財務レポートの定期分析を自動化したいアナリスト。
