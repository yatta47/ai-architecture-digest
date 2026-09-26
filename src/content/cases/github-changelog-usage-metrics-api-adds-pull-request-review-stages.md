---
type: announcement
title: Copilot利用メトリクスAPIにPRレビュー段階別の所要時間を追加
title_original: Usage metrics API adds pull request review stages
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- GitHub Copilot
- Copilot usage metrics API
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-25-usage-metrics-api-adds-pull-request-review-stages
published_at: '2026-09-25'
---

## 概要

Copilot利用メトリクスのレポートに、PRのレビュー待ち・レビュー往復・承認後マージの各段階の中央値とp90が追加された。どこで時間が滞留しているかを切り分けられる。人間のレビューのみが集計対象である。

## 設計のポイント

- 待ち時間を3段階に分け、原因ごとに異なる改善策へつなげる。
- 中央値とp90を併記し、少数の遅いPRが全体を押し上げているかを判別する。

## 使いどころ

- Copilot導入後のレビュー工程のボトルネックを分析する開発組織。
- 開発生産性の指標をAPIで収集したいエンジニアリング管理者。
