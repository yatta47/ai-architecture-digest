---
type: guidance
title: AIファクトリー向けスケールアップネットワーク第6世代NVLinkの設計思想
title_original: 'NVIDIA NVLink: The Scale-Up Network for AI Factories'
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- gpu-fleet-reliability
- cost-optimization
components:
- NVIDIA NVLink
- NVLink 6 Switch
- NVIDIA Dynamo
- TensorRT-LLM
- NCCL
- NIXL
- NVLink-C2C
- NVLink Fusion
- NVIDIA Quantum InfiniBand
- NVIDIA Spectrum-X Ethernet
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-nvlink-the-scale-up-network-for-ai-factories/
published_at: '2026-07-20'
---

## 概要

兆パラメータ級モデルやMoE、disaggregated servingなど今日のAIワークロードは、多数のアクセラレータを単一の計算ユニットのように協調させる高帯域・低遅延なGPU間通信を必要とする。第6世代NVLinkはGPUあたり最大3.6TB/s、ラック単位で260TB/s、130TFLOPSのネットワーク内演算を実現し、チップからソフトウェア(Dynamo/TensorRT-LLM/NCCL/NIXL)までを一体設計するextreme co-designにより、市販Ethernet比で最大2.3倍のデコードスループットとHopperからBlackwellへの50倍のtokens/wattを達成する。制御プレーンの冗長化やホットスワップ可能なスイッチトレイなど本番AIファクトリー向けの可用性機能も備える。

## 設計のポイント

- MoEのエキスパート並列やdisaggregated inferenceで生じる全対全通信を、スケールアップドメイン内の高帯域・低遅延ファブリックで吸収し、並列化の効果を通信オーバーヘッドで相殺しないようにする
- SHARPによるネットワーク内演算でリダクションなどのコレクティブ演算をファブリック側にオフロードしGPUサイクルを演算に専念させる
- チップ・システム・ファブリック・ソフトウェアスタックを一体で設計するextreme co-designにより、単純な帯域スペックだけでなくエンドツーエンドのトークン処理性能を最適化する
- コントロールプレーンの冗長化・ホットスワップ可能なスイッチトレイ・動的ルーティング・無停止アップデートにより本番AIファクトリーの稼働継続性を確保する

## 使いどころ

- 数千〜数十万GPU規模でMoEや長文脈推論を運用するAIインフラ/プラットフォームチーム
- トークンあたりのワット・ドルコストを最適化したいハイパースケーラーやGPUクラウド事業者
- disaggregated inferenceやexpert parallelismを前提に大規模LLM推論基盤を設計するアーキテクト
