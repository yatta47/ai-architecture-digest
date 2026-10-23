---
type: guidance
title: AIエージェントでロボットの歩行学習をシミュレーションで進めるワークフロー
title_original: Using AI Agents to Teach Robots Like Microduck to Walk in Simulation
company: NVIDIA
industry: manufacturing
cloud: []
patterns:
- ai-agent
- reinforcement-learning
components:
- NVIDIA RTX Spark
- Hermes
- Nemotron
- Isaac Sim
- Isaac Lab
- Omniverse
- Newton
- Blender
- FreeCAD
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/using-ai-agents-to-teach-robots-like-microduck-to-walk-in-simulation/
published_at: '2026-10-23'
---

## 概要

エージェントがプロンプトから計画を立て、3Dアセット生成、Isaac Simでの障害物コース構築、Isaac Labでの強化学習(4,096並列環境)、ローカル検証までを通す手順を示す。sim-to-real移行に向けた準備も扱う。

## 設計のポイント

- ローカル機で計画と検証、クラウドGPUで大規模学習という役割分担にしている。
- アセット生成から学習まで各段階をエージェントが支援する。
- 学習したポリシーをシミュレーションで検証してから実機転移に進む。

## 使いどころ

- ロボット開発の試作サイクルを短縮したい開発者。
- 強化学習の環境構築を自動化したいチーム。
