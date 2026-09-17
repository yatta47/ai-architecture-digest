---
type: announcement
title: Kubernetes v1.37のbind mountオプションとemptyDirパーミッション強化
title_original: 'Kubernetes v1.37: Hardening Container Storage with Bind Mount Options and EmptyDir Permissions'
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/09/16/kubernetes-v1-37-hardening-container-storage/
published_at: '2026-09-16'
---

## 概要

Kubernetes v1.37はストレージのセキュリティ機能としてbind mountオプション（noexec/nosuid/nodev）とemptyDirのパーミッションモード（mode指定・sticky bit）をアルファ機能として追加した。読み取り専用ルートファイルシステムでも書き込み可能ボリューム経由で任意バイナリが実行されるリスクや、マルチコンテナPodでのファイル削除競合を、initコンテナを使わずネイティブに防げるようになる。
