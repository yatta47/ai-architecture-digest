---
type: guidance
title: スキルとMCPを組み合わせてClaudeエージェントの業務ワークフローを実装する設計論
title_original: Extending Claude's capabilities with skills and MCP servers
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- MCP
- Claude
- Notion
- Salesforce
- S&P Capital IQ
- Daloopa
- Morningstar
- GitHub
- Slack
outcome:
  type: productivity
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers
published_at: '2025-12-19'
---

## 概要

MCP(Model Context Protocol)は外部システムへの接続性を提供し、スキルはその接続をチームの業務手順に沿って正しく使うための手順知識を提供するという役割分担を解説する。財務アナリストによる比較会社分析(S&P Capital IQやDaloopa、Morningstarへの接続とスキルによる手法適用・整形)や、Notion連携によるミーティング準備支援などの実例を通じて、MCPとスキルを組み合わせることで再現性の高いエージェントワークフローを構築できることを示す。

## 設計のポイント

- MCPはツールへの接続性を担い、スキルはどの情報源をどの順で参照しどう整形するかという業務ロジックを担う、という責務分離を徹底する
- スキル側でデータ参照の優先順位(発見手順)を明記することで、Claudeが情報源を推測せず一貫した手順で実行できるようにする
- MCPサーバー側の指示は『ツールの正しい使い方』に限定し、複数ツールをまたぐ業務手順やアウトプット形式の指定はスキル側に寄せて指示の衝突を避ける

## 使いどころ

- 財務アナリストが複数の市場データソースから比較会社分析を自動化し、コンプライアンス基準に沿った形式でアウトプットを作成する場面
- プロジェクトマネージャーがNotion連携でミーティング準備ドキュメントを一貫したフォーマットで自動生成する場面
- GitHubやSalesforceなど複数の外部システムをまたぐエージェントワークフローを、チーム固有の手順に沿って標準化したい場面
