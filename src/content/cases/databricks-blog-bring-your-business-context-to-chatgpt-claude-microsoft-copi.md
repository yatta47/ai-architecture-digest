---
type: announcement
title: ChatGPT・ClaudeなどからGenieの業務文脈を使うプラグイン
title_original: Bring your business context to ChatGPT, Claude, Microsoft Copilot Cowork, and Grok Bot
company: Databricks
industry: cross-industry
cloud: []
patterns:
- context-engineering
- ai-agent
- text-to-sql
components:
- Databricks Genie
- Genie Ontology
- MCP
- ChatGPT
- Claude
- Microsoft Copilot Cowork
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/bring-your-business-context-chatgpt-claude-microsoft-copilot-cowork-and-grok-bot
published_at: '2026-11-11'
---

## 概要

Genieプラグインにより、ChatGPT、Claude、Copilot Cowork、Grok Botから、Genie Ontologyの認定済み定義を使った回答を取得できる。プラグイン未対応のエージェントはMCPサーバー経由で利用でき、GenieがSQLを実行して引用付きで返す。

## 設計のポイント

- 外部エージェントが手探りで検索せず、先に業務の地図（Ontology）を参照させる。
- 専門的な質問は分野別のGenie Agentへ振り分ける。
- 権限のあるデータだけに対してSQLを実行する。

## 使いどころ

- 複数のエージェント製品を併用しつつ業務定義を一元化したい企業。
- 他エージェントから社内データへの質問を任せたい場面。
