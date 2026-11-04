---
type: announcement
title: DependabotがAgent Package Managerの更新に対応
title_original: Dependabot version updates support Agent Package Manager
company: GitHub
industry: cross-industry
cloud: []
patterns:
- ci-cd
- policy-as-code
components:
- Dependabot
- Agent Package Manager (APM)
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-03-dependabot-version-updates-support-agent-package-manager
published_at: '2026-11-03'
---

## 概要

Dependabotのバージョン更新がAPMに対応し、apm.ymlのgit依存を更新するPRを作成し、apm.lock.yamlも再生成する。エージェントのスキル、プロンプト、指示を最新に保てる。セキュリティ更新は対象外。

## 設計のポイント

- apm.ymlの依存をdependabot.ymlで宣言して更新スケジュールを管理する。
- ロックファイルを再生成して再現性を保つ。

## 使いどころ

- エージェントのスキルやプロンプトをパッケージ管理しているチーム。
