---
type: announcement
title: 複数ボリュームを一貫点で保護するKubernetesグループスナップショットがGAに
title_original: 'Kubernetes v1.36: Moving Volume Group Snapshots to GA'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/05/08/kubernetes-v1-36-volume-group-snapshot-ga/
published_at: '2026-05-08'
---

## 概要

Kubernetes v1.36で、複数のPersistentVolumeClaimをラベルセレクタでグループ化し同一時点でクラッシュコンシステントなスナップショットを取得する「ボリュームグループスナップショット」機能がGeneral Availabilityに到達した。VolumeGroupSnapshot・VolumeGroupSnapshotContent・VolumeGroupSnapshotClassの3つのCRD APIをv1に昇格させ、CSIドライバ対応ストレージであれば、複数ボリュームにまたがるアプリケーションをアプリ側の停止処理なしで整合性のある状態から復元できるようになった。
