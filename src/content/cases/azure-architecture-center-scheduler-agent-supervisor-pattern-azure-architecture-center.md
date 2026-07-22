---
type: guidance
title: Scheduler・Agent・Supervisorで分散タスクの失敗を検知し復旧するパターン
title_original: Scheduler Agent Supervisor pattern
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/scheduler-agent-supervisor
published_at: '2026-03-31'
---

## 概要

複数ステップからなる分散タスクをSchedulerが順序立てて実行し、リモートサービス呼び出しはAgentに委譲し、Supervisorが状態ストアを定期的に監視して失敗・タイムアウトを検知する設計パターン。一時的な障害はリトライで吸収し、恒久的な障害はSupervisorがAgentに復旧・是正アクションを指示することで、システム全体を一貫した状態に保つ。Scheduler/Agent/Supervisorは論理的な役割であり、複数インスタンスが並行稼働する場合はLeader Electionパターンで調停する。
