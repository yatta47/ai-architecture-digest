---
type: guidance
title: Agents SDK組み込みトレーシングによるエージェント実行の可視化とデバッグ
title_original: Tracing
industry: cross-industry
cloud: []
patterns:
- ai-agent
components:
- OpenAI Agents SDK
- Traces dashboard
outcome:
  type: reliability
source_id: openai-docs
source_name: OpenAI Docs
source_url: https://openai.github.io/openai-agents-python/tracing/
published_at: '2025-07-21'
---

## 概要

Agents SDKはLLM生成・ツール呼び出し・ハンドオフ・ガードレール・カスタムイベントを含むエージェント実行の記録を自動収集するトレーシング機能をデフォルトで備え、Tracesダッシュボードで開発時・本番時のワークフローをデバッグ・可視化・監視できる。トレースはworkflow_name・trace_id・group_id・metadataなどで構成されるSpanの集合として表現される。

## 設計のポイント

- トレーシングはデフォルト有効で、環境変数・コード・実行単位のRunConfigという3つの粒度で無効化できる。
- Zero Data Retention（ZDR）ポリシー下ではトレーシング自体が利用できないという制約がある。
- group_idで同一会話スレッドの複数トレースを紐付けられるため、マルチターンのデバッグに活用できる。

## 使いどころ

- 複数エージェント・ツール呼び出し・ハンドオフが絡む複雑なワークフローの本番運用時デバッグ。
- ガードレールやカスタムイベントを含めたエンドツーエンドの実行監視。
