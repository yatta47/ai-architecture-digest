---
type: guidance
title: Azure上でセキュアなLinux VMを構築する標準リファレンス構成
title_original: Run a Linux VM on Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/n-tier/linux-vm
published_at: '2026-07-01'
---

## 概要

AzureでLinux VMを安全に運用するための標準構成をまとめたリファレンスアーキテクチャ。NATゲートウェイ経由のアウトバウンド接続とAzure BastionによるSSH管理でVMへの直接インターネット露出を排除し、Premium SSDのマネージドディスクと一時ディスクの使い分け、診断ログのStorageアカウントへの集約などVMサイジング・ディスク選定・バックアップに関する実務的なベストプラクティスを示す。
