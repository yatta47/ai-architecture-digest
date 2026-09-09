---
type: case
title: TorchServe終了に備えたRay Serve Deep Learning Containersへの移行
title_original: Simplify and support your TorchServe workloads using Ray Serve Deep Learning Containers
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- inference-optimization
- unified-runtime
components:
- Amazon EKS
- Ray Serve
- AWS Deep Learning Containers
- Amazon EC2
- Amazon SageMaker
- PyTorch
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/simplify-and-support-your-torchserve-workloads-using-ray-serve-deep-learning-containers/
published_at: '2026-09-09'
---

## 概要

TorchServeがメンテナンス終了となり脆弱性・互換性対応を利用者が自前で負う状況を受け、AWSはRay Serve用のDeep Learning Container（DLC）を新設した。GPU/CUDA/PyTorch/Ray Serveをテスト済みの組み合わせで提供し、Qwen3-VLのような視覚言語モデルをAmazon EKS上のGPUノードでHTTPエンドポイントとして配信する構成を示す。

## 設計のポイント

- フレームワーク・GPUスタック・サービング層をAWSがビルド時に検証済みの単一イメージにまとめ、バージョンドリフトと脆弱性対応をチーム側から切り離す。
- モデルの提供コードはDockerイメージに焼き込まず ConfigMap 経由で注入し、イメージを再ビルドせずにサービングロジックを変更可能にする。
- @serve.deploymentデコレータとray_actor_options={'num_gpus':1}でGPUスケジューリングを宣言的に指定し、モデルアーカイバや独自ハンドラ階層を廃する。
- 単一ノード・単一GPUの最小構成から始め、マルチノード分散配信が必要な場合はKubeRayで水平方向に拡張する設計とする。

## 使いどころ

- TorchServeで本番推論を運用しておりメンテナンス終了に伴う脆弱性放置リスクを避けたいチーム。
- GPU/CUDA/フレームワークのバージョン整合を自前で管理する運用コストを削減したいMLプラットフォームチーム。
- 視覚言語モデルなどのマルチモーダルモデルをKubernetes上でHTTP推論エンドポイントとして提供したい場合。
