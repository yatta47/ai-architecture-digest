---
type: guidance
title: メッセージキューで順序保証と並列処理を両立するSequential Convoyパターン
title_original: Sequential Convoy pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/sequential-convoy
published_at: '2026-06-24'
---

## 概要

関連するメッセージをカテゴリキーでグループ化し、グループ内はFIFOで厳密な順序を保ちながらグループ間は並列に処理するSequential Convoyパターンを解説する。単一コンシューマは順序を保てるがスケールせず、複数コンシューマは並列に処理できるがグループ内の順序が崩れるというトレードオフを、メッセージブローカーによるカテゴリ単位のパーティショニングで解決する。Azureでは Azure Service Bus のメッセージセッション機能がこのパターンを標準で実装している。
