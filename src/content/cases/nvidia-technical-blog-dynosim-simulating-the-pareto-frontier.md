---
type: case
title: 'DynoSim: Dynamo推論スタックの構成探索を高速シミュレーションで代替'
title_original: 'DynoSim: Simulating the Pareto Frontier'
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- inference-optimization
- llmops
- eval
components:
- NVIDIA Dynamo
- DynoSim
- AI Configurator
- vLLM
- SGLang
- KVBM
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/dynosim-simulating-the-pareto-frontier/
published_at: '2026-06-11'
---

## 概要

LLMサービングはバックエンド・並列化形状・スケジューラ・ルーティング・KVキャッシュなど相互作用する多数の選択肢を持ち、大規模モデルでは1回の実測実験にも多数のGPUが必要になる。NVIDIAはDynamoサービングスタックのデジタルツインであるDynoSimを構築し、実測したフォワードパス時間・スケジューラ・ルーター・プランナーの挙動を離散イベントシミュレーションとして仮想時間軸上で合成することで、実時間の約1500倍の速度でPareto最適構成を探索し、GPUを消費する前に候補を絞り込めるようにした。

## 設計のポイント

- 1つの巨大なモデルではなく、ワークロードリプレイ・単一エンジンシミュレーション・複数エンジンシミュレーションを同じ離散イベントタイムライン上で合成可能な部品として設計する
- AI Configuratorによるフォワードパス時間の実測ベース推定と、バックエンド固有のスケジューラシミュレーション(vLLMのpreemption/recompute、SGLangのradix-cache-aware admissionなど)を分離し、それぞれの忠実度を独立に高める
- ルーター・プランナー・KVBMなど本番でオンライン判断するコンポーネントを、実際のフィードバックループとして同一イベントキュー上でモデル化する

## 使いどころ

- 本番投入前に大規模GPUクラスタでの実験を減らし、構成探索のGPUコストを抑えたいLLMサービング基盤チーム
- ルーターのコスト関数やキャッシュポリシーなど、アルゴリズム変更の効果を実機なしで事前評価したい研究者
