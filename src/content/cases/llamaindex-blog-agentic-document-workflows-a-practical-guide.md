---
type: announcement
title: 文書処理・検索・構造化出力・エージェントを統合するAgentic Document Workflows
title_original: Introducing Agentic Document Workflows
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- document-processing
- ai-agent
- rag
components:
- LlamaParse
- LlamaIndex Workflows
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/introducing-agentic-document-workflows
published_at: '2026-07-19'
---

## 概要

LlamaIndexが、従来のIDPやRAGの枠を超えてドキュメント処理・検索・構造化出力・エージェントオーケストレーションを統合するAgentic Document Workflows（ADW）を発表。契約レビューや保険金請求処理など、複数ステップにまたがる知的業務を自動化する。

## 設計のポイント

- ドキュメントエージェントがLlamaParseで抽出した情報と処理段階の状態を保持し続ける
- 抽出だけで終わらせず、ナレッジベース照合とビジネスルール適用まで一気通貫で行う
- 契約・保険・請求書など複数文書が絡む業務プロセス全体をエージェントが橋渡しする

## 使いどころ

- 契約書の条項抽出と規制要件の突合が必要なコンプライアンス業務
- 保険金請求や請求書処理など、抽出→検証→推奨アクションまで自動化したい業務
