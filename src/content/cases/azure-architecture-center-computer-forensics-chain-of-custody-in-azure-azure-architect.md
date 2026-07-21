---
type: guidance
title: Azureにおけるコンピュータフォレンジックのチェーン・オブ・カストディ基盤
title_original: Computer forensics chain of custody in Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/forensics/
published_at: '2026-06-11'
---

## 概要

法的請求に対応するデジタル証拠のチェーン・オブ・カストディ（証拠保全の連鎖）を担保するためのAzureアーキテクチャ。専用のSOCサブスクリプションでVMディスクのスナップショットをイミュータブルBlobストレージに保存し、Azure Key Vaultにハッシュ値を記録することで証拠の完全性を証明する。Azure Automationのハイブリッドランブックワーカーが証拠取得プロセス全体をシステム割り当てマネージドIDで自動実行する。
