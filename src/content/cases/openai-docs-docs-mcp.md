---
type: guidance
title: OpenAI開発者ドキュメントを参照できるMCPサーバー
title_original: Docs MCP
company: OpenAI
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
- llm-gateway
components:
- Model Context Protocol (MCP)
- Codex
- VS Code
- GitHub Copilot
- Cursor
- Claude Code
outcome:
  type: productivity
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://developers.openai.com/learn/docs-mcp/
published_at: '2026-01-06'
---

## 概要

OpenAIはdevelopers.openai.com・platform.openai.com・learn.chatgpt.comのドキュメントを検索・参照できる読み取り専用のMCPサーバーをstreamable HTTPで公開した。Codex、VS Code（GitHub Copilot）、Cursor、Claude CodeといったAIコーディングエージェントから共通のURLで接続し、AGENTS.mdに利用指示を書くことでエージェントが自動的に公式ドキュメントを参照するようにできる。OpenAI Docs Skillと組み合わせることで、MCPで見つからない場合は公式ドメインへフォールバックし、回答の出典を追跡可能にする運用も推奨されている。

## 設計のポイント

- MCPサーバーは読み取り専用でOpenAI APIを一切呼び出さず、ドキュメントの検索とページ内容取得のみに機能を絞っている
- streamable HTTPで単一のエンドポイントを公開し、Codex/VS Code/Cursor/Claude Codeなど複数のエージェントツールから同じ設定で接続できるようにしている
- AGENTS.mdに利用ルールを明記し、ユーザーが毎回明示的に指示しなくてもエージェントが自動的にMCPを参照するよう誘導する
- OpenAI Docs Skillと併用し、MCPで解決しない質問は公式ドメインへフォールバックする2段構えの情報取得フローにする

## 使いどころ

- OpenAI APIやChatGPT Apps SDK、Codexを使う開発者が最新の公式ドキュメントをエージェントのコンテキストに取り込みたい場面
- Codex/Cursor/VS Code/Claude Codeなど複数のAIコーディングツールを横断して同じドキュメント参照ソースを使いたいチーム
- 回答に公式ドキュメントの出典を明示し、トレーサビリティを担保したい場合
