---
type: guidance
title: Ray Train DLCとEFAでEKS上の分散学習を行う手順
title_original: Distributed training with Ray Train DLCs and EFA on EKS
company: Amazon Web Services
industry: cross-industry
cloud:
- aws
patterns:
- parallel-execution
- fine-tuning
- gpu-fleet-reliability
components:
- Ray Train
- KubeRay
- Amazon EKS
- Elastic Fabric Adapter
- PyTorch FSDP
outcome:
  type: speed
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/distributed-training-with-ray-train-dlcs-and-efa-on-eks/
published_at: '2026-10-28'
---

## 概要

AWS提供のRay Train DLCをそのまま使い、KubeRayでEKS上にRayクラスタを構築して、Qwen2.5-1.5BをFSDPで8GPUに分散してファインチューニングする例を示す。イメージのビルドは不要で、EFAによるノード間通信もそのまま使える。

## 設計のポイント

- CUDA、PyTorch、NCCL、EFAなどを揃えたイメージをDLCとして受け取り、自前ビルドと更新の手間をなくす。
- RayClusterのマニフェスト1つでheadとworkerの構成を宣言し、KubeRayに維持させる。
- インスタンス、GPU数、通信方式、追加パッケージはイメージの外から設定する。

## 使いどころ

- Kubernetes上でマルチノードのLLM学習を素早く立ち上げたいチーム。
- 学習用コンテナイメージの保守を減らしたい基盤担当者。
