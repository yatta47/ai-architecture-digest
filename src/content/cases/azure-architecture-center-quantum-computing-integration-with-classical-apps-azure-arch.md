---
type: guidance
title: Azure Quantumで量子コンピューティングとクラシックアプリを統合する2つのアーキテクチャパターン
title_original: Quantum computing integration with classical apps
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/quantum/quantum-computing-integration-with-classical-apps
published_at: '2026-06-25'
---

## 概要

Azure Architecture Centerのリファレンスアーキテクチャで、量子コンピューティングコンポーネントを古典的なアプリケーションに統合する「密結合」と「疎結合」の2方式を解説する。いずれもAzure Quantum・Key Vault・Microsoft Entra IDを用い、入力データ準備・ジョブ投入・実行監視・結果後処理という一連のオーケストレーションを非同期リクエスト応答パターンで実装する。密結合は単一チームが量子・古典コードを一体運用する専用ソリューション向け、疎結合はAPI経由で複数の古典アプリから再利用できる汎用量子機能の提供に適する。
