---
type: guidance
title: Kueueの承認状況をHeadlampで追跡してJobのPending原因を調べる
title_original: Why Is My Kubernetes Job Still Pending? Tracing Kueue Admission with Headlamp
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: reliability
source_id: kubernetes-blog
source_name: Kubernetes Blog
source_url: https://kubernetes.io/blog/2026/10/14/tracing-kueue-admission-with-headlamp/
published_at: '2026-10-14'
---

## 概要

KueueでJobが止まる場合に、まずWorkloadが承認されたかを確認する手順を紹介する。HeadlampのKueueプラグインでWorkloadからLocalQueue、ClusterQueue、ResourceFlavor、Cohortを辿って原因を調べる。
