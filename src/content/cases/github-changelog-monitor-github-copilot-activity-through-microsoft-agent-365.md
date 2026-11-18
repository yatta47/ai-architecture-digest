---
type: announcement
title: Copilotのエージェント活動をMicrosoft Agent 365へストリーミング
title_original: Monitor GitHub Copilot activity through Microsoft Agent 365
company: GitHub
industry: cross-industry
cloud:
- azure
patterns:
- guardrails
- defense-in-depth
components:
- GitHub Copilot
- Microsoft Agent 365
- Microsoft Purview
- Microsoft Defender
outcome:
  type: risk-compliance
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-17-monitor-github-copilot-activity-through-microsoft-agent-365
published_at: '2026-11-17'
---

## 概要

GitHub Enterprise CloudのEnterprise Managed Usersの顧客は、Copilotの監査ログをMicrosoft Agent 365へ流せる。プロンプト、応答、ツール呼び出しやクライアント別の活動を確認でき、PurviewやDefenderでリスク調査も行える。

## 設計のポイント

- 複数クライアントの監査データを単一のエージェント統制基盤に集約する。
- 既存のセキュリティ製品でリスクを調査する。

## 使いどころ

- AIエージェントの利用を監査・統制したい企業のセキュリティ部門。
