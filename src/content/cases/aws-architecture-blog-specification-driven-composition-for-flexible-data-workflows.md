---
type: guidance
title: 仕様駆動コンポジションによる柔軟なデータパイプライン基盤
title_original: Specification-driven composition for flexible data workflows
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: speed
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/specification-driven-composition-for-flexible-data-workflows/
published_at: '2026-07-09'
---

## 概要

データパイプラインがスクリプトベースで肥大化し、変換ロジックの重複やガバナンス欠如が課題になる問題に対し、ワークフローの意図(仕様)と実装を分離する「仕様駆動コンポジション」パターンを提案する。AWS Lambda・Step Functions・S3・OpenSearch Serviceを用いたサーバーレス実装例を通じ、仕様・コンポーザー・ケーパビリティレジストリ・パイプラインの4要素で構成する方法を示す。
