---
type: case
title: Henry Schein Oneの歯科X線画像をリアルタイム品質検証するSageMaker AI基盤「Image Verify」
title_original: Real-time dental image verification with Amazon SageMaker AI at Henry Schein One
company: Henry Schein One
industry: healthcare
cloud:
- aws
patterns:
- multi-model-routing
- inference-optimization
- cost-optimization
components:
- Amazon SageMaker AI
- Amazon EKS
- AWS Cloud WAN
- Dentrix
- Dentrix Ascend
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/real-time-dental-image-verification-with-amazon-sagemaker-ai-at-henry-schein-one/
published_at: '2026-07-10'
---

## 概要

Henry Schein Oneは、歯科X線画像の品質不足による保険請求の却下（最大20%）を防ぐため、撮影直後にAmazon SageMaker AI上でリアルタイムに画質を1〜5段階でスコアリングする「Image Verify」を構築した。画像種別の分類→専門モデルによる品質評価→スコア集約という多段推論パイプラインを中央値1.4秒・P90 2.2秒で処理し、着想からわずか数カ月で1万拠点・1,100万枚超のX線処理へとスケールした。

## 設計のポイント

- 画像種別（バイトウィング/パノラマ/根尖など）を最初に分類し、種別ごとに専門化した品質評価モデルへルーティングする多段推論パイプラインを組む。
- SageMaker AIの非同期推論を採用し、キュー深度ベースのオートスケーリングでGPUワークロードの需要変動に対応する。
- GPUインスタンス世代を継続的にベンチマーク・移行(g6e→g7e)し、台数を削減しながらレイテンシも改善するコスト最適化を行う。
- 本番トラフィックに対するA/Bテストでゼロダウンタイムのデプロイを行い、日次で最適化を継続する。

## 使いどころ

- 撮影・検査の現場でその場フィードバックが必要な医療画像ワークフロー（再撮影の手戻りコストを削減したい現場）。
- 数万拠点規模でリアルタイムML推論をグローバルに展開したい企業（マルチリージョン・低レイテンシ要件）。
