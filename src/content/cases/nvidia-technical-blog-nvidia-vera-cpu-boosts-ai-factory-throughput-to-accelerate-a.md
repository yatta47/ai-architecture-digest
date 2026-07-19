---
type: announcement
title: 'Vera CPU: エージェント/RLワークロードを支えるCPU設計'
title_original: NVIDIA Vera CPU Boosts AI Factory Throughput to Accelerate Agentic Workloads
industry: cross-industry
cloud: []
patterns:
- reinforcement-learning
- ai-agent
- inference-optimization
components:
- NVIDIA Vera CPU
- NVIDIA Olympus core
- NVIDIA Scalable Coherency Fabric
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-vera-cpu-boosts-ai-factory-throughput-to-accelerate-agentic-workloads/
published_at: '2026-07-09'
---

## 概要

エージェント実行やRL学習ではモデル呼び出しの合間にCPUがツール実行やKVキャッシュ管理などの逐次処理を担うため、CPU性能がGPUフリートの生産性を左右する。NVIDIA Vera CPUは88コアの単一ダイ設計と高いシングルコア性能により、RL評価完了率を45%から85%へ、ピーク負荷時レイテンシを40%削減し、GPU利用効率とSLA遵守率を高める。

## 設計のポイント

- モノリシックダイと統合キャッシュでチップレット間ホップを排除し、負荷時のテールレイテンシを予測可能にする
- RLのロールアウトはシーケンシャルで分岐の多い処理が支配的なため、コア数よりシングルコア性能を優先する設計にする
- CPU側の停滞はKVキャッシュのエビクションを招きGPUの節約効果を失わせるため、CPUを学習・推論のクリティカルパスとして扱う

## 使いどころ

- 大規模なRL学習パイプラインでロールアウト完了率を上げてtime-to-convergenceを短縮したいチーム
- 多数の同時サンドボックス・ツール呼び出しを伴うエージェント推論で予測可能な低レイテンシ応答が必要なサービス
