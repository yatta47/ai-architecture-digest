---
type: guidance
title: Smartsheet MCPサーバーをAmazon QuickとKiroから使う構成
title_original: Work management context for AI agents with Smartsheet MCP on AWS
company: Smartsheet / AWS
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- context-engineering
components:
- Smartsheet MCP Server
- Amazon Quick
- Kiro
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/work-management-context-for-ai-agents-with-smartsheet-mcp-on-aws/
published_at: '2026-10-20'
---

## 概要

Smartsheetの40以上のツールを持つMCPサーバーを統合層とし、Amazon Quick(業務ユーザー)とKiro(開発者)をMCPクライアントとして接続する構成を紹介する。自然言語でシートの照会・更新ができる。

## 設計のポイント

- MCPサーバーを中央の統合層にし、複数クライアントから同じ業務データへ接続する。
- Kiroフックでコミット時にタスク状態を自動更新する。

## 使いどころ

- スプリント管理で担当者別の遅延タスクを即座に把握する場面。
- 開発者がIDEを離れず進捗を更新する場面。
