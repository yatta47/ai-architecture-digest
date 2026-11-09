---
type: announcement
title: Unity Catalogテーブルを直接GPUへ流すPyTorchデータローダ UCDataset
title_original: Accelerate GPU training on Unity Catalog tables with UCDataset
company: Databricks
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- cost-optimization
components:
- Unity Catalog
- UCDataset
- PyTorch
- Databricks AI Runtime
outcome:
  type: speed
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/accelerate-gpu-training-unity-catalog-tables-ucdataset
published_at: '2026-11-09'
---

## 概要

DatabricksはUnity Catalogのテーブルを分散PyTorch学習へ直接ストリーミングするUCDatasetをベータ公開した。エクスポートしたParquetを読む場合に比べて学習時間を10倍短縮し、ガバナンスも自動で効く。

## 設計のポイント

- コピーやエクスポートを介さず、クラウドストレージ上のテーブルファイルを直接読み込む
- 一致した行を全GPUとワーカーに均等に分割し、重複や欠落を防ぐ
- 実行ID権限でUnity Catalogの権限をそのまま適用する

## 使いどころ

- 学習前のParquetエクスポートが負担になっているML基盤チーム
- 大規模な特徴量テーブルで複数GPU学習を行う場面
- 学習データの系譜とアクセス制御を保ちたい組織
