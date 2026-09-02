---
type: guidance
title: 投機的デコーディングによるLLM推論高速化のためのAIモデル共同設計ガイド
title_original: Co-Designing AI Models Using Speculative Decoding for Faster LLM Inference
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- reasoning-computation-separation
- fine-tuning
- eval
components:
- NVIDIA Model-Optimizer
- TensorRT-LLM
- Nemotron 3.5 Lightning
- SPEED-Bench
- EAGLE-3
- MTP
- DFlash
- DSpark
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/co-designing-ai-models-using-speculative-decoding-for-faster-llm-inference/
published_at: '2026-09-02'
---

## 概要

NVIDIAによるAIモデル共同設計シリーズ第3弾。小さなドラフトモデルが複数トークンを提案し、大きなターゲットモデルが並列に検証する投機的デコーディングでLLM推論を高速化する仕組みを解説し、ドラフト長・ドラフト機構を選ぶための5つの指針を示す。ドラフト機構の比較や、NVIDIA/Model-OptimizerでのEAGLE-3・DFlash・DSparkの学習例、専用ベンチマークSPEED-Benchも紹介している。

## 設計のポイント

- KVキャッシュ容量への負荷を増やさずにGEMMを演算律速領域へ押し上げるため、ドラフト長を増やす
- アテンションが支配的な場合はドラフト長を128/G-1に設定し、大きなドラフト長はアテンションカーネルのタイル境界(128)に合わせる
- 低レイテンシ環境では、受理長の伸びがドラフトコストに見合う範囲でのみドラフト長を増やす
- 外部ドラフトモデル・EAGLE-3・MTP・DFlash・DSpark・n-gram法などから、受理長・ドラフトオーバーヘッド・学習/運用コストのバランスでドラフト機構を選ぶ

## 使いどころ

- LLM推論基盤チームがレイテンシとスループットのトレードオフを踏まえてドラフト長を調整する場面
- 学習コスト制約から外部ドラフトモデルとEAGLE-3/MTPのような自己投機型手法のどちらを採用するか判断する場面
- コーディングや要約などのタスク領域ごとにSPEED-Benchで受理長を計測し、本番投入前に投機的デコーディングの効果を検証する場面
