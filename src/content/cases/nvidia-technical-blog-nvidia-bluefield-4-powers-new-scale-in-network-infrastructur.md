---
type: announcement
title: エージェント型AIファクトリーのアクセス・セキュリティを担う第5の柱「Scale-In」とBlueField-4
title_original: NVIDIA BlueField-4 Powers New Scale-In Network Infrastructure for Agentic AI Factories
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- defense-in-depth
- north-south-infrastructure-offload
components:
- NVIDIA BlueField-4
- NVIDIA DOCA
- NVIDIA Spectrum-X Ethernet
- NVIDIA ConnectX-9
- NVIDIA CMX
outcome:
  type: reliability
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-bluefield-4-powers-new-scale-in-network-infrastructure-for-agentic-ai-factories/
published_at: '2026-08-24'
---

## 概要

NVIDIAは、AIファクトリーのネットワーキング基盤における5本目の柱として「Scale-In」を発表した。BlueField-4 DPUとDOCA、Spectrum-X Ethernetを組み合わせ、ポリシー適用・ストレージアクセス・セキュリティ・テレメトリをホストCPUから独立して処理することで、南北トラフィックを最大800Gb/sで処理しつつテナント分離と可観測性を実現する。

## 設計のポイント

- セキュリティ・ストレージアクセス・テレメトリなどのインフラサービスをホストCPUから切り離し、専用のDPU処理ドメインとして分離することでテナントワークロードの性能への影響を避ける
- Scale-Up(NVLink)/Scale-Out(Spectrum-X/InfiniBand)/Scale-Across(Spectrum-XGS)/Context Memory(CMX)と並ぶ第5の柱として南北アクセスを再定義し、AIファクトリー全体を統合インフラドメインとして運用する
- DOCAソフトウェアでプログラマブルなポリシー駆動運用を可能にし、テナント分離・脅威検知・ストレージ仮想化・フリート全体の可観測性を一貫した仕組みで提供する

## 使いどころ

- 多数のテナント・エージェント・アプリケーションが共有するAIファクトリーでセキュリティとアクセス制御をホストCPUの負荷なく実現したい場合
- 大規模GPUクラスタの運用でストレージアクセスや脅威検知をオフロードしてスケールさせたい場合
