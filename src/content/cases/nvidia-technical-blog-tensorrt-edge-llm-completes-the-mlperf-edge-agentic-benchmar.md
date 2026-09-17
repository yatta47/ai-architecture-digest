---
type: case
title: Jetson AGX Thor上のTensorRT Edge-LLMでエッジエージェント推論を6.4倍高速化
title_original: TensorRT Edge-LLM Completes the MLPerf Edge Agentic Benchmark 6.4x Faster on Jetson AGX Thor
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- inference-optimization
- context-engineering
components:
- TensorRT Edge-LLM
- NVIDIA Jetson AGX Thor
- Qwen3.6-27B
- NVFP4
- FP8 KV cache
- llama.cpp
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/tensorrt-edge-llm-completes-the-mlperf-edge-agentic-benchmark-6-4x-faster-on-jetson-agx-thor/
published_at: '2026-09-16'
---

## 概要

NVIDIAはTensorRT Edge-LLMを用いてQwen3.6-27Bを単一のJetson AGX Thor上で動作させ、MLPerf Inference v6.1のEdge Agenticベンチマークで52.33 tokens/secを達成し、全1,007ターンをllama.cppリファレンス比6.4倍高速な24分36秒で完了した。NVFP4量子化とFP8 KVキャッシュ、ツリー型マルチトークン予測、エージェントターンをまたぐKVキャッシュ再利用を組み合わせ、電力・メモリ制約の厳しいエッジ環境で長文脈のエージェント推論を高速化している。

## 設計のポイント

- NVFP4量子化（重み・活性化）とFP8 KVキャッシュでDRAM帯域がボトルネックとなるエッジ低バッチ推論のメモリ量を削減する
- エージェントターンをまたぐKVキャッシュ・再帰状態の再利用によりプロンプトトークンの約96%をホットキャッシュから供給し再prefillを回避する
- 8ステップ・top-2・16ノードのツリー型マルチトークン予測で線形MTP比約40%のデコード性能向上を得る
- 量子化で浮いたメモリを長文脈・投機的デコード状態・アプリケーションワークロードに再配分する

## 使いどころ

- 電力・メモリ制約下でツール呼び出しを伴うマルチターンエージェントを動かす車両・ロボットなどのエッジ機器
- MLPerf Edge Agenticに対してエッジLLM推論スタックをベンチマーク・比較したいチーム
- 23.5Kトークン超級の長い会話履歴を伴うエージェントループを単一エッジデバイスで低遅延に処理したい用途
