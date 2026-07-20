---
type: announcement
title: 分散KVSストア etcd v3.7.0 のリリース
title_original: Announcing etcd v3.7.0
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: speed
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/07/08/announcing-etcd-3.7/
published_at: '2026-07-08'
---

## 概要

Kubernetesのコアコンポーネントである分散キーバリューストアetcdのv3.7.0がリリースされた。大きな結果セットをチャンク単位でストリーミングできるRangeStream、keys-onlyレンジ最適化、より高速で信頼性の高いリース処理などの性能改善に加え、v2storeへの依存を排除しprotobuf周りを刷新した。
