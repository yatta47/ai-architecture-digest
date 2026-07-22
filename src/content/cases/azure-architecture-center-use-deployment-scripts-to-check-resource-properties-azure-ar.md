---
type: guidance
title: Bicepデプロイスクリプトでリソースの準備完了を待ってから依存モジュールを実行する設計パターン
title_original: Use deployment scripts to check resource properties
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/devops/deployment-scripts-property-check
published_at: '2026-05-08'
---

## 概要

Azure Resource Managerがリソースを作成完了と報告しても、その配下の実体（例: Virtual WANハブのルーティング設定）がまだ利用可能とは限らない場合に、Bicepのデプロイスクリプトリソースでプロパティ値をポーリングし、条件を満たすまでデプロイを一時停止するパターンを解説する。Virtual WANハブのroutingStateプロパティがProvisionedになるまで待機し、それを満たしてから依存するVNet接続モジュールをdependsOnで実行することで、デプロイの競合状態による失敗を防ぐ。
