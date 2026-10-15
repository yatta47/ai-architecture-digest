---
type: case
title: FactSetのText-to-FormulaをファインチューニングとAI Runtimeで高速更新
title_original: How FactSet cut model training and deployment from days to hours on Databricks AI Runtime
company: FactSet
industry: financial-services
cloud: []
patterns:
- fine-tuning
- text-to-sql
- rag
- llmops
components:
- Databricks AI Runtime
- Llama
- FactSet Query Language
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/how-factset-cut-model-training-and-deployment-days-hours-databricks-ai-runtime
published_at: '2026-10-14'
---

## 概要

FactSetは自然言語をFQL式に変換するText-to-FormulaでRAGが品質の壁に当たり、ファインチューニングした公開モデルをCompound AIに取り入れた。2〜3週ごとの再学習をAI Runtimeのサーバーレスで行い、準備から展開までを数日から数時間に短縮した。

## 設計のポイント

- RAGで頭打ちの複雑な式生成はFQLの構造を学習させて補う
- 再学習が定常化するため、GPU環境構築のオーバーヘッドを排除する
- モデルごとに必要な計算構成が変わるためGPUを固定しない

## 使いどころ

- ドメイン固有言語への変換で検索拡張の限界に当たった金融系チーム
- 定期再学習を回すMLOps担当
