---
type: case
title: NeMo Agent Toolkitによるマルチエージェント金融シグナル発見の自動化
title_original: Automating and Optimizing Financial Signal Discovery with Multi-Agent Systems
company: NVIDIA
industry: financial-services
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
- eval
- llmops
components:
- NVIDIA NeMo Agent Toolkit
- NVIDIA Nemotron (nemotron-3-nano-30b-a3b)
- NVIDIA NIM
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/automating-and-optimizing-financial-signal-discovery-with-multi-agent-systems/
published_at: '2026-06-11'
---

## 概要

NVIDIAは、クオンツ運用における「シグナル発見」（仮説立案・コーディング・バックテスト・改善のサイクル）を自動化する開発者向けサンプルを、NeMo Agent ToolkitとNemotronオープンモデル群で構築した。シグナルエージェント・コードエージェント・評価エージェントの3つが連携し、コンテキストを保持したまま仮説生成から実行、バックテスト評価、フィードバックによる再生成までを自律的に繰り返す自己改善ループを実現している。

## 設計のポイント

- シグナル生成・コード生成・バックテスト評価の3つの専門エージェントに役割を分割し、NeMo Agent Toolkitのオーケストレーション層がハンドオフとコンテキスト（シグナル定義やバックテスト結果）の保持を担う。
- シグナル生成LLMに66種類の検証済み数式演算子（名前・シグネチャ・意味・コードを持つライブラリ）だけを使わせることで、数式の幻覚を防ぎ、解釈可能かつ再現可能なシグナルを保証する。
- 評価指標としてRank IC（順位相関）を用い、ユーザーが受け入れ閾値を設定することで、性能不足のシグナルに対する改善提案をシグナルエージェントへフィードバックし自己改善ループを回す。
- ワークフローをコンフィグ駆動にすることで、固定的なスクリプトではなく柔軟な研究プラットフォームとして再利用・調整できるようにする。

## 使いどころ

- データサイエンティスト・開発者・アナリストにまたがる手作業のシグナル仮説立案・実装・検証サイクルを自動化したいクオンツ運用チーム。
- ミリ秒単位で動く市場に対応するため、アルファシグナルの発見と改善を継続的かつ自律的に回したいヘッジファンドや資産運用会社。
