---
type: guidance
title: Azure Governance VisualizerによるガバナンスOSS可視化基盤の自動デプロイ
title_original: Use Azure Governance Visualizer to optimize cloud governance
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/landing-zones/azure-governance-visualizer-accelerator
published_at: '2026-05-23'
---

## 概要

オープンソースのAzure Governance Visualizerをタイマー起動のGitHub Actionsで自動実行し、管理グループ階層やポリシー、セキュリティ情報をHTML等で出力してApp Serviceで安全に公開するアーキテクチャ。Entra ID認証とプライベートエンドポイントでアクセスを制限する。
