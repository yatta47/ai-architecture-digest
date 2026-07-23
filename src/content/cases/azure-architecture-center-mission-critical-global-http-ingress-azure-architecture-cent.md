---
type: guidance
title: Azure Front DoorとApplication Gatewayを組み合わせた高可用グローバルHTTP入口設計
title_original: Mission-critical global HTTP ingress
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/guide/networking/global-web-applications/mission-critical-global-http-ingress
published_at: '2025-12-19'
---

## 概要

Azure Front Doorをグローバルなプライマリ経路とし、Front Doorが利用不能になった場合にAzure Traffic ManagerでApplication Gatewayへ自動的にフェイルオーバーする、ミッションクリティカルなグローバルHTTP入口の構成を解説する。重み付けルーティングとパフォーマンスルーティングを組み合わせた2段のTraffic Managerプロファイルで、各リージョンのApplication Gatewayインスタンスの健全性を監視しながら単一障害点を排除する。
