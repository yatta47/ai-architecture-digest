---
type: announcement
title: ワンクリック接続のコネクタディレクトリでClaudeに仕事の文脈を持たせる
title_original: Discover tools that work with Claude
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- Claude
- MCP
- Notion
- Canva
- Stripe
- Figma
- Socket
- Prisma
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/connectors-directory
published_at: '2025-07-14'
---

## 概要

AnthropicはClaudeとNotion・Canva・Stripeなどのリモートサービス、Figma・Socket・Prismaといったローカルデスクトップアプリをワンクリックで接続できるコネクタディレクトリを公開した。毎回コンテキストを説明し直す代わりに、Claudeが実際の作業ツールのデータに直接アクセスして応答できるようにする。

## 設計のポイント

- リモートサービスは認証(Connect)、ローカルアプリはデスクトップ拡張のインストールという2種類の接続方式に分け、リモートコネクタは有料プランユーザー限定で提供する。

## 使いどころ

- Linearのチケットからリリースノートを生成するなど、外部ツールの実データを踏まえた出力をClaudeに求めたい場合。
- Figmaファイルからプロダクションコードへといったツール間の変換フローにClaudeを組み込みたい場合。
