---
type: announcement
title: GitHub MCP Serverが次期MCP仕様(ステートレス化)に対応
title_original: GitHub MCP Server supports the next MCP specification
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- ai-agent
components:
- GitHub MCP Server
- MCP
- VS Code
- GitHub Copilot
outcome:
  type: speed
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-23-github-mcp-server-supports-the-next-mcp-specification
published_at: '2026-07-23'
---

## 概要

2026年7月28日に正式リリースされるステートレス版MCP仕様に、GitHub MCP Serverが先行対応した。セッション管理と初期化ハンドシェイクの廃止により初期化ごとのDB書き込みが不要になり、複数往復リクエストによるelicitationなど新機能も利用しやすくなる。

## 設計のポイント

- セッション状態(Redis)を廃止し、初期化時のDB書き込みと毎呼び出しのDB読み取りをなくすことでレイテンシを削減する
- ロギングやシークレットスキャン用の値をペイロード深部までのディープパケットインスペクションではなく、必ず存在するHTTPヘッダーから取得するよう変更する
- stdioサーバーのURL elicitationと新方式のマルチラウンドトリップelicitationの両方を同一SDKラッパーで吸収し後方互換性を保つ

## 使いどころ

- 多数のクライアントを相手にMCPサーバーをスケールさせる必要があるプラットフォームチーム
- 適合性テストスイートを使ってエージェント実装やMCPサーバーの検証を自動化したい開発者
