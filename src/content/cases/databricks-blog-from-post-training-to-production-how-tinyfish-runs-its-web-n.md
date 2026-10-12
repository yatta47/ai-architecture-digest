---
type: case
title: TinyFishがDatabricks上でWebネイティブモデルを学習・評価・配信
title_original: 'From post-training to production: how TinyFish runs its web-native model on Databricks AI Runtime'
company: TinyFish
industry: cross-industry
cloud:
- multi-cloud
patterns:
- fine-tuning
- eval
- llmops
- ai-agent
components:
- Databricks AI Runtime
- MLflow
- Databricks Model Serving
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/post-training-production-how-tinyfish-runs-its-web-native-model-databricks-ai-runtime
published_at: '2026-10-09'
---

## 概要

TinyFishはWebエージェント用の専用モデルを、Databricks AI RuntimeのマネージドGPUでSFTとDPOにより後学習し、MLflowで評価、Model Servingで配信している。2,178件の社内ベンチでタスク成功率は77.6%、直近15日間では1実行当たり約0.088ドルの配信コストだった。

## 設計のポイント

- 個々の応答でなく、エージェント全体がタスクを完了したかをLLM審査員が依頼・行動履歴・最終結果から判定する。
- 学習・評価・配信を同一基盤にまとめ、本番のエージェント挙動から後学習、デプロイへ継続的につなげる。
- 検索のリランカーやクエリ書き換えモデルも同じ基盤で配信する。

## 使いどころ

- Webエージェントなど専用モデルを自社で育てて運用したいAI基盤チーム。
- エンドツーエンドのタスク成功率でgo/no-go判断をしたい場面。
