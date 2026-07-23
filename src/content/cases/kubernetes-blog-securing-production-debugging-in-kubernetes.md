---
type: guidance
title: Just-in-Timeゲートウェイで本番デバッグアクセスを安全化する
title_original: Securing Production Debugging in Kubernetes
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/03/18/securing-production-debugging-in-kubernetes/
published_at: '2026-03-18'
---

## 概要

cluster-adminや共有Bastion、長期SSH鍵に頼りがちな本番デバッグアクセスを、RBAC最小権限・短命でID紐付けされた証明書・SSH的なJITゲートウェイの組み合わせで安全化する実践ガイド。グループ単位でのRBACバインディングとコマンド単位の承認ポリシーを推奨する。
