---
type: guidance
title: Cosmos 3 Edgをポストトレーニングしてロボットをオンデバイス制御する
title_original: Post-Train NVIDIA Cosmos 3 Edge for On-Device Robot Control
company: NVIDIA
industry: manufacturing
cloud:
- on-prem
patterns:
- fine-tuning
- inference-optimization
components:
- NVIDIA Cosmos 3 Edge
- NVIDIA Jetson Thor
- NVIDIA Nemotron
- LeRobotDataset
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/post-train-nvidia-cosmos-3-edge-for-on-device-robot-control/
published_at: '2026-08-18'
---

## 概要

物理世界データで事前学習された40億パラメータの世界モデルCosmos 3 Edgeを、ロボットアーム操作タスク向けにポストトレーニングし、データセンターGPUを介さずNVIDIA Jetson Thor上でクローズドループ推論させるチュートリアル。アクションチャンクを先読み生成することで約1.53秒の推論時間で2.13秒分の連続動作を維持し、閉ループ評価で22.9%の成功率を達成した。

## 設計のポイント

- 物理相互作用の事前知識を持つ世界基盤モデルを出発点にすることで、タスク固有デモからすべての物理関係を学習させる必要をなくす
- 次のアクションチャンクを現在の実行が終わる前に生成しておく先読み方式で、オンデバイスでも連続的な動作を維持する
- デバイスメモリと制御レイテンシという2つの実運用制約を明示的な設計目標としてポストトレーニング設定に落とし込む

## 使いどころ

- データセンターGPUへのオフロードなしにロボットアーム操作を実行したいエッジロボティクス開発者
- Franka/UR/WidowXなど複数のロボット embodiment に世界モデルを適用したいチーム
- オンデバイス推論のレイテンシと精度のトレードオフを検証したいロボット制御エンジニア
