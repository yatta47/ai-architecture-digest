---
type: guidance
title: ヘルスチェックでスケールゼロが壊れる問題をKubeElastiのProbeResponseで解決
title_original: Your Kubernetes Health Checks Are Accidentally Waking Your Services. Here's the Fix.
ai_relevant: false
industry: cross-industry
cloud:
- aws
- gcp
- azure
patterns: []
components: []
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/29/your-kubernetes-health-checks-are-accidentally-waking-your-services-heres-the-fix/
published_at: '2026-07-29'
---

## 概要

Kubernetesのスケールツーゼロは、ロードバランサーやモニタリングのヘルスチェックがリゾルバー層に届くとスケールアップ信号として解釈されてしまい、意図せずポッドが起動しコスト削減効果が失われる問題がある。KubeElastiは新機能ProbeResponseで、リゾルバーがヘルスチェックにマッチするリクエストをオペレーターへ通知せず直接200 OKなどで応答するルールを追加し、実トラフィックのみがスケールアップをトリガーするようにした。この仕組みはサービスがゼロレプリカでリゾルバーが既にトラフィックを横取りしている時だけ動くため、追加のプロキシやレイテンシコストなしに実現される。
