---
type: guidance
title: AKSまたはVMでメインフレームをAzureへリファクタリングする汎用アーキテクチャ
title_original: General mainframe refactor to Azure - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/general-mainframe-refactor
published_at: '2026-06-12'
---

## 概要

COBOLやPL/Iなどで書かれたメインフレームアプリケーションを、コードをJavaや.NETへ自動変換し、階層型データベースをリレーショナルデータベースへ変換することでAzureへの移行を加速するリファクタリング手法を解説する。移行後はAzure VMまたはAKS上のコンテナでアプリケーションを稼働させ、Azure SQL DatabaseなどのPaaSデータサービスに接続する。
