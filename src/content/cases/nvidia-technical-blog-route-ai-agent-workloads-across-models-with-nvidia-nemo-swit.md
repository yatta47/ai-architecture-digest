---
type: guidance
title: NeMo Switchyardによるエージェントワークロードのモデルルーティング設計
title_original: Route AI Agent Workloads Across Models with NVIDIA NeMo Switchyard
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- ai-agent
- cost-optimization
components:
- NVIDIA NeMo Switchyard
- NeMo switchyard-libsy
outcome:
  type: cost
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/route-ai-agent-workloads-across-models-with-nvidia-nemo-switchyard/
published_at: '2026-08-11'
---

## 概要

エージェントのタスクはステップごとに必要なモデル能力・コスト・レイテンシ特性が異なるため、常に最大モデルへ送ると過剰コストになり、常に小型モデルへ送ると精度が落ちる。NVIDIA NeMo Switchyardは、リクエストの分類・モデルの内部状態・システムシグナル(価格、レイテンシ、負荷)を組み合わせてタスクごとに最適なモデルへルーティングするプロバイダ非依存のオーケストレーション層を提供する。ルーティングロジックを特定プロバイダから分離することで、モデル入れ替え時にもアプリケーションを作り直す必要がない。

## 設計のポイント

- ルーティング判断をリクエスト内容の分類・モデル内部状態・システムシグナルの3系統の信号から構成する
- セマンティックなモデル名とプロバイダエンドポイントのマッピングを分離し、ルーティングロジックをプロバイダ非依存に保つ
- セッション単位でルーティング状態(ツール結果や過去の判断)を保持しつつ、不要な場合はステートレスにルーティングできる柔軟性を持たせる
- リクエスト単位・ターン単位・エージェント全体単位など粒度の異なるルーティング戦略を用途に応じて選べるようにする

## 使いどころ

- マルチステップのエージェントワークロードでモデルコストを最適化したいチーム
- フロンティアモデルと軽量モデルを併用しつつ、モデル切り替え時の実装変更を避けたい場合
- サブエージェントごとに異なるモデルプールを使い分けたい複雑なエージェントシステム
