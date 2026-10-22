---
type: announcement
title: Copilotインパクトダッシュボードに業界比較セクションが追加
title_original: Industry comparisons in the Copilot impact dashboard
company: GitHub
industry: cross-industry
cloud: []
patterns: []
components:
- GitHub Copilot
- Copilot impact dashboard
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-22-industry-comparisons-in-the-copilot-impact-dashboard
published_at: '2026-10-22'
---

## 概要

GitHubのCopilotインパクトダッシュボードに、同業・同規模の参加企業との比較セクションが加わった。エージェント型利用の採用率とマージ率を、ピアの中央値や上位10%と比べられる。参加はオプトインで既定は無効である。

## 設計のポイント

- 比較への参加はオプトインとし、有効化と解除は同一ポリシーで管理する。
- 集計値は識別情報を含まず30日で削除し、データ所在地設定の環境では同一リージョン内でのみ比較する。

## 使いどころ

- Copilot導入の進み具合を同業他社と比べ、目標設定や課題把握をしたい経営層や管理者。
