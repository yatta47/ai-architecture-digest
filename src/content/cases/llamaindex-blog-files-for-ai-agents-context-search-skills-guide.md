---
type: opinion
title: ファイルシステムをエージェントの文脈管理の中核インターフェースにする発想
title_original: Files Are All You Need
industry: cross-industry
cloud: []
patterns:
- context-engineering
- memory-consolidation
- ai-agent
- rag
components:
- Claude Code
- Cursor
- MCP
- CLAUDE.md
- semtools
outcome:
  type: quality
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/files-are-all-you-need
published_at: '2026-07-19'
---

## 概要

LlamaIndexのブログが、コーディングエージェントを中心に「ファイル」が長期会話履歴の保存、大量の外部コンテキスト取得(RAGの代替)、MCPに代わる「スキル」提供という3つの用途でエージェントの中核インターフェースになりつつあるトレンドを論じている。CLIやgrep/lsのようなファイルシステム操作と少数のツールだけで、多数のMCPツールを持つエージェントと同等以上の汎用性が得られると主張する。

## 設計のポイント

- コンテキストウィンドウの制約に対応するため、会話履歴やリサーチ内容をファイルに退避し必要な時に読み直せるようにする
- 素朴なセマンティック検索より、ファイルシステム探索(ls/grep/Read)の方が中小規模のドキュメント集合で精度が高くなり得る点を踏まえて設計する
- MCPツールを大量に定義する代わりに、ファイル+CLI+コードインタプリタ+Web取得という少数ツールでエージェントを構成する
- 大きなMCPツール応答はファイルにダンプしてから後処理させ、コンテキストの肥大化と切り詰めを回避する

## 使いどころ

- 長時間稼働するコーディングエージェントでコンテキスト圧縮によるタスク破綻を防ぎたい開発者
- 中小規模のドキュメント集合に対し素朴なRAGより高精度な検索を実現したいチーム
- MCPサーバーを都度実装せず、ファイルベースの「スキル」でエージェントに能力を素早く追加したい開発者
