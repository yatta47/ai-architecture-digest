---
type: guidance
title: SkyRLとHyperPodで行うVLMのマルチターンGRPO学習
title_original: Accelerate multimodal RL training with SkyRL on Amazon SageMaker HyperPod
company: AWS
industry: cross-industry
cloud:
- aws
patterns:
- reinforcement-learning
- fine-tuning
- gpu-fleet-reliability
components:
- Amazon SageMaker HyperPod
- Amazon EKS
- SkyRL
- Ray
- KubeRay
- vLLM
- Amazon FSx for Lustre
- Amazon Managed Grafana
- Qwen3-VL-8B
outcome:
  type: quality
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/accelerate-multimodal-rl-training-with-skyrl-on-amazon-sagemaker-hyperpod/
published_at: '2026-09-25'
---

## 概要

SkyRLをSageMaker HyperPodのRayクラスタ上で動かし、Qwen3-VL-8BをGRPOで視覚迷路タスク向けに学習させる手順を示す。SFTチェックポイントから迷路の解決率が43.75%から95%超に向上した。

## 設計のポイント

- 推論(vLLM)と学習(FSDP)を同一GPUにコロケーションし、LoRAアダプタをFSx for Lustre経由で同期する。
- HyperPodの自動ノード置換とチェックポイントで長時間RLの障害耐性を確保する。
- Managed Grafanaのダッシュボードで学習の挙動を可視化する。

## 使いどころ

- エージェント向けVLMのRL後学習を小規模クラスタで試したいチーム。
- 長時間RLジョブの耐障害運用を整えたい場面。
