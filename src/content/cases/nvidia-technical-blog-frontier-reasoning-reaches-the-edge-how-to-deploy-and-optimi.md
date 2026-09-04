---
type: guidance
title: NVIDIA Jetsonでのエッジ推論最適化
title_original: 'Frontier Reasoning Reaches the Edge: How to Deploy and Optimize Models on NVIDIA Jetson'
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
- ai-agent
components:
- NVIDIA Jetson
- Nemotron 3.5 Lightning
- Qwen3.8-27B
- vLLM
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/frontier-reasoning-reaches-the-edge-how-to-deploy-and-optimize-models-on-nvidia-jetson/
published_at: '2026-09-04'
---

## 概要

2026年にリリースされたNemotron 3.5 LightningやQwen3.8-27Bなどのコンパクトなオープンモデルは、これまでデータセンター級のシステムが必要だった推論・エージェント能力をNVIDIA Jetsonのようなエッジデバイス上でローカルに実行可能にし、NVFP4量子化と投機的デコードの組み合わせでBF16比最大6.28倍のデコードスループットを実現する方法を解説する。

## 設計のポイント

- 1トークンあたり3億パラメータのみ活性化するMoEのNemotron 3.5 Lightningと全27Bを活性化する密モデルQwen3.8-27Bはワークロードごとに向き不向きが異なるため、対象アプリの意思決定パターンで両方をベンチマークして選ぶ
- NVFP4量子化(計算量とメモリの削減)と投機的デコード(1検証ステップで複数トークンを確定)を組み合わせてエッジ上のデコードスループットを大きく改善する
- 最速の投機的デコード構成はモデルごとに異なるため(NemotronはDSpark、QwenはDFlash2)、対象モデルでドラフトチェックポイントと手法を実測検証する

## 使いどころ

- ネットワーク接続が不安定・利用できない環境で稼働する監視やロボットなど、エージェントループをオンプレミスで完結させたい場合
- センサーデータやログを監視し承認済みの是正アクションを取って専門家へエスカレーションする常時稼働エージェントを構築したい場合
- データをデバイス外に出せない、あるいはレイテンシ要件からデータセンター往復を避けたいエッジAIアプリケーション
