---
type: case
title: CloudFormationカスタムリソースのマルチリージョン耐障害アーキテクチャ
title_original: Building multi-Region resiliency for AWS CloudFormation custom resource deployment
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/building-multi-region-resiliency-for-aws-cloudformation-custom-resource-deployment/
published_at: '2026-07-22'
---

## 概要

AWS CloudFormationのカスタムリソースは単一リージョンでの実行が前提であり、リージョン障害時の自動フェイルオーバーや重複実行防止の仕組みが標準では提供されていない。この記事では、プライマリ(us-east-1)とセカンダリ(us-west-2)の2リージョンでSNS/SQSによるイベントのファンアウトを行い、DynamoDB Global Tablesによる分散ロックと冪等性管理、Amazon Application Recovery Controllerによる自動フェイルオーバーを組み合わせたActive-Active構成のアーキテクチャを紹介している。
