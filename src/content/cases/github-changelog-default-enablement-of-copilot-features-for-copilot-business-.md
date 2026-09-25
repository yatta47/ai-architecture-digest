---
type: announcement
title: Copilot機能のデフォルト有効化ポリシー
title_original: Default enablement of Copilot features for Copilot Business and Enterprise
company: GitHub
industry: cross-industry
cloud: []
patterns:
- policy-as-code
- human-in-the-loop
components:
- GitHub Copilot
- MCP
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-24-default-enablement-of-copilot-features-for-copilot-business-and-enterprise
published_at: '2026-09-25'
---

## 概要

GitHubがCopilot BusinessとEnterprise向けに、GA機能の既定を有効・無効・組織委任から選ぶグローバルポリシーを導入した。10月22日に発効し、明示設定は維持され、プレビュー機能はオプトインのままとなる。

## 設計のポイント

- 未設定の機能だけに既定ポリシーを適用し、明示的な判断は上書きしない。
- 無効を選んだ場合、新機能は管理者承認を必須にする。
- 発効前に28日の猶予期間を置いて設定と影響を確認できる。

## 使いどころ

- AI機能の統制を企業単位で一元管理したい管理者。
- 新機能の自動展開を承認制に切り替えたい組織。
