---
type: guidance
title: AKSのAdmission Controller（Webhook）健全性をトリアージする手順
title_original: Validate admission controllers
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/operator-guides/aks/aks-triage-controllers
published_at: '2025-01-20'
---

## 概要

AKSクラスタでAzure PolicyのGatekeeperやKyverno、サービスメッシュのサイドカー注入などに使われるMutating/Validating Webhook（Admission Controller）が不調な場合にAPIサーバーへのリクエストがブロックされうることを解説し、kubectlコマンドでPodの稼働状況・Webhook設定・ポリシー割り当ての同期状況を検証する手順を示す。
