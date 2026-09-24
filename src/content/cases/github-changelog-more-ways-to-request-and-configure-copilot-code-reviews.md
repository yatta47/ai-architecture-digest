---
type: announcement
title: Copilotコードレビューの個人設定とエンタープライズ既定の強化
title_original: More ways to request and configure Copilot code reviews
company: GitHub
industry: cross-industry
cloud: []
patterns:
- human-in-the-loop
- policy-as-code
components:
- GitHub Copilot code review
- Copilot Business
- Copilot Enterprise
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-23-copilot-code-review-more-ways-to-request-and-configure-reviews
published_at: '2026-09-23'
---

## 概要

GitHub Copilotのコードレビューに、全プランで使える専用の個人設定ページと、エンタープライズ全体の既定レビュー強度の設定が一般提供された。自動レビューの契機（PR作成、ドラフト解除、新規push、ドラフトPR）を個別に選べ、レビュー強度はLiteかBalancedから選ぶ。

## 設計のポイント

- 自動レビューの契機をPR作成、ドラフト解除、pushなどに分けて個人が選べるようにする。
- レビュー強度（Lite/Balanced）の既定値を個人に持たせ、手動リクエスト時は都度上書きできる。
- 企業管理者が設定した既定を組織・リポジトリへ継承し、下位での上書きも許す階層設計にする。

## 使いどころ

- チームごとにレビューの深さとコストのバランスを揃えたいエンタープライズ管理者。
- ドラフトPRやpushごとのレビュー頻度を自分で調整したい開発者。
- Copilot BusinessやEnterpriseでAIレビューを段階導入する組織。
