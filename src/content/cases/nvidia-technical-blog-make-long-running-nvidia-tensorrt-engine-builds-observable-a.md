---
type: guidance
title: TensorRTエンジンビルドを可視化・キャンセル可能にするIProgressMonitor API
title_original: Make Long-Running NVIDIA TensorRT Engine Builds Observable and Cancelable in Python or C++
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- llmops
- ci-cd
components:
- NVIDIA TensorRT
- IProgressMonitor
- NVIDIA NGC containers
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/make-long-running-nvidia-tensorrt-engine-builds-observable-and-cancelable-in-python-or-c/
published_at: '2026-07-22'
---

## 概要

NVIDIA TensorRTのIProgressMonitor APIを使うと、時間のかかるエンジンビルドの進捗をフェーズ単位で追跡し、ステップ境界でキャンセルできるようになる。Python/C++それぞれでphase_start・step_complete・phase_finishの3メソッドをオーバーライドするだけで実装でき、ターミナルやIDE、HTTPサービス、エージェントランタイムなど任意の場所に進捗を配信できる。これにより、長時間ビルドによる無駄なGPU時間やハングしたセッションを防げる。

## 設計のポイント

- TensorRTはモニタを複数の内部スレッドから呼び出すため、ロックによるスレッドセーフな状態管理を必須にする。
- phase_start/step_complete/phase_finishの3メソッドのみで、ネストしたフェーズを木構造として表現する設計にする。
- ビルドの継続可否を制御できるのはstep_completeの戻り値だけであり、キャンセルの反映はステップ境界に限られるという制約を前提に設計する。
- 進捗の描画・配信ロジックをビルドロジック本体から分離し、ターミナル・IDE・HTTPサービス・エージェントランタイムなど出力先を差し替え可能にする。

## 使いどころ

- 大規模モデルや新しいGPU SKU向けの長時間TensorRTビルドで、進捗が見えず待つべきか中断すべきか判断できない開発者向け。
- AIエージェントランタイムがモデルビルドを自動実行し、必要に応じてプログラム的に中断判断を行いたい場合。
- CI/CDパイプラインで長時間ビルドの詰まりを検知し、無駄なGPU時間を削減したい運用チーム向け。
- IDEや社内HTTPサービスからリアルタイムにビルド進捗をストリーミング表示したいツール開発者向け。
