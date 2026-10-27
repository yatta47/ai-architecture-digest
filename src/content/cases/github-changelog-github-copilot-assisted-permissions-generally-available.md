---
type: announcement
title: GitHub Copilotのassisted permissionsが一般提供
title_original: GitHub Copilot assisted permissions generally available
company: GitHub
industry: cross-industry
cloud: []
patterns:
- guardrails
- human-in-the-loop
components:
- GitHub Copilot CLI
- GitHub Copilot app
- Visual Studio Code
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-26-github-copilot-assisted-permissions-generally-available
published_at: '2026-10-26'
---

## 概要

Copilotがコマンド実行やファイルアクセス、URL参照の許可を求めると、LLMが要求を評価して明らかに安全なものは自動で通し、それ以外は承認を求める。管理者はAllow Allを禁止して既定モードも設定できる。

## 設計のポイント

- LLM分類で安全な操作を自動承認し、承認疲れを減らす。
- 企業管理設定で許可モードを制限し、不許可なら手動承認から始める。

## 使いどころ

- エージェントの承認ダイアログが多すぎる開発者。
- 組織で権限ポリシーを統制したい管理者。
