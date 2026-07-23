---
type: guidance
title: ミッションクリティカルなAKSワークロードの高可用性アプリケーション設計
title_original: Application design considerations for mission-critical workloads
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/containers/aks-mission-critical/mission-critical-app-design
published_at: '2025-09-22'
---

## 概要

Azure Architecture Centerによるミッションクリティカルワークロード向けリファレンスアーキテクチャの解説記事。オンラインカタログを題材に、AKS上でステートレスなAPI・ワーカー・ヘルスチェックの各コンポーネントを分離し、Azure Cosmos DBによる外部データストアと非同期メッセージングで高可用性とスケーラビリティを実現する設計を紹介している。デプロイスタンプがいつでも削除・再作成できることを前提に、疎結合とキューベースの負荷平準化パターンを推奨している。
