---
type: guidance
title: Azure Virtual WANにおける仮想ハブ拡張パターン
title_original: Virtual hub extension pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/networking/guide/private-link-virtual-wan-dns-virtual-hub-extension-pattern
published_at: '2026-05-01'
---

## 概要

Azure Virtual WANの仮想ハブには直接リソースを配置できない制約があるため、DNSやAzure Bastionのような共有サービスを専用のスポーク仮想ネットワーク（ハブ拡張）として構築し、複数のワークロードスポークへ単一責任の原則で公開するパターンを解説。信頼性・セキュリティ・コスト最適化・運用の各観点から設計上の考慮点を示す。
