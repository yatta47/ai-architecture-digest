---
type: guidance
title: 保険金請求における複数書類横断のOCR・検証アーキテクチャ
title_original: 'OCR for Insurance Documents: Claims Processing'
industry: financial-services
cloud: []
patterns:
- document-processing
components:
- LlamaParse
outcome:
  type: risk-compliance
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/ocr-for-insurance-documents
published_at: '2026-07-18'
---

## 概要

保険金請求は病院請求書・退院サマリ・処方箋など複数の異種文書が組み合わさって初めて意味を持ち、単体のOCR精度だけでは不十分で書類間の相互検証が不可欠である。LlamaParseはレイアウト認識抽出と検証ロジックを組み合わせ、信頼度スコアに基づき自動処理と人手レビューを振り分けるワークフローを提供する。

## 設計のポイント

- 書類を分類してから抽出ロジックと検証ルールを適用する段階的なワークフローにする
- 請求額・請求書合計・処方内容など複数書類間のクロスドキュメント検証をパイプラインに組み込む
- 信頼度スコアにより自動処理と人手レビューの境界を動的に決定する

## 使いどころ

- 医療保険金請求など複数書類の突合が必要な保険業務の自動化
- 不正検知のために書類間の矛盾を検出したい保険会社の審査部門
