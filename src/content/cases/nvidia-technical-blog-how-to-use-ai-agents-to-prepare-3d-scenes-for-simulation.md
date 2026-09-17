---
type: guidance
title: AIエージェントでBlenderシーンをロボティクスシミュレーション向けに自動準備する
title_original: How to Use AI Agents to Prepare 3D Scenes for Simulation
industry: manufacturing
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
- eval
components:
- NVIDIA Omniverse Libraries
- OpenUSD
- NVIDIA NemoClaw
- Hermes
- Codex
- Claude
- NVIDIA Isaac Sim
- NVIDIA Isaac Lab
- NVIDIA Nemotron
- ovphysx
- ovrtx
outcome:
  type: productivity
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/how-to-use-ai-agents-to-prepare-3d-scenes-for-simulation/
published_at: '2026-09-17'
---

## 概要

NVIDIAは、CodexやClaudeが全体を統括し、NemoClaw経由でデプロイされたHermesベースの専用サブエージェントがOmniverse Librariesのツール（ovphysxで物理属性付与、ovrtxでプレビューレンダリング）を使ってBlenderシーンをOpenUSDとして構造化し、意味ラベル・センサー・物理特性を付与してSimReady検証を通す、というエージェント型ワークフローを解説する。検証をIsaac SimやIsaac Labへの引き渡し前のゲートとし、曖昧な判断は人間にエスカレーションする設計になっている。

## 設計のポイント

- OpenUSDを共有の契約レイヤーとして使い、階層とメタデータを保持したまま複数エージェントが反復的に編集できるようにする
- 全体を統括するオーケストレーションエージェントと、各タスク専用のツールを持つサブエージェントに役割を分割する
- 機械的に安全な修正は自動適用し、意図に依存する曖昧な判断は人間にエスカレーションする
- SimReady検証をシミュレーション環境への引き渡し前の合否ゲートとして自動実行する

## 使いどころ

- アーティストが作成した3DシーンをロボティクスシミュレーションのSimReady状態に変換したいエンジニア
- ラベリングや衝突メッシュ作成など定型的だが手間のかかるシーン準備作業を自動化したいチーム
- Isaac Sim/Isaac Labへの引き渡しに検証ゲート付きの再現可能なエージェントパイプラインを構築したい組織
