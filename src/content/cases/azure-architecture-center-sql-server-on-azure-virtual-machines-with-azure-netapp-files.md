---
type: guidance
title: Azure NetApp FilesによるAzure VM上のSQL Server移行アーキテクチャ
title_original: SQL Server on Azure Virtual Machines with Azure NetApp Files
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: cost
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/file-storage/sql-server-azure-netapp-files
published_at: '2026-06-03'
---

## 概要

オンプレミスのSQL ServerワークロードをAzure VM上に移行する際、SMBプロトコルで高性能・低遅延なファイルストレージを提供するAzure NetApp Filesをデータ/ログファイルの格納先に使う構成を解説する。VMのディスクI/O上限を回避しつつ、Always On可用性グループやSnapCenterによるバックアップでHA/DRとコスト効率を両立する設計を示す。
