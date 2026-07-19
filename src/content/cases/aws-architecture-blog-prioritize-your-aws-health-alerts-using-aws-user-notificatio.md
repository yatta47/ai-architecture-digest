---
type: guidance
title: AWS Health通知を重要度別に振り分けて運用アラート疲れを防ぐ
title_original: Prioritize your AWS Health alerts using AWS User Notifications
ai_relevant: false
industry: cross-industry
cloud:
- aws
patterns: []
components: []
outcome:
  type: reliability
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/prioritize-your-aws-health-alerts-using-aws-user-notifications/
published_at: '2026-07-16'
---

## 概要

AWS Healthが発する未分類のイベントストリームを、AWS User Notificationsを使って「重要（即時通知）」と「情報（5分バッチ）」の2階層に振り分けるCloudFormationソリューション。監視対象サービスを絞り込むフィルタと優先度分離を組み合わせることで、運用チームが本当に重要な障害通知を見逃すリスクを減らす。
