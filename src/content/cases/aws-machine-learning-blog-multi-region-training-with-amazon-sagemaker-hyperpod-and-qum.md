---
type: case
title: HyperPodとQumuloによるリージョン跨ぎ学習データ配置
title_original: Multi-Region training with Amazon SageMaker HyperPod and Qumulo
company: Qumulo
industry: cross-industry
cloud:
- aws
patterns:
- cost-optimization
- inference-optimization
- gpu-fleet-reliability
components:
- Amazon SageMaker HyperPod
- Cloud Native Qumulo
- Qumulo Cloud Data Fabric
- NeuralCache
- Amazon EKS
- Amazon EC2 P5
outcome:
  type: cost
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/multi-region-training-with-amazon-sagemaker-hyperpod-and-qumulo/
published_at: '2026-09-25'
---

## 概要

計算資源とは別リージョンにある学習データを、複製せずQumuloのCloud Data Fabricで参照しながらHyperPodで学習する構成。60msの遅延下でも短いウォームアップ後にハブと同等の約116サンプル/秒に収束した。

## 設計のポイント

- ハブに単一の正本を置き、スポークへPOSIX名前空間として投影する。
- NeuralCacheがデータローダのアクセスパターンを学習して先読みし、読み取りの94〜96%をローカルNVMeで処理する。
- ウォームアップは最初の100〜150バッチで、長時間学習では無視できる。

## 使いどころ

- GPU確保のためデータと別リージョンで学習したいチーム。
- ペタバイト級データの複製コストを避けたい場面。
