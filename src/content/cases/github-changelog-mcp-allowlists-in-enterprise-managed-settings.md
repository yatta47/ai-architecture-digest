---
type: announcement
title: GitHub、エンタープライズ管理設定でMCPサーバーの許可/拒否リストを提供
title_original: MCP allowlists in enterprise managed settings
company: GitHub
industry: cross-industry
cloud: []
patterns:
- guardrails
- policy-as-code
components:
- GitHub Copilot
- Model Context Protocol (MCP)
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-06-mcp-allowlists-in-enterprise-managed-settings
published_at: '2026-08-07'
---

## 概要

GitHubは、GitHub CopilotクライアントがどのMCP(Model Context Protocol)サーバーを実行できるかをエンタープライズ全体で一元管理できるallowedMcpServers/deniedMcpServers設定を正式提供した。リモートURL・ローカルコマンド・サーバー名でマッチングし、設定が不正または検証不能な場合は許可せずブロックする「フェイルクローズ」設計により、信頼できないMCPサーバーの実行を防ぐ。

## 設計のポイント

- リモート(HTTP/SSE)とローカル(stdio)の両方のMCPサーバーを、URL正規化やコマンド完全一致でマッチングし、回避策を防ぐ。
- 設定が不正・検証不能な場合は許可せずブロックするフェイルクローズ設計にし、ポリシーの誤設定が安全側に倒れるようにした。
- 複数レイヤーのポリシーがある場合は全レイヤーを通過する必要があるとし、企業ベースラインの上にチーム独自のオーバーライドを重ねられるようにした。

## 使いどころ

- AIコーディングエージェントが利用するツール・データソースを、エンタープライズ全体で統制したいセキュリティ管理者。
- 信頼できるMCPサーバーのみを許可し、未承認・非準拠のサーバーへの接続をブロックしたい組織。
