---
type: announcement
title: Claude CodeでリモートMCPサーバーに接続できるように
title_original: Remote MCP support in Claude Code
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- Claude Code
- MCP
- Sentry MCP server
- Linear MCP server
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-code-remote-mcp
published_at: '2025-06-18'
---

## 概要

Claude Codeがリモートの MCP サーバーに対応し、SentryやLinearなど外部ツールをローカルサーバー管理なしで接続できるようになった。OAuthによる認証もサポートし、開発者はターミナルを離れずにコンテキストを取り込みながら開発を進められる。

## 設計のポイント

- リモートMCPサーバーへの接続をURL登録のみで完結させ、ローカルでのサーバー運用・スケーリングの負担をベンダー側に移す
- ネイティブOAuthでの認証によりAPIキー管理を不要にし、安全な接続を簡素化する

## 使いどころ

- Sentryのエラー情報をコンテキストとして参照しながらデバッグしたい開発者
- Linearなどのプロジェクト管理ツールと連携し計画・実装・課題管理をシームレスに行いたいチーム
