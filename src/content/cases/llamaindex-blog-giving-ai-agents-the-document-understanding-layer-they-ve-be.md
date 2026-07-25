---
type: announcement
title: LlamaParse/LiteParseをコーディングエージェント向け『スキル』として提供し文書理解層を与える
title_original: 'Beyond Raw Text: How LlamaParse and LiteParse Give Agents Real Document Understanding'
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- document-processing
- context-engineering
components:
- LlamaParse
- LiteParse
- Claude Code
- OpenCode
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/beyond-raw-text-how-llamaparse-and-liteparse-give-agents-real-document-understanding
published_at: '2026-07-19'
---

## 概要

汎用エージェントランタイムが標準で持つexecやシンプルな画像ツールはPDFの表・画像・レイアウトを崩してしまうため、LlamaIndexはClaude CodeやOpenCodeなどのスキル対応エージェント向けにLlamaParse(クラウド)とLiteParse(ローカル)のスキルを提供し、構造化された文書理解層をエージェントに与える。MCPサーバーのような複雑な設定なしに、スキルとしてコンテキストへ直接注入できる。

## 設計のポイント

- MCPサーバーを立てずに、スキルオーバーレイとしてエージェントのコンテキストへ直接パーサーの使い方を注入する設計にした
- 複雑なレイアウトはクラウドのLlamaParse(agentic/agentic_plusティア)、速度・プライバシー重視の用途はローカルのLiteParseと使い分けられるようにした
- ページ範囲指定・バッチ処理・設定ファイル再利用など、エージェントが再現可能な文書処理パイプラインを組めるようにした

## 使いどころ

- 財務報告書から表構造を保ったままデータを抽出したいエージェントワークフロー
- 条項の階層構造や相互参照を保持したまま法務契約書を解析したいケース
- セキュリティ上クラウド送信できない文書をローカルのみで処理したい場合
