---
type: guidance
title: Microsoft Fabricで構築するエンドツーエンド分析プラットフォーム
title_original: Analytics end-to-end with Microsoft Fabric
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: quality
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/dataplate2e/data-platform-end-to-end
published_at: '2026-06-05'
---

## 概要

Microsoft Fabricを中核に、オンプレミスやAWS S3・Google Cloud Storageなど多様なソースからのデータをOneLakeに集約し、レイクハウス・データウェアハウス・イベントハウスを使い分けて取り込み・格納・処理・提供する参照アーキテクチャ。メダリオン構成（Bronze/Silver/Gold）やミラーリングによる準リアルタイム同期に加え、Purviewによるガバナンス、Entra IDによるID管理、GitHub/Azure DevOpsによるCI/CDで運用基盤を支える。
