---
type: guidance
title: 1兆パラメータ級事前学習をビット単位で再現可能にする手法
title_original: Scale Bitwise-Deterministic Pretraining with NVIDIA Megatron Core
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- inference-optimization
components:
- NVIDIA Megatron Core
- Nemotron
- Megatron-LM
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/scale-bitwise-deterministic-pretraining-with-nvidia-megatron-core/
published_at: '2026-10-09'
---

## 概要

Megatron Coreで大規模事前学習をビット単位で決定的にする方法を解説する。ランごとのテンソルフィンガープリントで非決定性の発生箇所を絞り込み、カーネルの出力スロット分離や固定リダクション順で、2,432GPUでのオーバーヘッドを約2%に抑えた。

## 設計のポイント

- 各ステップの数値指標を完全精度でフィンガープリント化し、2回の実行を比較して最初の不一致ステップを特定する。
- エンドツーエンドからフェーズ、モジュール、演算、カーネルへと段階的にトレースを絞る。
- トレースはランクごとにファイルへ書き、集団通信を足さないことで競合の隠蔽を避ける。
- 並列性を保ったままカーネルの書き込み先分離と固定順リダクションで決定性を回復する。

## 使いどころ

- ロススパイクの再現と原因切り分けをしたい大規模事前学習チーム。
- チェックポイント復帰後も同一の学習軌跡を保証したい基盤運用者。
