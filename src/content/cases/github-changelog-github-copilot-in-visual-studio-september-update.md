---
type: announcement
title: 'Visual Studio向けCopilot 9月更新: Git agent・BYOM・NuGet脆弱性修正'
title_original: GitHub Copilot in Visual Studio — September update
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- GitHub Copilot
- Visual Studio 2026
- MCP
- Git agent
- NuGet MCP server
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-22-github-copilot-in-visual-studio-september-update-2
published_at: '2026-10-23'
---

## 概要

Visual Studio 2026のCopilotで、Git agentによるPR探索、独自モデル持ち込み(BYOM)、NuGet脆弱性をエラー一覧から修正する機能が加わった。BYOMは新しいAgent(Preview)が必要となる破壊的変更を含む。

## 設計のポイント

- Git providerのMCPサーバー経由でPRを文脈として取り込む。
- BYOMにより、Foundry・OpenAI・Anthropic・Ollamaなどのモデルを切り替えて使える。
- 脆弱性警告からエージェントモードの修正フローへ直接つなぐ。

## 使いどころ

- IDE内でPRレビューや依存関係の修正を済ませたい.NET開発者。
- チーム指定のモデルでコーディング支援を使いたい組織。
