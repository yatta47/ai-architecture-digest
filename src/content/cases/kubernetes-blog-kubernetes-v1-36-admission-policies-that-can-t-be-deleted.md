---
type: announcement
title: Kubernetesの削除不能なマニフェストベースAdmissionポリシー
title_original: 'Kubernetes v1.36: Admission Policies That Can''t Be Deleted'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/05/04/kubernetes-v1-36-manifest-based-admission-control/
published_at: '2026-05-04'
---

## 概要

APIオブジェクトとして作成されるAdmissionポリシーは、クラスタ起動直後の未適用期間や、特権ユーザーによる削除に弱いという弱点があった。Kubernetes v1.36はディスク上のマニフェストファイルをAPIサーバー起動時に読み込むmanifest-based admission control（アルファ機能）を導入し、常時有効なポリシー適用を可能にする。
