---
type: announcement
title: 16万件超のエージェントセッション遠隔測定から導いたバランス型CPU設計「Vera CPU」
title_original: Solving Agentic AI Fleet Challenges with NVIDIA Vera CPU
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- gpu-fleet-reliability
- inference-optimization
components:
- NVIDIA Vera CPU
- NVIDIA Olympus
- AMD Venice CPU
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/solving-agentic-ai-fleet-challenges-with-nvidia-vera-cpu/
published_at: '2026-08-21'
---

## 概要

NVIDIAは16万件超のエージェントセッションの実測テレメトリから、97%以上のセッションが固有の実行軌跡を持ち単一設計のCPUフリート戦略が非現実的であることを示した。エージェント処理は長い逐次的推論チェーンと一時的な並列ファンアウトの組み合わせであるため、コア数を最大化するのではなく完了セッション数を最適化する設計としてVera CPUを開発し、AMD Venice CPU比で最大1.5倍のコアあたり性能を実測した。

## 設計のポイント

- 「コア数」ではなく「完了したユーザーセッション数」をフリート設計の最適化目標に据える
- 逐次実行チェーン(レイテンシ律速)と一時的な並列ファンアウト(同時実行数律速)の両方を実測テレメトリから特定し、両立するバランス型コア設計を選ぶ
- シングルスレッド性能を上げるためにコアをオフにするとメモリ容量が座礁する(1コアあたり8GB遊休化)というトレードオフを定量化し、フリート全体のTCOで判断する

## 使いどころ

- 多様で予測不能なエージェント実行パターンを持つワークロードに対してCPUフリートを右サイジングしたいAIファクトリー運用者
- ツール呼び出しやサブエージェントのファンアウトを伴うエージェント型ワークロードのインフラ選定
