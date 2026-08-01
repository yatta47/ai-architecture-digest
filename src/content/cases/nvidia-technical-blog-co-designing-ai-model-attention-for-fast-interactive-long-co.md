---
type: guidance
title: GPU向けAttention設計の共設計ガイド（グループサイズ・head次元・並列化）
title_original: Co-Designing AI Model Attention for Fast, Interactive Long-Context Inference
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- parallel-execution
components:
- TensorRT-LLM
- NVIDIA Nemotron 3
- FlashAttention
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/co-designing-ai-model-attention-for-fast-interactive-long-context-inference/
published_at: '2026-07-31'
---

## 概要

NVIDIAは、GQA/MQAのグループサイズ・head次元・シーケンス長がprefill（compute-bound）とdecode（memory-bound）それぞれの性能をどう規定するかをGEMM形状とアリスメティック強度から分析し、長文脈エージェント向け推論のための共設計ガイドラインを示した。KVヘッド数に応じてTensor ParallelismやAttention Data Parallelism、KV Parallelismなどを使い分けることが推奨されている。

## 設計のポイント

- decode性能を上げるにはグループサイズ(G)を大きくし、head次元は128または256でGPUタイル・メモリアラインメントに合わせる
- KVキャッシュ圧縮やスパース/スライディングウィンドウAttention、ハイブリッドアーキテクチャで実効KV状態を最小化する
- Tensor Parallelismの分割数はKVヘッド数を超えないようにし、KVヘッドが少ないモデルはADP/KVP/Wide EP/Helix Parallelismなどのハイブリッド並列を検討する

## 使いどころ

- 長文脈・エージェント型ワークロード向けにLLM推論スタックのスループットと対話性を最適化したいモデル/インフラ設計者
- TensorRT-LLMなどでカスタムモデルのAttention構成とGPU並列化戦略を選定する際のチェックリストとして
