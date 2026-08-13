---
type: announcement
title: Agent Plugins 1.0——1つのプラグインをVS Code/Copilot CLI/アプリ間で共有する標準仕様
title_original: Agent Plugins 1.0 in VS Code, Copilot CLI, and the Copilot app
company: GitHub
industry: cross-industry
cloud: []
patterns:
- unified-runtime
- policy-as-code
components:
- GitHub Copilot
- VS Code
- Copilot CLI
- MCP
- Agent Plugins
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-12-agent-plugins-1-0-in-vs-code-copilot-cli-and-the-copilot-app
published_at: '2026-08-12'
---

## 概要

AWS・Anysphere・Microsoft・OpenAI・Vercel・GoogleがAgent Plugins 1.0を策定し、エージェントのskillとMCPサーバーを一つのプラグインパッケージとしてVS Code・Copilot CLI・Copilotアプリ間で共有できるようにしたことを発表。マニフェストにスキーマを追加するだけで既存プラグインを移行でき、企業は既存の管理設定でプラグイン利用を統制できる。

## 設計のポイント

- skillとMCPサーバー設定を標準化し、クライアント固有機能は名前空間付きディレクトリに隔離することでベンダー間の移植性を保つ
- 既存のCopilotプラグインは移行不要のまま動作を維持し、新仕様への対応は段階的に行える
- enabledPluginsやstrictKnownMarketplacesなど既存の管理設定をAgent Plugins 1.0にもそのまま適用できるようにする

## 使いどころ

- 複数のエージェントクライアント向けに同じプラグインを別々にメンテナンスしていた開発者
- 組織内で利用可能なプラグイン/マーケットプレイスを一元的に統制したいCopilot管理者
