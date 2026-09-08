---
type: case
title: モデル/ハーネスルーティングによるコーディングエージェントのコスト削減
title_original: How I cut coding agent costs with model and harness routing
company: Arize
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- multi-model-routing
- cost-optimization
components:
- Opus 5
- Kimi K3 Max
- GPT-5.6 Sol
- GLM 5.2 Max
- Composer 2.5
outcome:
  type: cost
source_id: arize-blog
source_name: Arize Blog
source_url: https://arize.com/blog/how-i-cut-coding-agent-costs-with-model-harness-routing/
published_at: '2026-09-08'
---

## 概要

Arizeのエンジニアが、コーディングエージェントのタスクを計画・探索・実装・レビューに分解し、判断が必要な工程だけフロンティアモデルに絞ってそれ以外を低コストモデルにルーティングすることで、日次のバグ発見Slackボットのコストを1回あたり約100ドルから15〜20ドルに削減した実験を紹介する。

## 設計のポイント

- フロンティアオーケストレーター+低コストサブエージェント、または低コストオーケストレーター+フロンティアアドバイザーの2パターンで役割分担する
- 計画・不確実性の解消・高リスク変更前など判断が必要な工程だけにフロンティアモデルの利用を絞る
- モデル単価ではなく「cost per accepted task」で成功タスクあたりの実コストを測定し、ハーネスの挙動差も比較する

## 使いどころ

- 定型的なコーディングタスクを反復実行するワークフローでAI予算を最適化したいチーム
- フロンティアモデルのフル活用が費用的に見合わない大規模スキャン・調査タスク
