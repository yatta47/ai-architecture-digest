---
type: case
title: Unisys ClearPath MCPメインフレームをAzure仮想マシンへリフト移行するアーキテクチャ
title_original: Unisys ClearPath MCP virtualization on Azure
ai_relevant: false
company: Unisys
industry: cross-industry
cloud:
- azure
- on-prem
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/unisys-clearpath-forward-mainframe-rehost
published_at: '2026-07-01'
---

## 概要

UnisysのClearPath Forward(CPF) Libra(MCP)メインフレームを、アプリケーションコードやデータベース構造を書き換えることなくAzure仮想マシンへリフト移行する仮想化アーキテクチャ。MCP OSや画面・データ構造をそのまま維持することでユーザー再教育コストを避け、テープ資産のAzure Storageへの移行やAzure Site Recoveryによるディザスタリカバリを組み合わせて、ハードウェア保守費用の削減と迅速なROI実現を狙う。
