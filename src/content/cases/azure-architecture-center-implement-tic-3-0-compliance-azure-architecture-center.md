---
type: guidance
title: TIC 3.0準拠のためのAzureネットワークログ集約アーキテクチャ（CISA CLAW連携）
title_original: Implement TIC 3.0 compliance
ai_relevant: false
industry: public-sector
cloud:
- azure
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/networking/architecture/trusted-internet-connections
published_at: '2026-06-02'
---

## 概要

米連邦政府機関（FCEB）向けに、Azure Firewall/Application Gateway/Front Doorのログを Log Analytics に集約し、Event Hubs 経由でCISAのTALON/CLAWに送信することでTIC 3.0コンプライアンスを満たす構成。
