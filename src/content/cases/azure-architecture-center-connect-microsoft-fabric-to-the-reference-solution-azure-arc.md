---
type: guidance
title: 産業IoTのOPC UAテレメトリをMicrosoft Fabric Eventhouseに取り込みOneLakeで組織横断共有する
title_original: Connect Microsoft Fabric to the reference solution
ai_relevant: false
industry: manufacturing
cloud:
- azure
patterns: []
components: []
outcome:
  type: productivity
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/iot/how-to-connect-fabric-to-solution
published_at: '2026-06-20'
---

## 概要

Azureサブスクリプションなしでも使えるMicrosoft Fabricを使い、産業IoTリファレンスソリューションが発行するOPC UA PubSubのテレメトリ・メタデータをEventhouseに取り込む方法を解説する。Azure Data Explorerと同じテーブル・関数・マテリアライズドビュー構成をFabric上に再現し、OneLake経由でParquet形式の時系列データを組織内で共有できるようにする。
