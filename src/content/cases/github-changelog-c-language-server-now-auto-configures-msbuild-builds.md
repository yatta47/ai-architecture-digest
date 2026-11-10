---
type: announcement
title: GitHub Copilot CLIのC++言語サーバーがMSBuildを自動構成
title_original: C++ Language Server now auto-configures MSBuild builds
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
components:
- GitHub Copilot CLI
- Microsoft C++ Language Server
- MSBuild
outcome:
  type: speed
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-10-c-language-server-now-auto-configures-msbuild-builds
published_at: '2026-11-10'
---

## 概要

C++言語サーバーがMSBuildのコンパイルコマンド抽出器を同梱し自動で実行する。エージェントが設定スキルを探して実行する手間とトークン消費をなくし、決定論的に解析できる。

## 設計のポイント

- 環境構成を決定論的な処理に寄せてトークンを節約する。

## 使いどころ

- MSBuildのC++プロジェクトでCopilotを使う開発者
