---
type: announcement
title: GB300 NVL72で動かすMuse Spark Open
title_original: Scale Agentic Coding Workflows with Meta's Muse Spark Open on NVIDIA GB300 NVL72
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- inference-optimization
- multi-agent-orchestration
components:
- NVIDIA GB300 NVL72
- NVIDIA NIM
- Muse Spark Open
- Hugging Face
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/scale-agentic-coding-workflows-with-metas-muse-spark-open-on-nvidia-gb300-nvl72/
published_at: '2026-10-15'
---

## 概要

NVIDIAはMuse Spark OpenをGB300 NVL72上で動かし、GPUあたり最大5万トークン/秒、ユーザーあたり最大600トークン/秒を示した。NVFP4チェックポイントで重みのメモリを減らし、長文脈の同時セッション用にKVキャッシュを確保する。

## 設計のポイント

- NVFP4で移動バイト数を減らして速度を上げ、空いたメモリをKVキャッシュに回す。
- テキスト・画像・映像・音声を1つの知覚エンコーダで処理し、モダリティ別のパイプラインを不要にする。
- 行動前に解説を出力し、エージェントの動作を追えるようにする。

## 使いどころ

- 長時間のエージェント型コーディングを高スループットで配信する基盤。
- スクリーンショットやログを含む開発ワークフロー。
