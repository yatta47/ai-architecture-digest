---
type: guidance
title: 共有サービスを中央集約するAzureのハブ&スポーク型ネットワーク構成
title_original: Hub-spoke network topology in Azure - Azure Architecture Center
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/networking/architecture/hub-spoke
published_at: '2026-06-13'
---

## 概要

ハブ仮想ネットワークにファイアウォールやVPNゲートウェイ、Bastionなど共有ネットワークサービスを集約し、本番・非本番などのワークロードごとに分離したスポーク仮想ネットワークをピアリング接続する、Azureで推奨されるハブ&スポーク型トポロジを解説する。全てのアウトバウンド通信をハブ経由に集約することで、送受信トラフィックの一元的な制御と監視を実現する。
