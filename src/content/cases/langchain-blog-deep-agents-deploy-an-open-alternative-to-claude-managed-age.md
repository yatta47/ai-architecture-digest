---
type: announcement
title: 'Deep Agents deploy: モデル非依存のエージェントを1コマンドで本番化'
title_original: 'Deep Agents Deploy: an open alternative to Claude Managed Agents'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- unified-runtime
- human-in-the-loop
components:
- Deep Agents
- LangSmith Deployment
- MCP
- A2A
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/deep-agents-deploy-an-open-alternative-to-claude-managed-agents
published_at: '2026-10-13'
---

## 概要

deepagents deployはモデル非依存のエージェントを、マルチテナントなサーバー、サンドボックス、MCP/A2A/Human-in-the-loop/メモリ用エンドポイント込みで1コマンドで本番化する。オープンなハーネスによりメモリの所有権を保てると主張する。

## 設計のポイント

- モデル、AGENTS.md、skills、mcp.json、サンドボックスの宣言でエージェントを定義する。
- MCPやA2Aなど30以上のエンドポイントを標準提供する。
- ハーネスをオープンにしてメモリのロックインを避ける。

## 使いどころ

- エージェントの本番化基盤を自前で作りたくないチーム。
