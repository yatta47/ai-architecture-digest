---
type: announcement
title: GitHub Copilotのモデルアクセスを課金組織単位に統一
title_original: Copilot model access update for GitHub Team plans
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llm-gateway
components:
- GitHub Copilot
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-31-copilot-model-access-update-for-github-team-plans
published_at: '2026-08-31'
---

## 概要

複数組織でCopilotシートを持つユーザーのモデルアクセス判定を、これまでの『いずれかの組織が有効化していれば使える』方式から、利用料金を支払う組織（課金組織）のポリシーのみで決定する方式に変更した。ガバナンスと課金の整合性を取ることが狙い。

## 設計のポイント

- モデルアクセスの可否判定を、シートを持つ複数組織のうち利用料金を支払う課金組織のポリシーに一本化する
- エンタープライズ配下のみでアクセスする場合はこの変更の影響を受けない

## 使いどころ

- 複数組織にまたがってCopilotシートを持つ開発者のモデルガバナンスを統一したい情報システム部門
- 組織横断のAIツール利用ポリシーを整理したいセキュリティ/コンプライアンス担当
