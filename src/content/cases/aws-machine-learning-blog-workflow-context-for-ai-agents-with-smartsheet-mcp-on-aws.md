---
type: guidance
title: Smartsheet MCPサーバーをAmazon QuickとKiroから使うワークフロー連携
title_original: Workflow context for AI agents with Smartsheet MCP on AWS
company: Smartsheet
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
components:
- Smartsheet MCP Server
- Amazon Quick
- Kiro
- MCP
outcome:
  type: productivity
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/workflow-context-for-ai-agents-with-smartsheet-mcp-on-aws/
published_at: '2026-10-20'
---

## 概要

Smartsheetの一般提供MCPサーバー(40超のツール)を介し、Amazon Quickのビジネス利用者とKiroの開発者が、自然言語でシートの更新や状況取得を行う構成を示す。MCPが中央の統合レイヤーとなる。

## 設計のポイント

- MCPサーバーを統合レイヤーとし、複数のMCPクライアントから同じツール群を使う。
- 非開発者向け(Quick)と開発者向け(Kiro)の経路を分ける。

## 使いどころ

- スプリントやプロジェクト管理をチャットで更新したいPM・運用チーム。
- 仕様参照とタスク更新を行き来せずに済ませたい開発者。
