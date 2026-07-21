---
type: guidance
title: RaincodeコンパイラでCOBOLメインフレームをコード無改修のままAzureへリホスト
title_original: Rehost mainframe applications to Azure with Raincode compilers - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/app-modernization/raincode-reference-architecture
published_at: '2026-06-12'
---

## 概要

Raincode COBOLコンパイラがCOBOLコードを.NET/.NET Coreのスレッドセーフなマネージドコードへ変換し、AKSやVM上でコンテナ実行することで、コード変更なしにメインフレームアプリをAzureへ移行するアーキテクチャ。Db2/IDMSなどのレガシーDBはAzure SQL Databaseへ、VSAMなどのファイル構造はBlob Storageへマッピングし、Private LinkやGeo冗長ストレージでDR/HAを確保する。
