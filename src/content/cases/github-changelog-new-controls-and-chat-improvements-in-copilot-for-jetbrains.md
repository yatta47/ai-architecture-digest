---
type: announcement
title: JetBrains向けCopilotのデフォルトモデル管理とMCP起動制御
title_original: New controls and chat improvements in Copilot for JetBrains
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- policy-as-code
components:
- GitHub Copilot
- JetBrains IDE
- MCP
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-10-new-controls-and-chat-improvements-in-copilot-for-jetbrains
published_at: '2026-10-10'
---

## 概要

GitHub Copilot for JetBrainsの更新。企業管理者が新規会話のデフォルトエージェントモデルを管理設定で指定でき、診断からのFixアクションやMCPサーバー自動起動の無効化設定が加わった。エージェントセッションやworktree周りの信頼性も改善された。

## 設計のポイント

- 管理設定でデフォルトモデルを組織が決めつつ、ユーザーのモデルピッカー選択は尊重する二層の制御にしている。
- 診断のFixアクションはエージェントモード優先、使えなければaskモードへフォールバックする。
- MCPサーバーの自動起動を無効化でき、ツールが有効になるタイミングをユーザーが制御できる。

## 使いどころ

- 組織でAIコーディング支援の初期モデルを統一したい管理者。
- MCPツールの有効化タイミングを厳密に管理したい開発チーム。
- IDE上の警告から修正提案までの手数を減らしたい開発者。
