---
type: announcement
title: エージェントAIのシングルスレッド性能を最大化するNVIDIA Vera CPU
title_original: 'NVIDIA Vera CPU: Olympus Cores Built for Maximum Single-Threaded Performance in Agentic AI'
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- ai-agent
components:
- NVIDIA Vera CPU
- Olympus core
- NVLink-C2C
- SOCAMM2 LPDDR5X
- Scalable Coherency Fabric
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/inside-nvidia-vera-cpu-olympus-cores-built-for-maximum-single-threaded-performance-in-agentic-ai/
published_at: '2026-07-21'
---

## 概要

NVIDIAは、エージェントのツール呼び出しやコード実行などCPU側の処理が増える中、シングルスレッド性能を最大化する新CPU「Vera」とOlympusコアを発表した。分岐予測強化や広いアウトオブオーダー実行、コヒーレント接続により、不規則で分岐の多いエージェントの実行パスを高速化する。

## 設計のポイント

- ニューラル分岐予測器や10-wideデコードで、分岐の多いエージェントランタイムやインタプリタの前段処理を高速化する。
- メモリリネーミングや値予測などの依存関係解消機構で、ポインタの多いコードや長い依存チェーンのストールを減らす。
- NVLink-C2Cによるコヒーレント接続とCXL/PCIe対応で、GPUとの間の機密データ移動を安全かつ低遅延に保つ。

## 使いどころ

- サンドボックスでのコード実行やツール呼び出しが多いエージェントループをホストするインフラ。
- 同時実行数が多くても予測可能なレイテンシが必要なAIファクトリーのCPU選定。
