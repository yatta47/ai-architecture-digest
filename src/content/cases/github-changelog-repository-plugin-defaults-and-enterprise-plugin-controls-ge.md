---
type: announcement
title: Copilotのリポジトリ既定プラグインと企業管理プラグイン制御の一般提供
title_original: Repository plugin defaults and enterprise-managed plugin controls generally available
company: GitHub
industry: cross-industry
cloud: []
patterns:
- policy-as-code
- guardrails
components:
- GitHub Copilot
- VS Code
- Copilot CLI
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-28-repository-plugin-defaults-and-enterprise-plugin-controls-generally-available
published_at: '2026-10-28'
---

## 概要

GitHub Copilotでリポジトリ単位の既定プラグインと、企業管理者によるプラグインの必須化・ブロック・承認済みマーケットプレイス制限が一般提供となった。管理設定がリポジトリや個人の選択より優先され、必須プラグインは自動インストールされ利用者は無効化できない。

## 設計のポイント

- 管理設定をリポジトリ設定・個人設定より優先する階層構造でポリシーを強制する。
- リポジトリ側で既定プラグインを定義し、コントリビューターの初期設定の手間を省く。
- 承認済みマーケットプレイスに限定してプラグインの供給元を統制する。

## 使いどころ

- Copilotを全社展開し拡張機能のガバナンスを一元化したい企業の管理者。
- チーム共通の開発環境をリポジトリで配布したいメンテナ。
