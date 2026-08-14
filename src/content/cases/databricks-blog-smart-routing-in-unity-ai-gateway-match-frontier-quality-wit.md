---
type: case
title: Databricks Unity AI GatewayのSmart Routingでコーディングエージェントのモデルを自動最適化
title_original: 'Smart routing in Unity AI Gateway: match frontier quality with 30%+ lower cost per task'
company: Databricks
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- cost-optimization
- llmops
components:
- Unity AI Gateway
- Claude Code
- Codex
- Omnigent
- Opus 5
outcome:
  type: cost
source_id: databricks-blog
source_name: Databricks Blog
source_url: https://www.databricks.com/blog/smart-routing-unity-ai-gateway-match-frontier-quality-30-lower-cost-task
published_at: '2026-08-13'
---

## 概要

Databricksは、コーディングタスクの多くが最上位モデルを必要としないという知見をもとに、セッション開始時にタスクの複雑さを分類し適切なモデル階層に自動ルーティングするSmart RoutingをUnity AI Gatewayにベータ提供した。Claude CodeやCodexに直接組み込まれ、内部ベンチマークでOpus 5相当の性能をコストの65%で、公開ベンチマークでは半分未満のコストで達成したという。

## 設計のポイント

- リクエスト単位のルーティングはキャッシュヒット率を壊しコストを増やすため、セッション開始時に1回だけ分類するタスク単位ルーティングを採用する
- 分類には安価で低レイテンシなモデルを使い、タスク説明のみから複雑度ラベルを抽出することでルーティング自体のコストを抑える
- デフォルトを中位モデルとし、フロンティア級の知識が必要な場合のみ上位モデルへエスカレーション、簡単なタスクは下位モデルへ委譲する単一ポリシーを全タスクに適用する
- モデル選択だけでなくコーディングハーネス(Omnigent)の選択まで含めて最適化し、開発者がモデルもハーネスも都度選ばずに済むようにする

## 使いどころ

- 大量のコーディングタスクで毎回最上位モデルを使いコストが膨らんでいる開発組織
- モデルの選択肢が多すぎて開発者が毎回選定に時間を取られている(choice overload)状況
- キャッシュヒット率を維持しながらコストとレイテンシを両立させたいプラットフォームチーム
