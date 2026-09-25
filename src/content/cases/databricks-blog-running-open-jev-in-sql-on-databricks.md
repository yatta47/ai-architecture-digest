---
type: guidance
title: Databricks上で決定モデルOpen-JevをSQLから実行
title_original: Running Open Jev in SQL on Databricks
company: Databricks
industry: cross-industry
cloud:
- multi-cloud
patterns:
- inference-optimization
- text-to-sql
- cost-optimization
components:
- Databricks Model Serving
- Databricks AI Runtime
- ai_query
- Lakeflow
- SemIf-OpenJev
- Express Deployments
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/running-open-jev-sql-databricks
published_at: '2026-09-24'
---

## 概要

選択肢から確率付きの判断を返す決定モデルSemIf-OpenJevを、Databricksのサーバーレスa GPUとModel Servingで配信し、ai_queryからSQLやLakeflowジョブで呼ぶ方法を示す。ホテルレビューの良し悪し分類を例にノートブックで再現できる。

## 設計のポイント

- Express DeploymentsでGPUのModel Servingエンドポイントを自動作成する。
- ai_queryは任意のカスタムAPI形式に対応し、チャット形式でなくても呼べる。
- ガバナンス下のデータにモデルを直接当て、構造化された列として結果を得る。

## 使いどころ

- 大量のテキスト分類を低コストで回したいデータチーム。
- LLMを使わず高速な判断モデルで分類したい場面。
