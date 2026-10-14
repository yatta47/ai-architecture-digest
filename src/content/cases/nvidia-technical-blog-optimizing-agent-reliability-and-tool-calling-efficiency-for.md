---
type: case
title: NeMo Gymによるチップ設計エージェントの信頼性とツール呼び出し効率の改善
title_original: Optimizing Agent Reliability and Tool Calling Efficiency for Chip Design Using NVIDIA NeMo Gym
company: Siemens EDA
industry: manufacturing
cloud: []
patterns:
- eval
- reinforcement-learning
- ai-agent
- context-engineering
components:
- NVIDIA NeMo Gym
- Siemens Fuse EDA AI Agent
- Model Context Protocol
- NVIDIA Nemotron
outcome:
  type: quality
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/optimizing-agent-reliability-and-tool-calling-efficiency-for-chip-design-using-nvidia-nemo-gym/
published_at: '2026-10-14'
---

## 概要

Siemens EDAのエージェントがLiberty file生成を行う際、最終成果物を検証するドメイン固有ベリファイアで評価・改善した事例。複合スコアは約55%から約95%に向上し、エージェントのターン数は155から53、出力トークンは約81Kから約29Kに減った。

## 設計のポイント

- 中間ステップではなく最終成果物を基準データと照合するベリファイアで採点し、いずれかのゲートで失敗なら報酬ゼロにする
- ロールアウトの軌跡を追跡して早期エラーの下流伝播を特定する
- ベリファイア診断に基づきスキルとMCPツール説明を改善する

## 使いどころ

- 多段工程で誤りが伝播しやすいEDA・CAEなどのエンジニアリングエージェント
- 本番投入前にエージェントの信頼性を定量評価したいチーム
