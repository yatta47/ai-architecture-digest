---
type: case
title: シャドウエンジンでLLM推論のフェイルオーバーを283秒から7.3秒に短縮
title_original: Restore LLM Inference Capacity in Seconds with Shadow Engine Recovery in NVIDIA Dynamo
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
- inference-optimization
- llmops
components:
- NVIDIA Dynamo
- GPU Memory Service
- GLM-5.2
- NVIDIA B200
- vLLM
- SGLang
- NVIDIA TensorRT-LLM
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/restore-llm-inference-capacity-in-seconds-with-shadow-engine-recovery-in-nvidia-dynamo/
published_at: '2026-08-25'
---

## 概要

NVIDIA Dynamoのシャドウエンジンリカバリは、同一GPU上に完全初期化済みの待機エンジンを常駐させ、GPU Memory Service(GMS)により重みの生存期間をエンジンプロセスから切り離すことでプロセス障害後のフェイルオーバーを高速化する。GLM-5.2をB200ノードで検証した結果、フェイルオーバー時間はコールドリスタートの283秒から7.3秒へと約39倍短縮された。

## 設計のポイント

- GPU Memory Serviceで物理メモリ上の重みをエンジンプロセスと独立管理し、プロセスがクラッシュしても重みを保持したまま新エンジンにマップし直す
- 通信ライブラリの初期化やCUDAグラフのキャプチャなど転送不可能な初期化処理は、障害前にシャドウエンジン側で完了させておく
- 複数エンジンが同一物理メモリの重みを共有マッピングすることで、スタンバイ確保による追加HBMコストをほぼゼロに抑える

## 使いどころ

- 大規模モデルのプロセス障害時にSLA上のTTFT・デコードレート劣化を最小限にしたい推論基盤チーム
- GPUリソースを増やさずに冗長性を確保したいLLMサービング運用者
