---
type: announcement
title: Copilot利用メトリクスAPIにカスタムのスキル・エージェント・MCPサーバー名を表示
title_original: Custom skills, agents, and MCP servers in usage metrics API
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
components:
- GitHub Copilot
- Copilot CLI
- Copilot SDK
- MCP
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-22-custom-skills-agents-and-mcp-servers-in-usage-metrics-api
published_at: '2026-10-22'
---

## 概要

Copilotの利用メトリクスが、組織が作成したスキル、カスタムエージェント、MCPサーバー、スラッシュコマンド、プラグインを、other/customでなく名称付きで報告するようになった。上位25件まで表示でき、導入後の定着や実際の利用状況を管理者が把握できる。

## 設計のポイント

- クライアントテレメトリ由来のため過少計測があり、傾向把握に使う前提にしている。
- エントリ上限を5件から25件に増やし、ロングテールを見える化している。

## 使いどころ

- 社内で作ったスキルやMCPサーバーの定着を追う管理者。
- エージェント拡張の展開後に研修の重点箇所を判断したい場合。
