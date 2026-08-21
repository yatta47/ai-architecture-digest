---
type: case
title: NVIDIA AVO、長期タスク自律エージェント基盤でARC-AGI-3を満点クリア
title_original: NVIDIA AVO Reaches 100% on ARC-AGI-3, Demonstrating a Frontier-Level General-Purpose Architecture for Long-Horizon
  Autonomous Agents
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- memory-consolidation
- multi-agent-orchestration
components:
- Claude Opus 5
- NVIDIA DGX B200
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-avo-reaches-100-on-arc-agi-3-demonstrating-a-frontier-level-general-purpose-architecture-for-long-horizon-autonomous-agents/
published_at: '2026-08-21'
---

## 概要

永続メモリ・監督機構・ツール利用を統合した汎用エージェント基盤AVOにより、Claude Opus 5単体では30%だったARC-AGI-3スコアを100%まで引き上げた。GPUカーネル最適化タスクでも500超の方向性を自律探索し、FlashAttention-4比で最大10.5%の性能改善を人手介入なしで達成し、性能はモデル単体でなくエージェントシステム設計に由来することを示した。

## 設計のポイント

- モデル単体の能力ではなく、永続メモリ・監督・ツール利用を組み合わせたエージェントハーネス設計で長期タスクの性能を引き上げる
- GPUカーネル最適化のような探索的タスクで、多数の方向性を自律的に試行しコミットする探索ループを人手介入なしで回す
- 行動効率（環境アクション数）も評価指標に含め、他手法比で少ないアクション数での達成を性能指標とする

## 使いどころ

- フロンティアモデルの素の性能だけでなく周辺のエージェントハーネス設計を強化したい研究・開発チーム
- GPUカーネルなど専門領域での自律的な性能改善探索を自動化したい場合
- 長期タスクの自律実行における永続メモリ設計を検討しているエージェント開発者
