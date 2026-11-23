---
type: announcement
title: LlamaSplit・仮想ファイルシステムによる安全なコーディングエージェント・非同期バッチPDF処理（LlamaIndexニュースレター 2025-12-16）
title_original: LlamaIndex Newsletter 2025-12-16
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- parallel-execution
- guardrails
components:
- LlamaSplit
- LlamaSheets
- LlamaParse
- SemTools
- LlamaAgents
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-12-16
published_at: '2025-12-16'
---

## 概要

文書を自動分割するLlamaSplit API（ベータ）、仮想ファイルシステムで誤削除を防ぐコーディングエージェント、LlamaSheetsの公開ベータなどを紹介している。asyncioとセマフォでPDFフォルダを並列パースする手法や、SemToolsのaskコマンドも取り上げる。

## 設計のポイント

- 仮想ファイルシステムで隔離し、コーディングエージェントによる誤削除を防ぎつつ機能は維持する。
- asyncioとセマフォで同時実行数を制御し、レート制限を避けながらスループットを最大化する。
- 分割結果にページ範囲と信頼度スコアを付与して下流の判断に使えるようにする。

## 使いどころ

- 大量PDFをバッチ処理する文書基盤の運用者。
- コーディングエージェントを安全に社内で運用したい開発チーム。
