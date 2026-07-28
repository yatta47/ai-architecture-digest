---
type: announcement
title: GitHub Copilotアプリのアクセスを専用ポリシーで統制
title_original: Manage GitHub Copilot app access with a dedicated policy
company: GitHub
industry: cross-industry
cloud: []
patterns:
- policy-as-code
- llmops
components:
- GitHub Copilot app
- GitHub Copilot CLI
- GitHub Copilot
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-27-manage-github-copilot-app-access-with-a-dedicated-policy
published_at: '2026-07-27'
---

## 概要

GitHub Copilotアプリが、これまでCopilot CLIのポリシーに依存していたアクセス制御から独立し、エンタープライズ・組織単位で個別に有効/無効を設定できる専用ポリシーを持つようになった。既存のエンタープライズ管理設定ガードレールもCopilotアプリに一貫して適用される。

## 設計のポイント

- クライアントごとに独立したポリシーを持たせることで、組織が導入するAIツールをクライアント単位で細かく制御できるようにする

## 使いどころ

- 複数のCopilotクライアント（CLI・アプリ・IDE）を組織全体で統制したいIT管理者
