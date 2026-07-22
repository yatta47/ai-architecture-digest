---
type: guidance
title: オーケストレータに頼らないサービス連携:コレオグラフィパターンによる分散ワークフロー設計
title_original: Choreography pattern
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
source_url: https://learn.microsoft.com/en-us/azure/architecture/patterns/choreography
published_at: '2026-04-02'
---

## 概要

中央のオーケストレータがすべてのサービス呼び出しを仲介する構成は、単一障害点や性能ボトルネックになりやすく、サービスの追加・削除のたびに連携ロジックの改修が必要になる。コレオグラフィパターンでは、メッセージブローカー上のパブリッシュ/サブスクライブ方式を用い、各サービスがメッセージを購読して自律的に処理し成功・失敗を応答することで、中央集権的な調整役なしにワークフローを分散実行する。並行して処理できる操作には適するが、サービス間に処理順序の依存がある場合は設計が複雑になり、失敗時の補償処理(コンペンセーティングトランザクション)の実装も必要になる。
