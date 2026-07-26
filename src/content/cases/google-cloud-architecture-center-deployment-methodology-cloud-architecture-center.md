---
type: guidance
title: Google Cloudのエンタープライズ基盤をTerraform+GitOpsで階層的にデプロイする方法
title_original: Deployment methodology
ai_relevant: false
industry: cross-industry
cloud:
- gcp
patterns: []
components: []
outcome:
  type: reliability
source_id: google-cloud-architecture-center
source_name: Google Cloud Architecture Center
source_url: https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology
published_at: '2026-07-19'
---

## 概要

Google Cloudのセキュリティ基盤ブループリントは、Terraformによる宣言的IaCとGit・Cloud Buildを使ったGitOpsフローで組織基盤をデプロイする。基盤・インフラ・アプリケーションの3層にパイプラインを分離し、チームごとに権限とレビューを分離する運用モデルを推奨する。
