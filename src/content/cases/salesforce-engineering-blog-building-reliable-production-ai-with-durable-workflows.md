---
type: case
title: Agentforce Gridを支える耐久性ワークフローによる本番AI実行基盤
title_original: Building Reliable Production AI with Durable Workflows
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- durable-workflow-orchestration
- parallel-execution
- llmops
components:
- Agentforce Grid
outcome:
  type: reliability
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/building-reliable-production-ai-with-durable-workflows/
published_at: '2026-07-27'
---

## 概要

Salesforceは数千行にAI出力を生成するAgentforce Gridの開発を通じ、本番AIの信頼性はプロンプトの巧拙ではなく実行状態の管理にあると学んだ。列全体の実行を1つの巨大ジョブとして扱うのではなく、列→行/バッチ→アクティビティという階層で回復可能な実行単位を定義し、ワーカー再起動やデプロイ中の失敗からも安全に再開できる設計にした。

## 設計のポイント

- リトライの境界は『再現可能な作業の最小単位』に置くべきで、粒度が粗すぎると成功済みの呼び出しまで再実行し、細かすぎるとオーケストレーションのオーバーヘッドが増える
- 実行を階層構造（全体ジョブ→行/バッチ→アクティビティ）でモデル化し、失敗を局所化して無関係な作業を巻き込まないようにする
- モデル呼び出しの成功・失敗だけでなく『どこまで完了したか』という実行状態そのものを永続化して可視化する

## 使いどころ

- 数千件規模のレコードに対しAIモデル呼び出しを並列実行するバッチ/エージェント基盤を設計するチーム
- デプロイやワーカー再起動を挟んでも長時間実行のAIワークフローを安全に再開したいプラットフォームエンジニア
