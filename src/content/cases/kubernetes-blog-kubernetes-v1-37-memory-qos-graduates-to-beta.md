---
type: announcement
title: Kubernetes v1.37でMemory QoSがベータ昇格しデフォルト有効化
title_original: 'Kubernetes v1.37: Memory QoS Graduates to Beta'
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/09/14/kubernetes-v1-37-memory-qos-graduates-to-beta/
published_at: '2026-09-14'
---

## 概要

Kubernetes v1.37でMemory QoS機能がベータに昇格しデフォルト有効化。cgroup v2上でmemory.high(スロットリング)やmemory.min/low(階層的予約)をkubelet設定で制御できるようになったが、デフォルトでは動作変更なし(memoryThrottlingFactorはnullに変更)。予約ポリシーはノード単位で適用されるため混在ワークロードでは注意が必要。
