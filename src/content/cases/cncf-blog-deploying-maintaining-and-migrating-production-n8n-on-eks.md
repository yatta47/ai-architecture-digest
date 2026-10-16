---
type: case
title: EKS上の本番n8nを公式Helmチャートへ移行
title_original: Deploying, Maintaining, and Migrating Production n8n on EKS
ai_relevant: false
company: Fairwinds
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: cncf-blog
source_name: CNCF Blog
source_url: https://www.cncf.io/blog/2026/10/16/deploying-maintaining-and-migrating-production-n8n-on-eks/
published_at: '2026-10-16'
---

## 概要

FairwindsはAmazon EKSでn8nをキューモードで運用し、コミュニティ版から公式Helmチャートへ全面切替で移行した。状態はPostgreSQL、Redis、S3、Secrets Managerに置き、メインPodの永続ボリュームを無効化した。
