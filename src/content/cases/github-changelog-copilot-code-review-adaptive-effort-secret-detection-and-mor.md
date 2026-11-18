---
type: announcement
title: Copilot code reviewのAdaptive労力・横断リポジトリ文脈・シークレット検出
title_original: 'Copilot code review: Adaptive effort, secret detection, and more'
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ai-agent
- context-engineering
- guardrails
components:
- GitHub Copilot code review
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-17-copilot-code-review-adaptive-effort-secret-detection-and-more
published_at: '2026-11-17'
---

## 概要

Copilotコードレビューは、PRの複雑さとリスクに応じてLite/Balanced/Maxを自動選択するAdaptiveを公開プレビューで導入した。関連リポジトリを文脈に使い、露出したシークレットも検出する。管理者の上限設定は超えない。

## 設計のポイント

- リスクに応じてレビュー深度を自動配分する。
- 組織・リポジトリ設定の最大労力を上限にする。
- 関連リポジトリを文脈に含める。

## 使いどころ

- レビューコストと品質を両立したい開発組織。
