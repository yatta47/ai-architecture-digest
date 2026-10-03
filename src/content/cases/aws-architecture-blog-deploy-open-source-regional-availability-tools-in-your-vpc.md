---
type: guidance
title: リージョン別サービス提供状況ツールを自社VPCに展開する
title_original: Deploy open source Regional availability tools in your VPC
ai_relevant: false
company: AWS
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: productivity
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/deploy-open-source-regional-availability-tools-in-your-vpc/
published_at: '2026-10-02'
---

## 概要

AWSのリージョン別提供状況データを自社VPC内で運用するOSS、Capability Insights for AWSとWorkload Analysisの導入方法を紹介する。前者は24時間ごとに更新されるダッシュボードを自アカウントに展開し、後者はCloudTrailとCloudFormationから実際に使うサービスに絞って差分分析する。AI基盤が主題ではない汎用インフラ運用の記事。
