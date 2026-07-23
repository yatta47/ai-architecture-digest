---
type: announcement
title: スラッシュコマンドやMCPサーバーを束ねて配布するClaude Codeプラグイン
title_original: Customize Claude Code with plugins
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- Claude Code
- MCP
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/claude-code-plugins
published_at: '2025-10-09'
---

## 概要

スラッシュコマンド・サブエージェント・MCPサーバー・フックをひとまとめにして単一コマンドでインストールできる「プラグイン」機能の発表。マーケットプレイスを通じてチームやコミュニティ間でベストプラクティスを共有できるようにする。

## 設計のポイント

- スラッシュコマンド・サブエージェント・MCPサーバー・フックを1つのパッケージとして配布する
- プラグインは必要な時だけ有効化しシステムプロンプトのコンテキスト肥大化を防ぐ
- GitリポジトリのURLだけでマーケットプレイスを構築できるようにし配布障壁を下げる

## 使いどころ

- チーム内でコードレビューやテストの標準を統一したいエンジニアリングリーダー
- OSSメンテナーがユーザー向けの定型操作をスラッシュコマンドとして提供したい場合
- 社内ツールをMCPサーバー経由でチーム全体に配布したい場合
