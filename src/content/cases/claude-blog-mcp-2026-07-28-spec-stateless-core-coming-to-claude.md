---
type: announcement
title: MCPがステートレスコアに移行しClaudeのエージェント連携を強化
title_original: Bringing MCP 2026-07-28 to Claude
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- Model Context Protocol (MCP)
- Claude
outcome:
  type: reliability
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/bringing-mcp-2026-07-28-to-claude
published_at: '2026-07-28'
---

## 概要

Model Context Protocolの最新仕様MCP 2026-07-28は双方向ステートフルなプロトコルからリクエスト/レスポンス型のステートレスコアへ移行し、サーバーレスやエッジへのデプロイを可能にした。あわせてMCP Apps/Tasksの拡張フレームワーク標準化と、エンタープライズIDプロバイダに対応した認可の強化が行われ、ClaudeやFigma、Intuit、Zoom等のエコシステムで採用が進んでいる。

## 設計のポイント

- プロトコルコアをステートレス化することでセッション管理を不要にし、サーバーレス/エッジでのスケールを可能にする
- インタラクティブUIや長時間実行タスクをコアプロトコルを変えずにバージョン管理された拡張（MCP Apps/Tasks）として追加する
- 認可をOAuth 2.0/OIDCの本番運用パターンに合わせ、Entra/Okta等の既存IDプロバイダとゼロタッチで統合できるようにする

## 使いどころ

- MCPサーバーを自社のエンタープライズID基盤経由で全社展開したいプラットフォーム管理者
- 既存のHTTPインフラ・サーバーレス基盤にMCPサーバーをシンプルにデプロイしたい開発者
