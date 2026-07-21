---
type: case
title: 教育ローン大手Avanseが外部BIツールを廃し、Amazon SageMaker Unified Studioでレイクハウス型分析基盤に刷新
title_original: Modernizing financial analytics with Amazon SageMaker Unified Studio
ai_relevant: false
company: Avanse Financial Services
industry: financial-services
cloud:
- aws
patterns: []
components: []
outcome:
  type: cost
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/modernizing-financial-analytics-with-amazon-sagemaker-unified-studio/
published_at: '2026-06-22'
---

## 概要

インドの教育ローン大手Avanse Financial Servicesは、AWS上のデータレイクと連携しない外部分析ツールを使っていたため、日次の4時間バッチ同期や利用実態に見合わない固定ライセンス費用、監査性の低さに悩んでいた。Amazon SageMaker Unified Studioへ移行し、Amazon S3上のデータに直接クエリするレイクハウス構成へ刷新することで、データコピー工程を排除し、Athena/EMR Serverlessによる従量課金とプロジェクト単位のガバナンスを実現した。
