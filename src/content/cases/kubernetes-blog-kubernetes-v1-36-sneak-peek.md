---
type: announcement
title: Kubernetes v1.36における非推奨・削除とセキュリティ強化の先行紹介
title_original: Kubernetes v1.36 Sneak Peek
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/03/30/kubernetes-v1-36-sneak-peek/
published_at: '2026-03-30'
---

## 概要

Kubernetesは2026年4月末リリース予定のv1.36で、Service .spec.externalIPsの非推奨化やgitRepoボリュームドライバの恒久廃止など、既知のセキュリティリスクに対応するAPI削除・非推奨化を進める。あわせてIngress NGINXプロジェクトの引退（2026年3月24日）を受け、代替のIngressコントローラへの移行が推奨されている。SELinuxラベリング高速化のGA化やServiceAccountトークンの外部署名のGA化など、安定性・セキュリティを高める機能強化も予定されている。
