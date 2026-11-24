---
type: announcement
title: 'LlamaIndex: Workflows 1.0とLlamaParseネイティブMCPサーバー'
title_original: LlamaIndex Newsletter 2025-07-01
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- ai-agent
- unified-runtime
- llmops
components:
- LlamaParse
- Workflows
- MCP
- OpenTelemetry
- Claude
- Cursor
outcome:
  type: productivity
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/llamaindex-newsletter-2025-07-01
published_at: '2025-07-01'
---

## 概要

Workflows 1.0の独立提供とLlamaParseのネイティブMCPサーバー公開、OpenTelemetry連携を告知する週次ニュースレター。OAuth 2.1対応のMCPサーバーテンプレートも紹介。

## 設計のポイント

- パース機能をMCP経由で公開しClaudeやCursorから呼べるようにする
- OpenTelemetryのワンクリック連携でエージェントのトレースを可視化する
- OAuth 2.1対応のMCPサーバーテンプレートで自作サーバーを立てやすくする

## 使いどころ

- エージェントの処理をトレースして運用監視したい場面
- 社内データをMCPサーバー化してAIクライアントに接続したい場面
