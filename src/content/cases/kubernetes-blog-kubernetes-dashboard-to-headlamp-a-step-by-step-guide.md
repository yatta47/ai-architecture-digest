---
type: guidance
title: Kubernetes DashboardからHeadlampへの移行手順
title_original: 'Kubernetes Dashboard to Headlamp: A Step-by-Step Guide'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/07/13/kubernetes-dashboard-to-headlamp/
published_at: '2026-07-13'
---

## 概要

Kubernetes公式ブログが、クラスタ内蔵型でサービスアカウントトークンに依存するKubernetes Dashboardから、kubeconfigベースでデスクトップ/クラスタ内のどちらでも動作しマルチクラスタやプラグイン拡張に対応するHeadlampへの移行手順を解説する。現状棚卸し・kubeconfig動作確認・並行運用またはカットオーバーのロールアウト計画選定・デスクトップ/クラスタ内インストールという段階的なチェックリストを提示している。
