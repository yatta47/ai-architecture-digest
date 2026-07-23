---
type: announcement
title: Databricks、AWS IAM委任によるS3自動接続機能を提供開始
title_original: Connect Amazon S3 data to Databricks with delegated IAM permissions
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/connect-amazon-s3-data-databricks-delegated-iam-permissions
published_at: '2026-07-23'
---

## 概要

DatabricksはAWS IAMの一時的委任を用いて、S3バケットとUnity Catalogの外部ロケーション接続を数クリックで自動設定できる新機能を発表した。従来は140行のIAM信頼ポリシー作成やCloudFormationテンプレートのデプロイなど手作業が必要だったが、最小権限のIAMロールと外部ロケーションを自動生成し、認可は時限付きで自動失効する。
