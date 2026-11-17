---
type: announcement
title: Copilotのカスタマイズをプラグインと管理設定に限定する制御
title_original: Control where GitHub Copilot customizations come from
company: GitHub
industry: cross-industry
cloud: []
patterns:
- policy-as-code
- guardrails
components:
- GitHub Copilot
- Model Context Protocol
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-16-control-where-github-copilot-customizations-come-from
published_at: '2026-11-16'
---

## 概要

管理者は、スキル、カスタムエージェント、フック、MCPサーバー、拡張機能を、プラグインか管理設定経由に限定できる。マーケットプレイス制限と併用して承認済みツールだけを配布できる。

## 設計のポイント

- カテゴリ別に独立してプラグイン限定を適用する。
- マーケットプレイス許可リストと組み合わせて供給元を制限する。

## 使いどころ

- エージェント拡張の統制が必要な企業の管理者。
