---
type: guidance
title: Flex processingで評価・非同期処理のAPIコストをBatch料金水準まで削減
title_original: Flex processing
industry: cross-industry
cloud: []
patterns:
- cost-optimization
- inference-optimization
components:
- Responses API
- Chat Completions
outcome:
  type: cost
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://platform.openai.com/docs/guides/flex-processing
published_at: '2025-07-22'
---

## 概要

Flex processingはservice_tierをflexに設定することでResponses/Chat CompletionsのリクエストをBatch API相当の低価格で処理できるモードで、応答が遅くなったり一時的に利用不可になる代わりにコストを抑えられる。モデル評価やデータ拡充、非同期ワークロードなど本番外・低優先度タスクに向く。

## 設計のポイント

- service_tier: "flex" を指定するだけで既存のResponses/Chat Completions呼び出しに適用でき、プロンプトキャッシュの割引も併用できる。
- レイテンシが増えるためタイムアウトをデフォルトより長く（例: 15分）設定する必要がある。
- 対象モデルは限定されるため、事前にpricingページで対応状況を確認する。

## 使いどころ

- モデル評価やデータ拡充など、応答速度が問われない非同期バッチ処理。
- 本番トラフィックとは別に低優先度のバックグラウンドジョブのAPIコストを下げたい場合。
