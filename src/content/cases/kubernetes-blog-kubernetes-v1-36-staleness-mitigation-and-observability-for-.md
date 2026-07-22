---
type: announcement
title: Kubernetesコントローラーのキャッシュ鮮度問題を緩和する新機能
title_original: 'Kubernetes v1.36: Staleness Mitigation and Observability for Controllers'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/04/28/kubernetes-v1-36-staleness-mitigation-for-controllers/
published_at: '2026-04-28'
---

## 概要

kube-controller-managerのコントローラーがローカルキャッシュの古さ(staleness)により誤ったり遅れたアクションを取る問題に対応するため、Kubernetes v1.36でclient-goにAtomicFIFOキュー処理を追加。DaemonSet/StatefulSet/ReplicaSet/JobコントローラーがAPIサーバーへの書き込みresourceVersionとキャッシュの整合性を確認してから動作するようになり、独自informerでも同様の鮮度チェックを実装できるConsistencyStoreが提供された。
