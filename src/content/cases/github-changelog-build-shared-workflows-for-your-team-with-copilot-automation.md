---
type: announcement
title: チームで共有できるCopilot Automations
title_original: Build shared workflows for your team with Copilot Automations
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- event-driven
- policy-as-code
components:
- GitHub Copilot Automations
- GitHub Copilot cloud agent
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-28-build-shared-workflows-for-your-team-with-copilot-automations
published_at: '2026-10-28'
---

## 概要

共有Copilot Automationsにより、プロンプト・トリガー・ツールを組み合わせたAIワークフローをチームで作成・保守できる。実行主体はCopilotで、課金はリポジトリ所有者に付く。

## 設計のポイント

- オートメーションをリポジトリに帰属させ、作成者が離れても動き続けるようにする。
- アクションをCopilotとして記録し、AIクレジットをリポジトリ所有者に課金する。
- 許可したツールのみで動かし、変更履歴をチームで追えるようにする。

## 使いどころ

- Issue作成時のバグ再現やPRのスクリーンショット取得を自動化したいチーム。
- 監視ツールの障害検知から調査を自動開始したい運用チーム。
