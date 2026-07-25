---
type: announcement
title: OAuth統合とURLベースアップロードで再設計したLlamaParse MCPサーバー
title_original: 'LlamaParse MCP: Agentic OCR Tools for Your AI Agents'
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- document-processing
- guardrails
components:
- LlamaParse MCP
- WorkOS
- Redis
- OpenTelemetry
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaparse-mcp-the-tooling-layer-for-your-document-agents
published_at: '2026-07-18'
---

## 概要

LlamaParse Platform MCPをストレージ/検索中心からParse・Classify・Split主体のドキュメント処理へ再設計し、プラットフォーム共通のWorkOS OAuthによる認証、base64エンコードに代わるトークン発行式アップロードエンドポイント、OpenTelemetryトレーシングとレート制限を導入した。

## 設計のポイント

- MCPはファイルアップロードをネイティブサポートしないため、base64埋め込みではなく一時トークン付きアップロードURLを発行する方式に切り替え、トークン消費を削減する
- 既存プラットフォームと同じWorkOS OAuthに認証を統一し、別個のAPIキー管理をなくす
- 全ツール呼び出しをOpenTelemetryでトレースし、1分あたり100リクエストのスライディングウィンドウでレート制限する

## 使いどころ

- Claude DesktopやCursorなどMCP対応クライアントからドキュメント処理を呼び出したい開発者
- 本番運用に耐えるMCPサーバーの認証・可観測性設計を検討しているチーム
