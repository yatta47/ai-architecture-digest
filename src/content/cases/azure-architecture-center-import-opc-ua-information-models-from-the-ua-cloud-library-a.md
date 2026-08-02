---
type: guidance
title: UA Cloud LibraryからOPC UA情報モデルを取り込みオフラインで機器を事前構成する
title_original: Import OPC UA Information Models from the UA Cloud Library
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/iot/import-opc-ua-information-models-from-ua-cloud-library
published_at: '2026-07-30'
---

## 概要

OPC FoundationとCESMIIが運営するクラウド上のOPC UA情報モデルリポジトリ「UA Cloud Library」から、機器が稼働する前にモデルを取得しAzure Data Explorerへ取り込む方法を解説する。これにより実機オンライン前のオフラインエンジニアリングや、レガシー機器へのモデル再利用が可能になる。
