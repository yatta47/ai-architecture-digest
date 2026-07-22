---
type: announcement
title: Kubernetes Service ExternalIPsフィールドの非推奨化とセキュリティ代替策
title_original: 'Kubernetes v1.36: Deprecation and removal of Service ExternalIPs'
ai_relevant: false
industry: cross-industry
cloud:
- on-prem
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/05/14/kubernetes-v1-36-deprecation-and-removal-of-service-externalips/
published_at: '2026-05-14'
---

## 概要

Kubernetes 1.36で`.spec.externalIPs`フィールドが正式に非推奨となったことを発表する記事。このフィールドはクラスタ内の全ユーザーを信頼する前提で設計されておりCVE-2020-8554の脆弱性の原因となっていたため、MetalLBなどの非クラウドロードバランサコントローラやGateway APIへの移行が代替策として推奨されている。
