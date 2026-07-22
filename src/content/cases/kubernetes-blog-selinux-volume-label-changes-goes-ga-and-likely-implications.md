---
type: guidance
title: SELinuxボリュームラベリングの高速化とv1.37での互換性影響
title_original: SELinux Volume Label Changes goes GA (and likely implications in v1.37)
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/04/22/breaking-changes-in-selinux-volume-labeling/
published_at: '2026-04-22'
---

## 概要

SELinux強制モードで動くKubernetesクラスタ向けに、ボリュームの再帰的ラベリングを高速化するSELinuxMountがv1.37でデフォルト有効化される見込みを解説する。特権/非特権Pod間でボリュームを共有するような従来の再帰ラベリング依存構成は壊れる可能性があるため、v1.36のうちに監査・対応することを推奨している。
