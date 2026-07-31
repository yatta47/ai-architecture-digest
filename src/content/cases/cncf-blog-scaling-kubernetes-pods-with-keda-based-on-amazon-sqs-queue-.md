---
type: guidance
title: SQSキュー滞留量に基づきKEDAでKubernetesワーカーをオートスケールする
title_original: Scaling Kubernetes Pods with KEDA Based on Amazon SQS Queue Depth
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: cost
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/07/31/scaling-kubernetes-pods-with-keda-based-on-amazon-sqs-queue-depth/
published_at: '2026-07-31'
---

## 概要

Amazon SQSのキュー滞留量をスケーリング指標として使い、KEDAとAmazon EKSでイベント駆動型ワーカーをオートスケールする方法を解説。CPU/メモリではなく実際の未処理メッセージ数に基づいてスケールすることで、バースト対応とアイドル時のコスト削減を両立する。
