---
type: announcement
title: 常時稼働エージェントの高頻度実行層向けに30B MoEモデルNemotron 3.5 Lightningを公開
title_original: NVIDIA Nemotron 3.5 Lightning Delivers Fast, Accurate Specialized Task Execution for Long-Running Agents
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- inference-optimization
- ai-agent
components:
- NVIDIA Nemotron 3.5 Lightning
- NVIDIA NeMo Switchyard
- NeMo Automodel
- NeMo Megatron Bridge
- NeMo RL
- NeMo Gym
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/
published_at: '2026-08-11'
---

## 概要

長時間稼働するAIエージェントは、ツール呼び出しや結果検証、サブエージェントへの委譲といった高頻度・低レイテンシな実行作業にほとんどの時間を費やすが、これらにフロンティア級の推論モデルを使うとコストと遅延が増大する。NVIDIAはこの実行層に特化した30Bパラメータ(アクティブ3B)のオープンMoEモデルNemotron 3.5 Lightningを公開し、投機的デコードやハーネス最適化学習により同規模モデル比で最大4倍の出力速度を実現した。NeMo Switchyardと組み合わせることで、複雑な計画はフロンティアモデルに、高頻度の実行タスクはLightningにルーティングする『モデルのシステム』を構築できる。

## 設計のポイント

- オーケストレーションや複雑な計画を担うフロンティアモデルと、高頻度の実行タスクを担う軽量モデルに役割を分離する
- MoE構成により、トークンごとに一部のエキスパートのみを稼働させることで大規模モデル相当の性能を小規模モデルのコストで実現する
- 投機的デコードとエージェントハーネス向けの学習を組み合わせ、ツール呼び出しの精度とレイテンシを同時に改善する
- 重み・学習データ・レシピを許諾的ライセンスで公開し、LoRAや強化学習によるカスタマイズを前提に設計する

## 使いどころ

- 常時稼働でツール呼び出しを大量に行うエージェントの実行コストを削減したいチーム
- フロンティアモデルと軽量モデルを使い分ける『モデルのシステム』を構築したい場合
- DGX Sparkのようなローカルハードウェアからデータセンターまで同一モデルを展開したい場合
