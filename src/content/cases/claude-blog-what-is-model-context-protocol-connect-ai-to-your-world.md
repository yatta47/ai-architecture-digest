---
type: guidance
title: LLMと外部ツールをつなぐ標準プロトコルMCP
title_original: What is Model Context Protocol? Connect AI to your world
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- mcp
- ai-agent
components:
- Model Context Protocol
- Claude
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/what-is-model-context-protocol
published_at: '2025-10-31'
---

## 概要

LLMと外部アプリケーション・データソースを接続するための標準プロトコルMCP（Model Context Protocol）の全体像を解説。クライアント/サーバー型のアーキテクチャにより、個別統合が組み合わせ爆発するM×N問題を1つの標準に集約する狙いを説明している。

## 設計のポイント

- USB-Cのような単一の接続規格でLLMと外部ツールを疎結合に接続する
- MCPクライアントとMCPサーバーの二面構成にすることで統合の組み合わせ爆発（M×N問題）を回避する
- 既存のLanguage Server Protocolの設計を参考にオープン標準として設計する

## 使いどころ

- 複数のSaaSやデータソースにAIエージェントを接続したい開発者
- 社内システムへの安全でスケーラブルなAI接続を必要とする企業
- カスタム統合を作らずにAIアシスタントから業務ツールを操作したい利用者
