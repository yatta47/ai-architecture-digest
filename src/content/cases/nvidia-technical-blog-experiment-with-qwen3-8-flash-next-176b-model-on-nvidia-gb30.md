---
type: announcement
title: NVIDIA GB300 NVL72でQwen3.8-Flash-Next 176BをエージェンティックコーディングAI基盤として検証
title_original: Experiment with Qwen3.8-Flash-Next 176B Model on NVIDIA GB300 NVL72 for Agentic Coding
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- inference-optimization
- context-engineering
- ai-agent
- reinforcement-learning
components:
- Qwen3.8-Flash-Next
- NVIDIA GB300 NVL72
- SGLang
- vLLM
- NVIDIA TensorRT-LLM
- NVIDIA NeMo AutoModel
- NVIDIA NeMo RL
- NVIDIA DGX Station
- NVIDIA DGX Spark
- RTX PRO 6000 Blackwell
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/experiment-with-qwen3-8-flash-next-176b-model-on-nvidia-gb300-nvl72-for-agentic-coding/
published_at: '2026-08-26'
---

## 概要

AlibabaがQwen4アーキテクチャのプレビューとして公開した176BパラメータのMoEモデルQwen3.8-Flash-Nextは、Gated DeltaNetとQwen Sparse Attentionを組み合わせたハイブリッド構成でロングコンテキスト推論のボトルネックを解消する。NVIDIAはGB300 NVL72上でこのモデルを検証し、GPUあたり16K tokens/sec超のスループットとSGLang・vLLM・TensorRT-LLMなどによるDay 0推論サポート、NeMo AutoModel/NeMo RLによるファインチューニング経路を提供した。ローカルのDGX StationやワークステーションからラックスケールのGB300 NVL72まで同一モデルでスケールできる開発フローを示している。

## 設計のポイント

- 4層のうち3層をGated DeltaNetによる履歴コンテキストの固定サイズ圧縮に充て、残り1層をQwen Sparse Attentionによる高精度な全文脈検索に使うことでKVキャッシュ増大と計算コストを抑える。
- トークン単位ではなくマイクロブロック単位で重要度を推定・選択するQSAにより、コンテキストが伸びてもインデキシングオーバーヘッドが線形に増えない設計にしている。
- 72基のBlackwell Ultra GPUを130TB/sのNVLinkドメインで結合し、MoEのエキスパート間通信がラック外ネットワークを跨がないようにすることで推論スループットを最大化する。
- ローカルのDGX StationやRTX PRO 6000ワークステーションでプロトタイピングし、同一モデル・同一スタックのままGB300 NVL72の本番環境へスケールできる経路を用意する。

## 使いどころ

- 長大なコンテキストを扱うエージェンティックコーディングやドキュメント処理、ツール駆動ワークフローを高スループット・低レイテンシで動かしたい開発者。
- 1Mトークン級のプレフィックスキャッシュ命中率が高いオンラインサービングを行い、推論コストとレイテンシを両立させたいチーム。
- 手元のワークステーションで小規模検証してから、同じモデルをラックスケールGB300 NVL72に無改修でスケールさせたいMLOps担当者。
- Hugging Face形式のチェックポイントから変換なしでLoRAやフルSFT、強化学習による追加チューニングを行いたい開発者。
