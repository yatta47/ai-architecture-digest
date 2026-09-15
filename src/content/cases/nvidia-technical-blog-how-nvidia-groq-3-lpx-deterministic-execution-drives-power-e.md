---
type: case
title: 決定的実行モデルで電力ガードバンドを削減しAIファクトリーの性能/ワットを最大化する設計
title_original: How NVIDIA Groq 3 LPX Deterministic Execution Drives Power-Efficient High-Interactivity Inference on NVIDIA
  Vera Rubin
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- gpu-fleet-reliability
- inference-optimization
components:
- NVIDIA Vera Rubin NVL72
- NVIDIA Groq 3 LPX
- NVIDIA DSX MaxLPS
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-nvidia-groq-3-lpx-deterministic-execution-drives-power-efficient-high-interactivity-inference-on-nvidia-vera-rubin/
published_at: '2026-09-15'
---

## 概要

NVIDIA Vera Rubinプラットフォームは性能/ワットを最重要指標とし、ファクトリー単位でラック間の電力を融通するDSX MaxLPSで同一電力予算内のGPU数を最大40%増やし、ラック単位のキャパシタとIntelligent Power Smoothingでバースト電力を吸収する。高インタラクティブ推論向けのGroq 3 LPXは決定的実行モデルで電流需要を予測しPEP/CPSで電圧ガードバンドを削減、GB200 NVL72比で最大35倍のスループット/メガワットを達成。

## 設計のポイント

- LPUコンパイラがサイクル単位で計算とデータ移動のスケジュールを事前生成し電流需要曲線を予測可能にする
- 予測可能な需要曲線を使いPreemptive PowerとClock Period Synthesisで電圧ガードバンドを削減し、実ワークロードに使える電力比率を高める
- ファクトリーレベルではDSX MaxLPSがラック間で電力をシフトしストランデッド電力を回収する

## 使いどころ

- 電力予算の制約下でGPU台数とトークンスループットを最大化したいAIファクトリー運用者
- 長コンテキスト・高インタラクティブ推論を低レイテンシで提供したい推論基盤チーム
