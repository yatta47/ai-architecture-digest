---
type: announcement
title: エージェント型AI時代を支えるNVIDIA Rubin GPUアーキテクチャ
title_original: 'Inside NVIDIA Rubin GPU Architecture: Powering the Era of Agentic AI'
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- gpu-fleet-reliability
components:
- NVIDIA Rubin GPU
- NVIDIA Vera Rubin NVL72
- HBM4
- NVLink 6
- Transformer Engine
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/inside-nvidia-rubin-gpu-architecture-powering-the-era-of-agentic-ai/
published_at: '2026-07-21'
---

## 概要

NVIDIAは、エージェント型AI推論に特化した新GPU「Rubin」を発表した。336億トランジスタ、288GBのHBM4メモリ(22TB/s)、第3世代Transformer Engineなどにより、Blackwell比で単位電力あたり最大10倍のエージェント推論スループットを実現する。ラック単位のVera Rubin NVL72では液冷や電源平滑化、ホットスワップ可能なNVLinkスイッチにより、大規模モデルを高い電力効率で稼働できる。

## 設計のポイント

- MoEモデルのエキスパート重み移動を減らすため、TMAのディスクリプタをインライン更新できるようにし、メタデータ管理のオーバーヘッドを削減する。
- 長文コンテキストのアテンション処理やカーネル遷移レイテンシを最小化する専用機構で、推論のトークン/秒とトークン/ワットを最大化する。
- ラックスケールでは液冷・電源平滑化・ケーブルレス設計により、同じ電力予算内でより多くのGPUを稼働できるようにする。

## 使いどころ

- 長時間・多ステップで推論するエージェント型ワークロードを大規模に運用するAIファクトリー。
- 巨大MoEモデルを低レイテンシ・高スループットで配信したいインフラチーム。
