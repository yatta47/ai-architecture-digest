---
type: announcement
title: Kubernetes APIサーバーのetcd大量読み取りをストリーミング化しメモリ使用量を削減
title_original: 'Kubernetes v1.37: etcd RangeStream Cuts Memory Use on Large List Reads'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/09/01/kubernetes-v1-37-etcd-range-stream/
published_at: '2026-09-01'
---

## 概要

Kubernetes v1.37とetcd v3.7の組み合わせで、etcdの新しいRangeStream RPCがベータに昇格した。APIサーバーがwatchキャッシュ初期化などで大きなコレクションを読み取る際、従来のRangeはページ全体をメモリに保持してから返すのに対し、RangeStreamはバイト単位でチャンクをストリーミング配信するため、メモリ使用量が予測可能になりOOMのリスクを抑えられる。
