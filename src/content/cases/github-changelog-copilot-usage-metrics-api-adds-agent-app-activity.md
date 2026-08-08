---
type: announcement
title: GitHub Copilot利用状況APIがエージェントアプリ別の活動指標に対応
title_original: Copilot usage metrics API adds agent app activity
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- Copilot usage metrics API
- Claude
- Codex
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-07-copilot-usage-metrics-api-adds-agent-app-activity
published_at: '2026-08-07'
---

## 概要

GitHub Copilot usage metrics APIに、ClaudeやCodexなどパートナー製エージェントアプリごとの利用状況を集計するtotals_by_3rd_party_agentフィールドが追加された。これまで単一バケットだったエージェント活動が個別に把握できるようになり、複数エージェント導入時の比較やロールアウト・ライセンス判断を実データに基づいて行えるようになる。

## 設計のポイント

- agent_idを安定キーとしてエージェントを識別し、表示名(agent_name)の変更に影響されない集計を可能にした。
- セッション数はエンタープライズ・組織単位の集計レポートのみに含め、個人単位のレポートからは除外してプライバシーに配慮している。
- 既存フィールドの形状を変えず、該当データが無い期間はフィールド自体を省略することで後方互換性を保っている。

## 使いどころ

- 複数のAIコーディングエージェントを併用しており、エージェントごとの採用状況を比較したい管理者。
- 新規導入したエージェントが既存エージェントをどれだけ代替できているかを実利用データで検証したい場合。
