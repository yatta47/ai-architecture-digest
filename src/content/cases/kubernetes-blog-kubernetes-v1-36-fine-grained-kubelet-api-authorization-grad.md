---
type: announcement
title: kubelet APIの最小権限化(Fine-Grained Authorization)がGAに到達
title_original: 'Kubernetes v1.36: Fine-Grained Kubelet API Authorization Graduates to GA'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/04/24/kubernetes-v1-36-fine-grained-kubelet-authorization-ga/
published_at: '2026-04-24'
---

## 概要

監視エージェント等に付与すると事実上ノード上の全コンテナでコマンド実行が可能になってしまう粗粒度のnodes/proxy権限を、/metrics・/stats・/pods等ごとに専用のサブリソースへ分割するFine-Grained Kubelet API Authorizationがv1.36でGAに到達。WebSocketハンドシェイクの実装不備を突いたnodes/proxy GETのみでコマンド実行が可能になる脆弱性への対策も兼ね、既存RBAC権限への後方互換フォールバックにより無停止での移行を可能にする。
