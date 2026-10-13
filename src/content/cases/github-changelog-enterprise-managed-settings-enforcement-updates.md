---
type: announcement
title: Copilotのマネージド設定で起動時に最新ポリシー取得を強制
title_original: Enterprise managed settings enforcement updates
company: GitHub
industry: cross-industry
cloud: []
patterns:
- policy-as-code
- guardrails
components:
- GitHub Copilot
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-13-enterprise-managed-settings-enforcement-updates
published_at: '2026-10-13'
---

## 概要

forceRemoteSettingsRefreshによりCopilotクライアントは起動時に最新のポリシー取得を必須にでき、確認できなければfail closedとなる。sandboxキーには最小クライアントバージョンの強制も加わった。

## 設計のポイント

- ポリシー確認不能時はキャッシュで動かさずfail closedにする。
- キャッシュによる起動速度と遅延許容を、設定でトレードオフ選択できる。

## 使いどころ

- Copilotのガバナンスを厳格化したい企業管理者。
