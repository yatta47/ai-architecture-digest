---
type: announcement
title: エージェントAI向け決定論的スケールアップを実現するVera Rubinプラットフォームの設計
title_original: How the NVIDIA Vera Rubin Platform is Solving Agentic AI's Scale-Up Problem
company: NVIDIA
industry: cross-industry
cloud:
- on-prem
patterns:
- ai-agent
- inference-optimization
- parallel-execution
components:
- NVIDIA Vera Rubin NVL72
- NVIDIA Groq 3 LPX
- LPU C2C
- NVIDIA MGX
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-the-nvidia-vera-rubin-platform-is-solving-agentic-ais-scale-up-problem/
published_at: '2026-06-11'
---

## 概要

エージェント型AIの推論はセッション内で数百回に及ぶ非決定的なトラジェクトリを生成し、レイテンシがエンドツーエンドで積み上がる。NVIDIA Vera Rubin NVL72とNVIDIA Groq 3 LPX（LPU C2C）は、高radixポイントツーポイントリンク・コンパイラによる静的データ移動スケジューリング・ハードウェアによるplesiosynchronous同期という3技術を組み合わせ、数千チップにまたがる決定論的で低ジッタな実行を実現し、兆パラメータ級MoEモデルを長コンテキストで低レイテンシ配信できるようにする。

## 設計のポイント

- 各LPUに96本のC2Cリンク（112Gbps）を持たせる高radixポイントツーポイント接続により、直接ピア接続と低ホップ数を実現し集団通信の効率を高める。
- コンパイラが送信元・経路・到着タイミングまで転送を事前に静的スケジューリングすることで、ランタイムでの競合や負荷分散判断を排除する。
- 各LPUのクロックドリフトをplesiosynchronousプロトコルで補正し、数千チップを単一のコンパイル時既知レイテンシを持つ実行面として扱う。

## 使いどころ

- 兆パラメータ級MoEモデルを長コンテキストかつ低レイテンシで提供する必要があるプレミアムAIサービス事業者。
- マルチターン・マルチエージェントパイプラインでKVキャッシュや会話履歴の増大によるレイテンシ蓄積を抑えたい基盤インフラチーム。
