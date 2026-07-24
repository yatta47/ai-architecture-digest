---
type: guidance
title: AKSクラスタのネットワーク障害トラブルシューティング
title_original: Troubleshoot network problems in AKS clusters
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/operator-guides/aks/troubleshoot-network-aks
published_at: '2024-03-12'
---

## 概要

AKSクラスタでAPIサーバーへの疎通不可、PodのIPアドレス割当失敗、サービス到達不能といったネットワーク障害の典型的な原因と診断手順を整理。認可済みIPレンジの確認やCNIプラグインの不具合対応など、具体的なコマンド例とともに対処法を示す。
