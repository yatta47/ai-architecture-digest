---
type: announcement
title: KubernetesバッチスケジューラVolcanoをHeadlampで可視化するプラグイン
title_original: Inspect Volcano workloads faster with Headlamp
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: productivity
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/06/25/visual-context-volcano-headlamp-plugin/
published_at: '2026-06-25'
---

## 概要

Kubernetes向けバッチスケジューラVolcanoのJob・Queue・PodGroupを、拡張可能なWeb UIであるHeadlampのプラグインとして一元的に確認できるようにした。従来はkubectlやVolcano CLIで複数リソースを行き来する必要があったが、詳細ビューやマップビューでリソース間の関係を可視化し、ログ閲覧やSuspend/Resumeといった操作もUIから行えるようにしている。
