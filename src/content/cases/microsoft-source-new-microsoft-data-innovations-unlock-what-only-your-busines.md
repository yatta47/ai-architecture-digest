---
type: announcement
title: Fabric IQによるCopilotへの業務文脈の接続とデータ基盤の新機能
title_original: New Microsoft data innovations unlock what only your business knows
company: Microsoft
industry: cross-industry
cloud:
- azure
patterns:
- context-engineering
- ai-agent
- data-federation
- policy-as-code
components:
- Microsoft Fabric
- Fabric IQ
- Microsoft Copilot
- Power BI
- OneLake
- Azure Databases
- SQL Server on Azure Local
outcome:
  type: quality
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://blogs.microsoft.com/blog/2026/09/28/new-microsoft-data-innovations-unlock-what-only-your-business-knows/
published_at: '2026-09-29'
---

## 概要

Microsoftは欧州のFabricとSQLのカンファレンスで、Fabric IQをCopilotに接続する機能の一般提供や、組織間でデータと文脈を共有するIQ Sharingのプレビューなどを発表した。ガバナンス済みのセマンティックモデルにAIの回答を根拠づける方針を、Observability、Fabric Apps、エージェント型データエンジニアリングとともに打ち出している。

## 設計のポイント

- CopilotをPower BIのセマンティックモデルに接続し、部門間で指標の定義を統一して答えを根拠づける。
- 既存のアクセス制御とガバナンスを保ったまま、データと業務文脈を組織外にも共有する。
- Operations AgentsとActivatorで原因分析と対応を自動化し、AI規模拡大時の運用を支える。
- 成果物と境界を人が定め、その範囲内でエージェントが計画・実行・検証する。

## 使いどころ

- Power BIの指標をCopilotで使いたい企業のデータ・BI部門。
- パートナーや顧客とガバナンス付きでデータ共有したい組織。
- データエンジニアリングの自動化を段階的に進めたい基盤チーム。
