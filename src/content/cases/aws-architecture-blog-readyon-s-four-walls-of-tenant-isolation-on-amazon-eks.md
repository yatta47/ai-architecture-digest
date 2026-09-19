---
type: case
title: Amazon EKS上でのマルチテナント分離『Four Walls』アーキテクチャ
title_original: ReadyOn's Four Walls of tenant isolation on Amazon EKS
ai_relevant: false
company: ReadyOn
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/readyons-four-walls-of-tenant-isolation-on-amazon-eks/
published_at: '2026-09-18'
---

## 概要

労務管理プラットフォームを運営するReadyOnは、Amazon EKS上のマルチテナント環境において、ネームスペース分離・Karpenterによるテナント専用ノードプール・VPCセキュリティグループによるネットワーク分離・テナントごとのAmazon Auroraデータベースという4層の独立した境界を組み合わせた『Four Walls』アーキテクチャを構築した。ペイロールや組織階層など機微なデータを扱うため、単一の分離機構に頼らず、複数層を同時に突破しない限りテナント間の越境アクセスができない多層防御を採用している。
