---
type: guidance
title: メッセージ重複配信に耐えるIdempotent Consumerパターン
title_original: Idempotent Consumer pattern
ai_relevant: false
industry: cross-industry
cloud:
- azure
patterns: []
components: []
outcome:
  type: reliability
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/idempotent-consumer
published_at: '2026-08-15'
---

## 概要

Azure Service BusやKafkaなどのat-least-once配信メッセージブローカーは同一メッセージを複数回配信しうるため、コンシューマ側で重複を検知・無視する設計が必要になる。安定した識別子をデデュープキーとして永続ストアに記録し、ビジネス処理とマーカー記録を単一トランザクションでコミットすることで、実質的にexactly-once処理を実現する。
