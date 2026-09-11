---
type: announcement
title: SageMaker HyperPodでモデル/コンテナをノードに事前キャッシュしコールドスタートを解消
title_original: Reduce inference cold starts on Amazon SageMaker HyperPod with model caching
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- model-caching
components:
- Amazon SageMaker HyperPod
- Amazon ECR
- Amazon S3
- Amazon FSx for Lustre
- HuggingFace Hub
- vLLM
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/reduce-inference-cold-starts-on-amazon-sagemaker-hyperpod-with-model-caching/
published_at: '2026-09-10'
---

## 概要

SageMaker HyperPodに、コンテナイメージとモデル重みをクラスタノードのローカルNVMeへ事前ロードするモデルキャッシュ機能が追加された。DeepSeek-R1(600GB超)のような大規模モデルで30分以上かかっていたPod起動を数秒に短縮する。

## 設計のポイント

- 重みキャッシュとイメージキャッシュを独立した機能として分離し、必要に応じて個別に有効化できる
- Preferred schedulingを採用し、キャッシュが無いノードに配置されても通常のダウンロードにフォールバックするため障害にならない
- CRD(ModelDataCacheConfig/ModelImageCache)でキャッシュのライフサイクルを管理し、モデル切替時はゼロダウンタイムで新旧キャッシュを入れ替える

## 使いどころ

- 数百GB級の大規模モデル(DeepSeek-R1等)をオートスケールで頻繁に起動するワークロード
- トラフィック急増時にスケールアウトの実効レイテンシを縮めたい推論基盤チーム
