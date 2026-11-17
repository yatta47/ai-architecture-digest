---
type: announcement
title: GitHub Copilotの旧モデル廃止と代替モデル
title_original: GitHub Copilot models deprecated on November 16, 2026
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
components:
- GitHub Copilot
outcome:
  type: reliability
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-16-github-copilot-models-deprecated-on-november-16-2026
published_at: '2026-11-16'
---

## 概要

2026年11月16日に、Copilotの複数モデルが主要機能で廃止された。管理者の設定がなければ代替モデルが自動で有効化される。モデル管理の運用上の注意を伝える告知である。

## 設計のポイント

- 代替モデルを既定で自動有効化しつつ、管理者のポリシーで制御できるようにする。

## 使いどころ

- Copilot上のモデル構成を管理する管理者。
