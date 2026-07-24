---
type: guidance
title: 非同期メッセージングにおけるメッセージエンコーディング設計のベストプラクティス
title_original: Best practices for message encoding
ai_relevant: false
industry: cross-industry
cloud: []
patterns: []
components: []
outcome:
  type: speed
source_id: azure-architecture-center
source_name: Azure Architecture Center
source_url: https://learn.microsoft.com/en-us/azure/architecture/best-practices/message-encode
published_at: '2025-05-02'
---

## 概要

非同期メッセージングでペイロードをどう符号化するかについて、JSON/YAMLのようなテキスト形式とAvro/Protobufのようなバイナリ形式のトレードオフを解説する。可読性、暗号化、サイズ、スキーマ管理の観点から適切なエンコーディング形式を選ぶ指針を示す。
