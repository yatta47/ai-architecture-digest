---
type: announcement
title: オープンウェイトモデルKimi K3をUnity AI Gateway経由で統一ガバナンス下に提供
title_original: Kimi K3 from Moonshot AI is now available on Databricks through Unity AI Gateway
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- multi-model-routing
- llm-gateway
- cost-optimization
components:
- Kimi K3
- Unity AI Gateway
- Databricks Foundation Model API
- Unity Catalog
- Agent Bricks
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/kimi-k3-moonshot-ai-now-available-databricks-through-unity-ai-gateway
published_at: '2026-08-06'
---

## 概要

DatabricksはMoonshot AIのオープンウェイトモデルKimi K3を、Unity AI Gatewayによる統一APIとガバナンス、ゼロデータリテンションのもとでFoundation Model APIから利用可能にした。既存の商用モデル(Claude・GPT・Gemini)と同じアクセス権限・コスト制御・監査ログの枠組みでKimi K3を扱えるため、コーディングやドキュメント処理などのタスクにモデルをロックインなく使い分けられるとしている。

## 設計のポイント

- オープンウェイトモデルも商用モデルと同一のガバナンス・監査・支出制御の対象にし、モデル追加のたびにガバナンスを作り直さない
- レイクハウス内でモデルをホストし、Unity Catalog経由で企業データに直接根拠づけることで汎用的な学習知識との差別化を図る
- タスクごとに異なるモデル(低コストのコーディング用、高精度が必要な分析用など)をインテリジェントルーティングで使い分ける

## 使いどころ

- 複数プロバイダのモデルを併用しつつガバナンスを一元化したいエンタープライズのプラットフォームチーム
- 継続稼働するコーディングエージェントや大量ドキュメント処理など、コスト面でこれまで難しかったワークロードを実用化したい場合
