---
type: announcement
title: KubernetesのCSI変更ブロック追跡APIがベータへ昇格しCRDがv1beta1に
title_original: Kubernetes Changed Block Tracking API - Beta Differences
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/09/14/csi-changed-block-tracking-beta/
published_at: '2026-09-14'
---

## 概要

KubernetesのCSI Changed Block Tracking APIがベータに昇格。SnapshotMetadataService CRDがv1alpha1からv1beta1に変わり(スキーマは同一)、ブロックボリュームの変更差分追跡によりバックアップアプリケーションが差分バックアップを効率化できるようになった。
