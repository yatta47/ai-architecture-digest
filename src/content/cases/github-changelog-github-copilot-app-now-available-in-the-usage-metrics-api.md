---
type: announcement
title: GitHub Copilotアプリの利用状況をUsage Metrics APIで可視化
title_original: GitHub Copilot app now available in the usage metrics API
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- GitHub Copilot
- Copilot usage metrics API
- GitHub Copilot app
outcome:
  type: cost
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-17-github-copilot-app-now-available-in-the-usage-metrics-api
published_at: '2026-07-17'
---

## 概要

GitHub CopilotのUsage Metrics APIが、エンタープライズ／組織の1日・28日レポートにCopilotアプリの利用状況を追加した。distinct active user数を示すdaily_active_copilot_app_usersと、セッション数・リクエスト数・プロンプト数・トークン使用量内訳を含む専用セクションtotals_by_copilot_appの2フィールドが新設され、これまで表れていなかったアプリの活動を既存のIDE/チャット/コードレビュー等の指標と同じAPIで取得できる。

## 設計のポイント

- アプリ固有の指標を汎用の集計（feature/model/language/LOC）に混ぜず、`totals_by_copilot_app` として独立セクションに分離する
- 活動が無い場合は両フィールドを null で返し、既存の連携インテグレーションを壊さず後方互換を保つ

## 使いどころ

- Copilotアプリの導入がどれだけ広がっているか（アクティブユーザー、セッション／リクエスト量、トークン消費）を把握したい、エンタープライズ／組織の管理者に効く
- 既存の利用メトリクス基盤に手を加えずに、Copilotアプリの利用状況を可視化したい場面で有効
