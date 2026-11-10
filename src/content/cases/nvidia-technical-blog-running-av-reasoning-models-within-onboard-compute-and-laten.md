---
type: announcement
title: 車載向け適応推論VLA「Alpamayo 2 Edge」と報酬モデルによる改善ループ
title_original: Running AV Reasoning Models Within Onboard Compute and Latency Limits
company: NVIDIA
industry: other
cloud: []
patterns:
- inference-optimization
- reinforcement-learning
- eval
components:
- NVIDIA Alpamayo 2 Edge
- NVIDIA DRIVE AGX Thor
- AlpaGym
- AlpaJudge
- TensorRT
- NVIDIA Cosmos 3 Edge
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/running-av-reasoning-models-within-onboard-compute-and-latency-limits/
published_at: '2026-11-10'
---

## 概要

NVIDIAは車載の計算・遅延制約内で動く2B規模の適応推論VLAモデルAlpamayo 2 Edgeを紹介した。必要な時だけ推論(Chain-of-Causation)を生成し、閉ループRLで性能を48.9%改善、TensorRT等でDRIVE AGX Thor上160〜190msの遅延を実現する。

## 設計のポイント

- 推論を必要時のみ生成し、トークン生成と計算を節約する。
- 人手で校正した評価モデルAlpaJudgeを評価と報酬の両方に使い、学習データ選別とRL後学習に接続する。
- ターゲットハードウェア上で推論最適化し、遅延を検証する。

## 使いどころ

- エッジで推論モデルを動かす自動運転・ロボティクス開発
- 推論品質を報酬化して後学習したいチーム
