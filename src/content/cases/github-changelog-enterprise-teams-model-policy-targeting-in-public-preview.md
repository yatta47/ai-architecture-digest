---
type: announcement
title: チーム単位でCopilotモデル利用権限を制御するエンタープライズチームポリシー
title_original: Enterprise teams model policy targeting in public preview
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- GitHub Copilot
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-31-enterprise-teams-model-policy-targeting-in-public-preview
published_at: '2026-07-31'
---

## 概要

GitHubはCopilot Business/Enterprise向けに、モデル利用ポリシーを組織全体ではなくエンタープライズチーム単位で細かく制御できる「Enterprise teams」機能をパブリックプレビューとして公開した。モデルをEnabled/Disabled/Optionalの3段階で設定し、Optionalモデルはチームごとに個別付与できる。

## 設計のポイント

- モデルアクセス評価は最も制限の緩い方の権限を採用する（いずれか1つのチームから付与されればどこでも利用可能）ため、権限設計はチーム構成に注意が必要
- プレビュー期間中はEnterprise teamsモードを有効化する前にチーム作成とモデル割り当てを準備でき、ロールバックも可能

## 使いどころ

- 職種や習熟度、先行実験チームなど役割単位でAIモデルへのアクセスを細かく管理したいAI管理者
