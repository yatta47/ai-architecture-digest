---
type: announcement
title: Kubernetesのノードコンポーネントを非rootで動かすRootlessモードがベータに
title_original: 'Kubernetes v1.37: KubeletInUserNamespace (aka Rootless mode) Graduates to Beta'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/09/04/kubernetes-v1-37-rootless-beta/
published_at: '2026-09-04'
---

## 概要

Kubernetes v1.37でKubeletInUserNamespace（Rootlessモード）機能ゲートがベータに昇格し、kubelet・CRI/OCIランタイム・CNIプラグイン・kube-proxyをLinuxユーザー名前空間内で非rootユーザーとして実行できるようになった。過去のコンテナブレイクアウト脆弱性の被害をホストのroot権限まで広げず非root権限内に封じ込めることが目的で、共有マシンやAIエージェントのサンドボックス用途にも有効とされる。
