---
type: case
title: 人手レビューを正解にしてai_extractの改善を測定する
title_original: 'From Spot Fixes to Measured Gains: Improving Document Extraction Accuracy with ai_extract and MLflow Prompt
  Registry'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- document-processing
- prompt-optimization
- eval
- human-in-the-loop
- llmops
components:
- ai_extract
- ai_parse_document
- MLflow Prompt Registry
- Lakeflow
- Lakebase
- Genie Code
outcome:
  type: quality
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/spot-fixes-measured-gains-improving-document-extraction-accuracy-aiextract-and-mlflow-prompt
published_at: '2026-10-27'
---

## 概要

約40項目を多数のPDFレイアウトから抽出する発注書処理で、スポット修正が全体の誤りを9%増やした経験から、レビュー承認値を正解に評価する仕組みを作った。プロンプトとスキーマをMLflow Prompt Registryで版管理し、昇格前に評価する。

## 設計のポイント

- レビュー担当者の承認結果を固定の評価データセットにして、項目ごとの精度を測る。
- プロンプトとスキーマをパイプラインコードから切り出し、エイリアスで展開・ロールバックする。
- 項目単位の改善が全体を悪化させないか、実行ごとのばらつきも見て判断する。

## 使いどころ

- 多様なレイアウトの帳票から構造化データを抽出し、改善を継続したいチーム。
- LLM抽出の変更を安全に本番へ出したいデータ基盤チーム。
