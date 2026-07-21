---
type: announcement
title: JetPack 7.2、エッジデバイスでのエージェントAI展開をメモリ効率化
title_original: Deploy Agentic-Ready AI at the Edge with Memory Efficiency in NVIDIA JetPack 7.2
company: NVIDIA
industry: manufacturing
cloud:
- on-prem
patterns:
- ai-agent
- inference-optimization
- edge-ai-deployment
components:
- NVIDIA Jetson
- NemoClaw
- JetPack
- DeepStream
- Metropolis VSS
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/deploy-agentic-ready-ai-at-the-edge-with-memory-efficiency-in-nvidia-jetpack-7-2/
published_at: '2026-06-12'
---

## 概要

NVIDIA JetPack 7.2は、プライバシー・セキュリティ制御を備えたエージェント基盤NemoClawをJetsonデバイスに1コマンドでデプロイできるようにし、Linuxカスタマイズ・メモリ最適化・モデルベンチマークを自動化する『Jetson agent skills』を提供する。Jetson ThorではGPUをMulti-Instance GPU(MIG)で2分割し、ロボティクス等の低レイテンシワークロードと生成AI推論を隔離して同時実行できるようにする。

## 設計のポイント

- エージェント自身が実行する再現可能な手順(agent skills)としてLinuxカスタマイズやメモリ最適化のノウハウを定義し、手作業の設定を自動化する
- ブートローダのメモリカーブアウトからカーネルメモリ予約、常駐プロセス削減まで、スタック全体を対象にメモリ効率を追求しTCOを直接下げる
- MIGでGPUを専用コンピュート/キャッシュ/メモリ帯域を持つ複数インスタンスに分割し、安全性が重要な制御系ワークロードと生成AI推論を互いに干渉させず同居させる
- 同一ハードウェア上でソフトウェア更新のみでエージェント対応能力を継続的に引き上げる、ソフトウェア定義プラットフォームとして設計する

## 使いどころ

- ヒューマノイドロボットや産業オートメーションなど、知覚・制御と生成AIを同一SoC上で共存させたい開発者
- 限られたメモリ/コストのエッジデバイスでエージェント型AIアプリケーションを本番展開したいチーム
