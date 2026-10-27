---
type: guidance
title: S3アノテーションによるデータガバナンス
title_original: Data governance with annotations in Amazon S3
ai_relevant: false
company: AWS
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/data-governance-with-annotations-in-amazon-s3/
published_at: '2026-10-26'
---

## 概要

S3アノテーションでオブジェクトに分類や保持ポリシーなどのガバナンス情報を直接付与でき、コピーやレプリケーションでも維持され、Icebergテーブル経由でSQLでも検索できる。
