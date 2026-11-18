---
type: guidance
title: 表形式基盤モデル(TFM)の仕組みと選定、Databricks AI Runtimeでの評価・微調整
title_original: Tabular Foundation Models on Databricks AI Runtime
company: Databricks
industry: cross-industry
cloud: []
patterns:
- fine-tuning
- eval
- inference-optimization
components:
- Databricks AI Runtime
- MLflow
- Unity Catalog
- TabPFN
- TabICL
- Mitra
- KumoTabular
- TabFM
outcome:
  type: productivity
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/tabular-foundation-models-databricks-ai-runtime
published_at: '2026-11-16'
---

## 概要

事前学習済みの表形式基盤モデル(TFM)は、タスクごとの学習なしにインコンテキスト学習で予測でき、個別モデルの開発・再学習の負担を減らす。本記事は TabPFN から TabICL 系の行圧縮までの仕組み、主要モデルの規模とライセンス、精度・遅延・GPUメモリ・コストを既存ベースラインと比較する観点を整理し、Databricks AI Runtime のマネージドGPUで実験・微調整する方法を示す。

## 設計のポイント

- ラベル付き行を文脈として渡し、1回の順伝播で予測するインコンテキスト学習により再学習パイプラインを不要にする。
- 行ごとに少数トークンへ圧縮して標本間アテンションの計算量を抑える設計が主流になっている。
- 採用前に自社データで精度・遅延・GPUメモリ・コストを既存ベースラインと比較する。
- 商用利用可否などモデルごとのライセンスも選定条件に含める。

## 使いどころ

- 与信・解約予測・需要予測など多数の表データ予測タスクを抱えるMLチーム。
- モデルの保守・再学習コストを下げたい組織。
- マネージドGPU上でTFMを試験・微調整したい場面。
