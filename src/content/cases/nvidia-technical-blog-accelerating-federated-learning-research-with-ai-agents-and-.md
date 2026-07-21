---
type: case
title: NVIDIA FLARE Auto-FL:AIエージェントで連合学習のアルゴリズム探索を自動化・再現可能にする
title_original: Accelerating Federated Learning Research with AI Agents and NVIDIA FLARE Auto-FL
company: NVIDIA
industry: cross-industry
cloud: []
patterns:
- ai-agent
- guardrails
- eval
components:
- NVIDIA FLARE
- Auto-FL
outcome:
  type: speed
source_id: nvidia-technical-blog
source_name: NVIDIA Technical Blog
source_url: https://developer.nvidia.com/blog/accelerating-federated-learning-research-with-ai-agents-and-nvidia-flare-auto-fl/
published_at: '2026-07-06'
---

## 概要

NVIDIA FLARE Auto-FLは、program.mdという『研究の制御プレーン』でAIエージェントの変更範囲を拘束し、固定のベンチマーク契約と実験台帳(results.tsv)によって連合学習(FL)アルゴリズムの探索を再現可能かつ比較可能な形で自動化する仕組み。FedAvgやSCAFFOLDなど複数の集約戦略や境界付きアーキテクチャ探索を、公平な基準の上でエージェントに反復させる。

## 設計のポイント

- エージェントが変更できる範囲をmutation_schema.yamlで境界付け、FLのプロトコル契約(サーバー・クライアント間の意味論)を壊さないようにする
- 全ての候補実行をresults.tsvという実験台帳に記録し、採用・却下の判断をログとして追跡できる形にする
- 固定の学習予算と一貫したスコアリングを持つベンチマークから出発することで、候補間の比較を公平かつ意味のあるものにする

## 使いどころ

- 多数の集約アルゴリズムやハイパーパラメータを試行錯誤したい連合学習の研究者
- AIエージェントに研究ループを任せつつ、人は問いの設定と予算管理・レビューに専念したいチーム
