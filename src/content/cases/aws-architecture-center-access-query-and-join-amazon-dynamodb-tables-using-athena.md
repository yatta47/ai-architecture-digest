---
type: guidance
title: AthenaでDynamoDBテーブルをSQLクエリ・結合するパターン
title_original: Access, query, and join Amazon DynamoDB tables using Athena
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: productivity
source_id: aws-architecture-center
source_name: AWS Architecture Center
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/access-query-and-join-amazon-dynamodb-tables-using-athena.html?did=pg_card&trk=pg_card
published_at: '2022-07-30'
---

## 概要

Amazon Athena DynamoDBコネクタをLambda経由でセットアップし、コードを書かずにDynamoDBテーブルをSQLで直接クエリ・結合できるようにする構成を解説。テーブルサイズが大きい場合のコスト増やSCAN操作を避けるべき注意点など運用上の勘所も示す。
