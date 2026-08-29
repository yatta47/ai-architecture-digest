---
type: announcement
title: GitHub Copilot週次リリースまとめ(Slack/Teams共有セッション・CLIのRust化ほか)
title_original: GitHub Copilot weekly releases — August 24
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- human-in-the-loop
components:
- GitHub Copilot
- GitHub Copilot CLI
- GitHub Copilot app
- VS Code
- GitHub Copilot for JetBrains
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-28-github-copilot-weekly-releases-august-24
published_at: '2026-08-28'
---

## 概要

GitHub Copilotの週次アップデートとして、SlackやMicrosoft Teams上のチームでの会話をそのまま共有エージェントセッションに変換できる機能、Copilot appのCustomizeタブ一般提供(MCPサーバー・プラグイン・スキル・キャンバスの統合管理)、Copilot CLIのネイティブRustランタイム移行による高速化、VS Code 1.135での複数モデルによるセカンドオピニオン機能などがまとめて公開された。JetBrains向けにもプラグイン・MCP・権限モードのエンタープライズ統制が拡張されている。

## 設計のポイント

- チームのチャット(Slack/Teams)上の会話をそのまま共有エージェントセッションとして扱い、調査・計画・変更の過程をチームで追跡・誘導できるようにする
- MCPサーバー・プラグイン・スキルなど拡張機構を単一のCustomizeタブに集約し、設定の発見性と一貫性を高める
- CLI本体をRustランタイムに置き換えつつターミナルUIはTypeScriptのまま保つことで、体験を変えずに実行速度を改善する

## 使いどころ

- チームでのインシデント調査や計画策定をチャット上のエージェントセッションとして進めたい開発チーム
- IDE・CLI・JetBrains等マルチクライアントでCopilotの権限やMCP構成を統一管理したいエンタープライズ管理者
