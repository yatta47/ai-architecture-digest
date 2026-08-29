---
type: announcement
title: Kubernetes 1.37のPod証明書自動発行機構(Pod Certificates/Cluster Trust Bundles)
title_original: 'Kubernetes v1.37: Pod Certificates and Cluster Trust Bundles'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/08/28/kubernetes-v1-37-pod-certificates-and-cluster-trust-bundles/
published_at: '2026-08-28'
---

## 概要

Kubernetes 1.37で、Pod単位のX.509証明書を自動発行・更新するPod CertificatesとCluster Trust BundlesがGAになった。従来の主要な本番アイデンティティ手段であるサービスアカウントJWTはベアラートークンのため盗用リスクがあるのに対し、Pod Certificatesは秘密鍵をワークロード内に留めた証明書ベースの所有証明方式を提供する。Kubeletが鍵生成とPodCertificateRequestの発行を担い、pluggableなsigner controllerが証明書発行とClusterTrustBundleの公開を行う構成になっている。
