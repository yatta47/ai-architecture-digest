---
type: case
title: GB300 NVL72でMoE事前学習の世界記録を達成したNVIDIAの通信最適化
title_original: Setting a World Record for MoE Pre-Training on NVIDIA GB300 NVL72
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- pretraining
components:
- NVIDIA GB300 NVL72
- NVLink
- ConnectX-8 SuperNIC
- Quantum-X800 InfiniBand
- Spectrum-X Ethernet
- NVIDIA Megatron Core
- TorchTitan
- JAX
- DeepSeek-V3
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/setting-a-world-record-for-moe-pre-training-on-nvidia-gb300-nvl72/
published_at: '2026-07-21'
---

## 概要

NVIDIAはGB300 NVL72上でDeepSeek-V3 671BのMoE事前学習において1GPUあたり1,648TFLOPsという世界記録を達成した。ラック内はメモリセマンティックなNVLinkで全GPU間all-to-all通信を隠蔽し、ラック間はConnectX-8とInfiniBand/Ethernetでスケールアウトすることで、256から1,024GPUへの拡張でも97%以上のGPUあたりスループットを維持した。

## 設計のポイント

- MoEのトークンディスパッチ用all-to-all通信をラック内のNVLink(1.8TB/s、非ブロッキング130TB/s)に閉じ込め、計算とのオーバーラップを最大化する。
- ラック間のスケールアウト通信は軽量かつ計算ウィンドウ内に収まるよう設計し、単一の遅いリンクがステップ全体を律速しないようにする。
- BlueField DPUでインフラ処理(ネットワーキング・ストレージ・セキュリティ)をホストCPUからオフロードし、学習ジョブのオーバーヘッドを下げる。
- Megatron Core・TorchTitan・JAXへの最適化をオープンソースに還元し、同一ハードウェアでソフトウェアだけで半年で1.5倍の性能向上を得た。

## 使いどころ

- 数千億〜兆パラメータ級のMoEモデルを多数GPUで事前学習する研究・プロダクトチーム。
- delivered FLOPsを最大化してGPU投資対効果を高めたいAIインフラ担当。
