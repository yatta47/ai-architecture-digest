---
type: announcement
title: エージェント/RLワークロードのCPU実行時間を短縮するVera CPU設計
title_original: NVIDIA Vera CPU Sets a New Standard for Agentic Workloads in AI Factories
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- reinforcement-learning
- inference-optimization
components:
- NVIDIA Vera CPU
- NVIDIA Olympus core
- NVIDIA Scalable Coherency Fabric
- LPDDR5X
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-vera-cpu-sets-a-new-standard-for-agentic-workloads-in-ai-factories/
published_at: '2026-06-11'
---

## 概要

エージェントAIやRLでは、ツール実行・データ処理・オーケストレーションなどモデル呼び出しの合間のCPU処理がクリティカルパスになるとし、NVIDIA Vera CPUがこの需要に応える設計だと解説する。88基のOlympusコアと最大1.2TB/sのLPDDR5X帯域、Scalable Coherency Fabricによるコア間通信高速化により、競合アーキテクチャ比でエージェントワークロードのサンドボックス性能を1.8倍以上、グラフ探索性能を3倍以上向上させる。

## 設計のポイント

- コア数よりシングルコアの持続性能を優先し、逐次実行が支配的なエージェントの1ステップごとの待ち時間を短縮する
- 分岐の多いエージェントコードに対応するニューラル分岐予測器と広いフロントエンドで、深いソフトウェアスタックでも高いIPCを維持する
- モノリシックメッシュ上のScalable Coherency Fabricで全コアを接続し、ダイをまたぐ構成より高速で予測可能なコア間データ移動を実現する

## 使いどころ

- 多数の同時RL評価環境やサンドボックスを高負荷状態でも高速に完走させたいAIファクトリー運用者
- ツール呼び出しやオーケストレーションのCPU待ちでGPU利用率が下がっている推論/RL基盤を改善したいチーム
