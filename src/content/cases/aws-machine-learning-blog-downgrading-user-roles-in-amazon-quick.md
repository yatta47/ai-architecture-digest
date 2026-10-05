---
type: guidance
title: Amazon Quickのユーザーロールを降格して最小権限とコストを最適化する手順
title_original: Downgrading user roles in Amazon Quick
ai_relevant: false
company: AWS
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/downgrading-user-roles-in-amazon-quick/
published_at: '2026-10-05'
---

## 概要

Amazon Quickのユーザー管理で、AdminやAuthorからReaderへロールを降格する手順を解説する。最小権限の徹底に加え、ロール別課金を踏まえて閲覧のみのユーザーをReaderにすることでコスト削減につながる。
