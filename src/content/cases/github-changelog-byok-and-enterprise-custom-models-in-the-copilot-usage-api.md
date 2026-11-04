---
type: announcement
title: Copilot利用メトリクスAPIにBYOK利用を追加
title_original: BYOK and enterprise custom models in the Copilot usage API
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
- cost-optimization
components:
- GitHub Copilot
- Copilot usage metrics API
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-03-byok-and-enterprise-custom-models-in-the-copilot-usage-api
published_at: '2026-11-04'
---

## 概要

GitHub Copilotの利用メトリクスAPIで、開発者のローカルBYOKと管理者設定の企業カスタムモデルの利用を、Copilotホスト型モデルと分けて取得できるようになった。ガバナンス確認とコスト把握に使える。

## 設計のポイント

- ローカルBYOKとカスタムモデルを別フィールドで集計し、既存の合計は変えない。
- ユーザー・集計単位、1日・28日レポートで取得できる。

## 使いどころ

- BYOKポリシーの遵守状況を監査したいとき。
- ホスト型と自前プロバイダの支出を分けて把握したいとき。
