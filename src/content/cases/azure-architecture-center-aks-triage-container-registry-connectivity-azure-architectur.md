---
type: guidance
title: AKSとコンテナレジストリ間の接続トラブルシューティング
title_original: Verify the connection to the container registry
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/operator-guides/aks/aks-triage-container-registry
published_at: '2026-06-26'
---

## 概要

AKSクラスターがコンテナレジストリからイメージを取得できずImagePullBackOffやErrImagePullが発生する場合の原因切り分け手順を解説するガイド。kubeletのマネージドIDへのAcrPullロール割り当てやABAC対応レジストリでの権限設定、az aks check-acrによる疎通確認の方法を示す。さらにネットワーク・サインイン・パフォーマンスの観点別トラブルシューティング手順も網羅している。
