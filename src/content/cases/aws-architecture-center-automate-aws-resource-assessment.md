---
type: guidance
title: CDKで自動化するAWSリソース棚卸しダッシュボード
title_original: Automate AWS resource assessment
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: aws-architecture-center
source_name: AWS Architecture Center
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-aws-resource-assessment.html?did=pg_card&trk=pg_card
published_at: '2023-10-21'
---

## 概要

AWS CDKでCloudTrailログをS3・Glue・Athena経由でQuickSightダッシュボードに集約し、Terraform/CloudFormation/CDK/CLIなど異なるIaCツールで作成されたリソースを横断的に棚卸しできるようにするパターン。組織全体のCloudTrailと組み合わせればマルチアカウントにも拡張できる。
