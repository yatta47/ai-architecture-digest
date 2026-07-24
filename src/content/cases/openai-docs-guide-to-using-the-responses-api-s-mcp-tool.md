---
type: guidance
title: Responses APIのMCPツールで外部サービス連携を簡素化する
title_original: Guide to Using the Responses API's MCP Tool
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- Responses API
- MCP
- Stripe
- Shopify
- Sentry
- Twilio
outcome:
  type: speed
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/cookbook/examples/mcp/mcp_tool_guide/
published_at: '2025-05-21'
---

## 概要

Responses APIに統合されたホスト型MCPツールにより、個別の関数呼び出しラッパーを実装せずにモデルからMCPサーバーへ直接ツール呼び出しできるようになる。allowed_toolsによるツールの絞り込みやprevious_response_idを使ったツールリストのキャッシュなど、レイテンシとトークン消費を抑えるベストプラクティスを解説する。

## 設計のポイント

- MCPサーバーを一度設定するだけでツール定義をモデルに公開し、個別のfunction callingラッパー実装を不要にする
- allowed_toolsでサーバーが公開するツールを絞り込み、コンテキストへのトークン負荷とレイテンシを削減する
- mcp_list_toolsアイテムをコンテキストに保持することでツール一覧の再取得を避け、キャッシュのように機能させる

## 使いどころ

- ECサイトへのカート追加や決済リンク発行など、複数の外部SaaSを単一の会話ターンでまたぐ操作
- 既存のfunction calling実装をMCP経由に置き換え、バックエンドの中継実装を削減したい開発チーム
