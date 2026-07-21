---
type: guidance
title: メインフレームファイルのAzureへの複製・同期ソリューションアイデア
title_original: Mainframe file replication and sync on Azure - Azure Architecture Center
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/solution-ideas/articles/mainframe-azure-file-replication
published_at: '2026-06-12'
---

## 概要

オンプレミスのメインフレーム/ミッドレンジファイルをAzureへ複製・同期する複数手法(SFTP、Self-hosted Integration RuntimeによるData Factory連携、Host Integration ServerによるEBCDIC→ASCII変換など)を整理したソリューションアイデア。変換・オーケストレーションにはAzure DatabricksやMicrosoft Fabricを用い、Data Lake StorageやCosmos DBなど用途に応じた保存先を選択する。
