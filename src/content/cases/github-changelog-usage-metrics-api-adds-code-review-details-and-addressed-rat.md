---
type: announcement
title: Copilotコードレビューの対応率を測る利用メトリクスAPI
title_original: Usage metrics API adds code review details and addressed rate
company: GitHub
industry: cross-industry
cloud: []
patterns:
- eval
- llmops
components:
- GitHub Copilot
- GitHub Copilot code review
- Copilot usage metrics API
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-05-usage-metrics-api-adds-code-review-details-and-addressed-rate
published_at: '2026-11-06'
---

## 概要

GitHubのCopilot利用メトリクスAPIに、コードレビューコメントへの開発者の対応状況を示す項目が追加された。重大度、レビュー階層、コメント種別、カスタマイズ別の内訳で、リポジトリごとの対応率を追跡できる。

## 設計のポイント

- コメントがマージ時に評価され、提案適用以外の対応(自分で修正、後続PRで対応など)も対応済みとして数える。
- 重大度やコメント種別、カスタム指示/スキル/MCPの有無で内訳を取り、効果を比較できる。
- 人からの変更依頼なしでマージされたPR数も把握できる。

## 使いどころ

- Copilotコードレビューの導入効果を測る企業管理者。
- カスタム指示やMCP設定が効いているかを検証したいチーム。
