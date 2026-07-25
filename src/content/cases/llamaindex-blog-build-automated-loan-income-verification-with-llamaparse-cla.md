---
type: case
title: 4種類のローン書類を横断して収入の整合性を検証する自動化パイプライン
title_original: Build Automated Loan Income Verification with LlamaParse & Claude Agent SDK
industry: financial-services
cloud: []
patterns:
- document-processing
- ai-agent
components:
- LlamaExtract
- Claude
- Pydantic
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/build-automated-loan-income-verification-with-llamaparse-claude-agent-sdk
published_at: '2026-07-18'
---

## 概要

500ページを超えることもある住宅ローン審査書類のうち、収入の整合性確認（ローン申込書・W-2・給与明細・銀行明細の間で数字が一致するか）は本来機械的な作業でありながら審査担当者の時間の40〜60%を消費している。LlamaExtractで4種類の書類を構造化抽出し、Claudeが雇用主名の表記ゆれや説明のつかない入金パターンを検出してHTMLの審査推奨レポートを生成するパイプラインを構築した。

## 設計のポイント

- 書類種別ごとにPydanticスキーマとフィールド説明を定義し、書式の異なる文書でも同じ抽出ロジックを再利用する
- 抽出（Extract）と横断検証（Claudeの推論）を役割分担し、構造化抽出は機械的に、整合性判断はLLM推論に任せる
- 抽出結果に信頼度スコアと出典引用を付与し、審査担当者が最終判断の根拠を追跡できるようにする

## 使いどころ

- 給与の増減や不明な入金など、書類間の矛盾を検出する必要がある住宅ローン審査
- 収入証明の自動突合により審査担当者の手作業レビューを削減したい金融機関
