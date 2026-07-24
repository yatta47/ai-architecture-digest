---
type: guidance
title: AKSクラスタのトップダウン・トリアージ手法
title_original: Triage practices for AKS operations
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/operator-guides/aks/aks-triage-practices
published_at: '2025-01-20'
---

## 概要

AKSクラスタの根本原因分析は難易度が高いため、クラスタ階層に沿ったトップダウンのトリアージ手法を提案する。クラスタ全体の健全性確認からノード/Pod、デプロイ、アドミッションコントローラ、コンテナレジストリ接続まで段階的に切り分けるシリーズの概要。
