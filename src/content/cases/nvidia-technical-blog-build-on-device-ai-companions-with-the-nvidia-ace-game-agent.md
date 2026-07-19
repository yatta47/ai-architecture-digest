---
type: announcement
title: NVIDIA ACE Game Agent SDKとUE5プラグインでオンデバイスAIコンパニオンを構築
title_original: Build On-Device AI Companions with the NVIDIA ACE Game Agent SDK and Unreal Engine 5 Plugins
industry: media
cloud:
- on-prem
patterns:
- voice-agent
- ai-agent
- rag
components:
- NVIDIA ACE Game Agent SDK
- Qwen 3.5 4B
- Chatterbox Turbo 350M
- nemo-conformer-ctc-120m
- NVIDIA DLSS 4.5
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/build-on-device-ai-companions-with-the-nvidia-ace-game-agent-sdk-and-unreal-engine-5-plugins/
published_at: '2026-07-09'
---

## 概要

Unreal Fest 2026でNVIDIAは軽量なC/C++エージェントフレームワークNVIDIA ACE Game Agent SDK Betaと、ASR/SLM/TTSに対応するUnreal Engine 5プラグイン群を発表した。Agent/Chat/RAGの3種のAPIでNPCに多段階のツール利用推論を持たせられ、PUBG AllyやTotal War: PHARAOHのアドバイザーで実戦投入済みの手法をUE5開発者に開放する。

## 設計のポイント

- ステートフルに複数ステップの推論を自律駆動するAgent API、直接制御向けのステートレスなChat API、知識接地用のRAG APIを用途別に使い分ける
- ASR・SLM・TTSをすべてオンデバイスで実行し、クラウド依存によるレイテンシ変動とコストの不確実性を避ける
- RAG APIで1,200以上の連結されたゲームデータテーブルを検索させ、NPCの回答をゲーム内の実データに接地させる

## 使いどころ

- Unreal Engine上でオンデバイスの低遅延AIキャラクター/NPCを実装したいゲームスタジオ
- ブループリントとC++の両方でASR/LLM/TTSパイプラインを素早くプロトタイピングしたい技術アーティスト
