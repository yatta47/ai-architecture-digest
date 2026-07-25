---
type: guidance
title: Claude Codeにドキュメント理解を組み込む3つの方法
title_original: Adding Document Understanding to Claude Code
industry: cross-industry
cloud: []
patterns:
- ai-agent
- document-processing
- context-engineering
- rag
components:
- LlamaParse
- Claude Code
- MCP
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/adding-document-understanding-to-claude-code
published_at: '2026-07-19'
---

## 概要

企業データの9割は文書に閉じ込められているにもかかわらず、Claude Codeなどのコーディングエージェントは標準ではPDFや契約書を十分に扱えない。この記事はMCP経由でのドキュメントアクセス、CLIツールでの操作、エージェント自身に文書処理ワークフローを構築させる、という3つの補完的アプローチを解説している。

## 設計のポイント

- MCP経由でドキュメントを公開する前にLlamaParseなどでパース・チャンク化・埋め込みを行う前処理層を用意する
- 多数のMCPサーバーに分散アクセスする『フェデレーテッド検索』問題を避けるため、集中インデックス層を持つ
- Claude Codeのファイルサイズ・ページ数上限（32MB・100ページ）を超える文書には専用の解析/検索レイヤーが必須
- 文書理解はコンテキスト収集フェーズとコード生成フェーズの両方で活用できるよう設計する

## 使いどころ

- デューデリジェンスや契約レビューなど文書中心の業務アプリをコーディングエージェントで『ローコードIT』構築したい事業部門
- 自社のPRDや財務報告書、社内ポリシーを踏まえた具体的なコード生成をエージェントに行わせたい企業
