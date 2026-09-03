---
type: announcement
title: 宅内ネットワーク上の複数端末にマルチエージェント推論を分散するNVIDIA PAIR
title_original: NVIDIA PAIR Virtual Inference Router Expands Available Compute on Your Local Network
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- multi-agent-orchestration
- inference-optimization
- parallel-execution
components:
- NVIDIA PAIR
- Ollama
- LM Studio
- DGX Spark
- Hermes Desktop
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-pair-virtual-inference-router-expands-available-compute-on-your-local-network/
published_at: '2026-09-02'
---

## 概要

NVIDIAが、家庭内ネットワーク上の複数のGPU搭載端末へ独立した推論リクエストを分散するVirtual Inference Router『PAIR』のベータ版を発表。エージェントハーネスの変更なしにOllama/LM Studioのインターフェースをプロキシし、マルチエージェント/サブエージェントによるGPU競合のボトルネックを緩和する。5サブエージェントのデモでは3台構成で処理時間が18分から8分48秒に短縮された。

## 設計のポイント

- エージェント側からは1本の接続に見えるプロキシとして振る舞い、新しいクラスタAPIへの統合を各エージェントハーネスに要求しない
- mDNS探索・mTLS暗号化・ノード状態（準備状況/エンジン状態/モデル有無/GPU使用率）に基づくライブスケジューリングで動的な家庭内環境に対応する
- 1つの推論リクエストは常に1ノードで完結させ、複数GPUにまたがる分散推論は行わずワークロードレベルの並列性に留める

## 使いどころ

- ローカルで複数サブエージェントを並列実行する際にメインPCのGPUが詰まる問題の緩和
- ゲーミングPCなど他用途にも使う端末を占有せず余剰GPU容量をエージェント推論に振り向けたい個人開発者
- プライバシー上プロンプトやデータを宅内ネットワーク外に出したくないローカルAI活用シーン
