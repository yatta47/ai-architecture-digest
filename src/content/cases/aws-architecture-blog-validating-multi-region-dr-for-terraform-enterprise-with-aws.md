---
type: case
title: Athenahealthが検証したTerraform Enterpriseのマルチリージョンディザスタリカバリ
title_original: Validating multi-Region DR for Terraform Enterprise with AWS FIS
ai_relevant: false
company: Athenahealth
industry: healthcare
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/validating-multi-region-dr-for-terraform-enterprise-with-aws-fis/
published_at: '2026-09-09'
---

## 概要

電子カルテ大手Athenahealthは、us-east-1の単一リージョン障害でHashiCorp Terraform Enterprise環境が利用不能になった経験から、AWS FISとAuroraグローバルデータベース、S3クロスリージョンレプリケーションを用いたマルチリージョンDR構成を検証した。段階的なFIS実験により12〜14分の復旧時間を達成した。
