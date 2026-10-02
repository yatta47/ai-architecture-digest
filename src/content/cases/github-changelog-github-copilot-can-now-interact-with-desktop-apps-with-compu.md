---
type: announcement
title: GitHub CopilotのコンピュータユースがCLIとアプリでパブリックプレビュー
title_original: GitHub Copilot can now interact with desktop apps with computer use
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- GitHub Copilot CLI
- GitHub Copilot app
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-01-github-copilot-can-now-interact-with-desktop-apps
published_at: '2026-10-01'
---

## 概要

GitHub Copilot CLIとCopilotアプリ（macOS/Windows）でコンピュータユースがパブリックプレビューとなり、Copilotがデスクトップアプリをクリックや入力で操作できるようになった。APIやCLI、MCP連携を持たないレガシー/GUI専用ソフトのワークフローも自動化対象になる。

## 設計のポイント

- アプリ操作の前にユーザー承認を求め、常時許可したアプリの確認やリセットも可能にする。
- 組織管理の設定で機能を無効化でき、macOSではアクセシビリティ等の権限取得を案内する。
- API/CLI/MCPが無い対象をGUI操作で補うことで、エージェントの自動化範囲を広げる。

## 使いどころ

- APIを持たない社内のレガシーGUIアプリを使う業務を自動化したい場面に効く。
- 経費精算のような複数アプリをまたぐ定型作業をエージェントに任せたい開発者に向く。
