---
type: announcement
title: 長文コンテキスト向けMoEモデルQwen3.8-Flash-NextのGB300対応
title_original: Experiment with Qwen3.8-Flash-Next on NVIDIA GB300 NVL72 for Agentic Coding
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
- fine-tuning
components:
- Qwen3.8-Flash-Next
- NVIDIA GB300 NVL72
- NVIDIA NeMo AutoModel
- NVIDIA NeMo RL
- SGLang
- vLLM
- NVIDIA TensorRT LLM
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/experiment-with-qwen3-8-flash-next-on-nvidia-gb300-nvl72-for-agentic-coding/
published_at: '2026-08-27'
---

## 概要

AlibabaがQwen4アーキテクチャのプレビューとして公開したQwen3.8-Flash-Nextは、Gated DeltaNetとQwen Sparse Attentionを組み合わせたMoEモデルで、最大1Mトークンのコンテキストを扱える。NVIDIAはGB300 NVL72上でGPUあたり16K tokens/秒超のスループットを確認し、SGLang/vLLM/TensorRT LLMでのDay 0対応とNeMo AutoModel/NeMo RLによるポストトレーニングレシピを提供する。

## 設計のポイント

- 全layerの3/4にGated DeltaNet（履歴コンテキストを固定サイズの再帰状態へ圧縮）、残り1/4にQwen Sparse Attention（ブロック単位で重要領域のみ選択）を配置しKVキャッシュの増大を抑制
- トークン単位インデクサに比べ計算コストの低いブロック単位の重要度推定により、1Mトークン級のprefillを最大7.6倍高速化
- 72GPUを単一NVLinkドメイン（130TB/s）で結ぶGB300 NVL72により、MoEのエキスパート間all-to-all通信のボトルネックを解消

## 使いどころ

- 長文コンテキストを扱うエージェント型コーディングやツール駆動ワークフローの高スループット推論基盤を検討するチーム
- ローカルDGXワークステーションからラックスケールGB300 NVL72まで同一モデルを段階的にスケールさせたい開発者
