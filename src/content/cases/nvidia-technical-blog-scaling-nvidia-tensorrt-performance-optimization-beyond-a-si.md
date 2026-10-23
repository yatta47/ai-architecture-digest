---
type: guidance
title: TensorRTのGlobal Performance Tunerによるビルドルート探索と精度制約付きチューニング
title_original: Scaling NVIDIA TensorRT Performance Optimization Beyond a Single Build Route with the Global Performance Tuner,
  Part 2
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
components:
- NVIDIA TensorRT 11.1
- trtexec
- Global Performance Tuner
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/scaling-nvidia-tensorrt-performance-optimization-beyond-a-single-build-route-with-the-global-performance-tuner-part-2/
published_at: '2026-10-23'
---

## 概要

TensorRT 11.1のGlobal Performance Tunerは、コンパイラノブの組み合わせを探索可能なビルドルートとして表し、候補をビルド・計測して最速のエンジンを選ぶ。精度を制約として扱い、10ワークロードでデフォルト比1.14〜1.63倍の高速化を得た。

## 設計のポイント

- スケジューリング戦略を明示的なビルドルートとして表現し、200超のノブの探索空間をAPIで列挙できる。
- 精度は候補のフィルタ制約、性能は順位付け基準として分離している。
- tuningCacheFileと--continueで探索を途中再開でき、モデル・形状・GPU変更時に再チューニングする。

## 使いどころ

- モデルごとに推論エンジン性能を詰めたい推論基盤担当者。
- 精度劣化なしで最適化したい本番推論環境。
