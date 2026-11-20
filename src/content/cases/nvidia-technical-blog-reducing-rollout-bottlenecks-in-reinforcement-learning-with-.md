---
type: guidance
title: NVIDIA Dynamoで強化学習のロールアウトのボトルネックを減らす
title_original: Reducing Rollout Bottlenecks in Reinforcement Learning with NVIDIA Dynamo
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- reinforcement-learning
- inference-optimization
- gpu-fleet-reliability
components:
- NVIDIA Dynamo
- ModelExpress
- verl
- NeMo RL
- Slime
- prime-rl
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/reducing-rollout-bottlenecks-in-reinforcement-learning-with-nvidia-dynamo/
published_at: '2026-11-19'
---

## 概要

強化学習で使うロールアウト生成を、KV対応ルーティング、差分圧縮による重み配布、障害時の再ルーティングと復旧でDynamoが支える。verlやNeMo RLなど既存のRL基盤と統合できる。

## 設計のポイント

- KV対応ルーティングでキャッシュ再利用とワーカー負荷を両立する。
- 重みを圧縮した差分で配布し、GPU上の既存重みを再利用する。
- ワーカー障害時に健全な容量へ再ルーティングし、交換ワーカーは追いつかせる。

## 使いどころ

- 大規模なRL学習でGPUの無駄と待ち時間を減らしたい学習基盤チームに向く。
