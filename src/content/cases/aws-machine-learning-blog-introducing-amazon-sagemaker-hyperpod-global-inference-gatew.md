---
type: announcement
title: リージョンとクラスタを横断するHyperPodのグローバル推論ゲートウェイ
title_original: 'Introducing Amazon SageMaker HyperPod Global Inference Gateway: One endpoint across Regions and clusters'
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- llm-gateway
- inference-optimization
- disaster-recovery
components:
- Amazon SageMaker HyperPod
- AWS PrivateLink
- AWS IAM
- SigV4
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-global-inference-gateway-one-endpoint-across-regions-and-clusters/
published_at: '2026-11-20'
---

## 概要

複数のHyperPodクラスタやリージョンに分散したGPUを、1つのSageMaker管理エンドポイントで束ねるGlobal Inference Gatewayを発表した。最適なクラスタを選んで転送し、障害時は自動フェイルオーバーする。クラスタ内のポッド選択は従来のInference Gatewayが担う。

## 設計のポイント

- クラスタ間とクラスタ内の二層でルーティングを分け、それぞれ責務を分離している。
- KVキャッシュ使用率やキュー深さなどのリアルタイム信号でGPU状況を見て振り分ける。
- SigV4とIAM認証、PrivateLink経由で、既定で閉域に保つ。

## 使いどころ

- ピーク時に一部クラスタだけが詰まる推論サービスを平準化したいとき。
- クライアント側のエンドポイント管理とフェイルオーバーをなくしたいとき。
