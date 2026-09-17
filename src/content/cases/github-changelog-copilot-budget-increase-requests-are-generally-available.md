---
type: announcement
title: GitHub Copilotの追加予算リクエストフローが一般提供
title_original: Copilot budget increase requests are generally available
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
- cost-optimization
components:
- GitHub Copilot
outcome:
  type: cost
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-16-copilot-budget-increase-requests-are-generally-available
published_at: '2026-09-16'
---

## 概要

GitHub Copilotの利用でAIクレジット上限に達したメンバーが、その場で予算の追加リクエストを送れるフローがGA（一般提供）になった。組織/エンタープライズの管理者は設定画面から申請を確認し、金額を調整して承認するとメンバーのアクセスが即座に復旧する。GitHub Copilot BusinessおよびEnterpriseの従量課金プランで利用できる。

## 設計のポイント

- クレジット枯渇時にブロックするだけでなく、その場で追加予算をリクエストできる導線を用意し利用中断を最小化する
- 予算の支払い元アカウント（組織/エンタープライズ）に自動でリクエストをルーティングし、承認者が一元的に管理できるようにする
- 承認時に金額を調整可能にし、要求額をそのまま通すのではなく管理者が上限をコントロールできるようにする

## 使いどころ

- Copilotの従量課金AIクレジットを組織全体で管理している管理者・課金担当者
- 利用制限に達して作業が止まりがちな開発者の生産性を落とさずに予算統制を効かせたい組織
