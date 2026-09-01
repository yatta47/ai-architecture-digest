---
type: announcement
title: Kubernetes 1.37でストレージバージョンマイグレーションがデフォルト有効に
title_original: 'Kubernetes v1.37: Storage Version Migration Enabled by Default'
ai_relevant: false
industry: cross-industry
cloud:
- multi-cloud
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/08/31/kubernetes-v1-37-storage-version-migration-ga/
published_at: '2026-08-31'
---

## 概要

Kubernetes v1.37でStorageVersionMigration APIがGAとなり、CRDの古いストレージバージョンや暗号化キー更新後の既存リソースを宣言的なマニフェストで自動的に最新バージョンへ書き換えられるようになった。手作業でのkubectl get/replaceスクリプトや外部ツールへの依存を解消する。
