---
type: guidance
title: Remote MCPサーバーとConnectorsでエージェントに外部サービス操作権限を付与
title_original: Remote MCP
industry: cross-industry
cloud: []
patterns:
- ai-agent
- mcp-integration
components:
- Responses API
- MCP
- Connectors
- Secure MCP Tunnel
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/tools-remote-mcp
published_at: '2025-07-22'
---

## 概要

Responses APIのmcp組み込みツールを使うと、Google WorkspaceやDropboxなどOpenAI管理のConnectorsや、任意の公開MCPサーバーに接続してモデルに新しい能力を付与できる。ツール呼び出しは自動承認または明示的な承認制御を選べ、社内・オンプレのMCPサーバーはSecure MCP Tunnelで公開せずに接続できる。

## 設計のポイント

- ConnectorsとRemote MCPサーバーはいずれも同じmcpツールタイプで扱え、server_urlとOAuthトークンを渡すだけで接続できる。
- 機密操作を伴うツール呼び出しは自動承認ではなく開発者側の明示的承認フローを挟める設計になっている。
- 非公開MCPサーバーはSecure MCP Tunnelを使ってファイアウォール内から公開せずに安全に接続する。

## 使いどころ

- 既存の社内SaaSやオンプレシステムをエージェントの追加ツールとして安全に接続したい場合。
- ChatGPTのConnectorsと同様の体験をAPI経由の自社エージェントにも実装したい場合。
