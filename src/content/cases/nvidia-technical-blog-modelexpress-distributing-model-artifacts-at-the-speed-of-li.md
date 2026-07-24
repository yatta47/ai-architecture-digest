---
type: case
title: NVIDIA ModelExpress:GPU間P2P転送でLLM重みのコールドスタートを高速化
title_original: 'ModelExpress: Distributing Model Artifacts at the Speed of Light'
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- gpu-fleet-reliability
components:
- NVIDIA ModelExpress
- NIXL
- GPUDirect Storage
- vLLM
- SGLang
- Dynamo
- llm-d
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/modelexpress-distributing-model-artifacts-at-the-speed-of-light/
published_at: '2026-07-24'
---

## 概要

NVIDIA ModelExpressは、既存のサービング中レプリカからGPU-to-GPUのP2P RDMA転送を優先し、オブジェクトストレージやホストメモリ経由の冗長なコピーを排除するモデル重み配布基盤。DeepSeek-V4 Proの新規レプリカ起動時間を8分から1分44秒に短縮する。

## 設計のポイント

- 初回ワーカーはオブジェクトストレージからストリーミングでブートストラップし、以降のワーカーはサービング中ピアからGPU間P2P RDMAで直接重みを取得する経路選択を自動化する
- 共有ディスクキャッシュへのダウンロードをMetadata Storeでのアトミックな排他制御により1回に集約し、レプリカ台数分の重複ダウンロードを防ぐ
- GPUDirect Storage対応時はホストメモリのステージングを迂回してローカルストレージからGPUへ直接読み込む
- 強化学習の重みロールアウトにも同じ経路選択の仕組みを適用し、トレーナーからロールアウトワーカーへの重み更新を高速化する

## 使いどころ

- オートスケールやローリング更新で頻繁に新規レプリカを立ち上げる大規模LLM推論基盤
- 強化学習の事後学習で更新済み重みを継続的にロールアウトワーカーへ配布する必要があるパイプライン
