---
type: announcement
title: Copilotのモデルポリシー管理REST APIが利用可能に
title_original: Copilot model policy API for enterprise, orgs, and teams
company: GitHub
industry: cross-industry
cloud: []
patterns:
- policy-as-code
- llm-gateway
components:
- GitHub Copilot
- GitHub REST API
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-19-copilot-model-policy-api-for-enterprise-orgs-and-teams
published_at: '2026-10-19'
---

## 概要

GitHub Copilotのモデルポリシーを取得・更新するGET/PATCH APIが、Enterprise・チーム・アプリ・Organizationの4階層で一般提供された。組織モードや企業チームモードで、下位階層へモデル制御を委任できる。

## 設計のポイント

- モデル利用可否を階層別のポリシーとしてAPIで管理し、コード化しやすくする。
- 上位ポリシーから組織やチーム、アプリへ制御を委任できる。

## 使いどころ

- 多数の組織を持つ企業が使えるモデルを一元管理する場面。
- モデル廃止や追加に合わせて設定を自動化したいプラットフォーム管理者。
