---
type: guidance
title: メインフレーム/ミッドレンジのアーカイブデータをAzureへ移す各種転送手法
title_original: Move archive data from mainframe systems to Azure - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mainframe/move-archive-data-mainframes
published_at: '2026-06-12'
---

## 概要

コンプライアンス要件で保持が必要なメインフレーム/ミッドレンジのアーカイブデータを、Azure Data FactoryのFTPコネクタやJCLベースのカスタムJavaソリューション、大容量向けのAzure Data Boxなど複数手法でAzure Storageへ移すリファレンスアーキテクチャ。アーカイブデータはメインフレーム側でのみ利用され、Azureは低コストな保管媒体としてのみ使う設計を示す。
