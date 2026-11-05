---
type: opinion
title: 企業がオープンウェイトモデルを使う理由とUnity AI Gateway
title_original: The enterprise case for open-weight models on Databricks
company: Databricks
industry: cross-industry
cloud: []
patterns:
- llm-gateway
- multi-model-routing
- cost-optimization
- guardrails
components:
- Unity AI Gateway
- Databricks
- GLM 5.2
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/enterprise-case-open-weight-models-databricks
published_at: '2026-11-04'
---

## 概要

単一の最先端モデル提供元に依存する戦略を見直す7つの圧力（費用対効果、順位の変動、ガードレールによる拒否、データ保持方針の変化、ガバナンス、ハーネスの影響など）を挙げ、オープンウェイトモデルを選択肢に加える意義を述べた記事。Unity AI Gatewayが多種のモデルを1つの統制されたAPIで提供する。

## 設計のポイント

- ゲートウェイでオープンウェイト・最先端・外部モデルを1つのAPIに集約し、ルーティング、フォールバック、予算管理を行う。
- モデル順位が変わっても乗り換えられるよう、特定の提供元に固定しない。
- ハーネスで性能が大きく変わるため、モデルとハーネスをセットで評価する。
- 入出力やエージェント行動の検索可能な記録を残し、評価とガバナンスに使う。

## 使いどころ

- モデル提供元のポリシー変更や費用に備えたいAI基盤担当
- 防御用途の解析などでガードレール拒否を避けたい組織
