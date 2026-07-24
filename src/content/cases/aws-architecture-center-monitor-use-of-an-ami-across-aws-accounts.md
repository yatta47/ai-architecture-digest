---
type: guidance
title: マルチアカウント間で共有AMIの利用状況を監視する仕組み
title_original: Monitor use of a shared Amazon Machine Image across multiple AWS accounts
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-center
source_name: AWS Architecture Center
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/monitor-use-of-a-shared-amazon-machine-image-across-multiple-aws-accounts.html?did=pg_card&trk=pg_card
published_at: '2023-09-09'
---

## 概要

複数のAWSアカウント間で共有されるAMIが非推奨化・登録解除・共有停止された際、利用中のインスタンスやテンプレートで障害が起きるリスクを防ぐため、EventBridge・DynamoDB・Lambda・SESを用いてAMIの共有・利用状況をイベント駆動で追跡し、影響がある場合はメール通知する構成を解説。
