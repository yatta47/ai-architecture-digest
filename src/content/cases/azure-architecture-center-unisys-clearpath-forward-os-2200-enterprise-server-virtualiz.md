---
type: case
title: Unisys ClearPath Forward OS 2200エンタープライズサーバーのAzure仮想化移行
title_original: Unisys ClearPath Forward OS 2200 enterprise server virtualization on Azure
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/mainframe/virtualization-of-unisys-clearpath-forward-os-2200-enterprise-server-on-azure
published_at: '2026-07-01'
---

## 概要

UnisysのClearPath Forward(CPF) Dorado(OS 2200)エンタープライズサーバーを、COBOL/Fortranなど既存アプリケーションやデータベース構造を変更せずにAzure仮想マシンへ移行するアーキテクチャ。Unisys SAIL仮想マシン上でテープ・印刷サブシステムを含む運用環境をそのまま再現し、Azure BastionによるセキュアなVM管理やAzure Storageへのディスクマッピングを組み合わせることで、移行コストとユーザー再教育コストを最小化する。
