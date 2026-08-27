---
type: guidance
title: 信頼スコアに応じてAIエージェントの権限を段階的に伸縮させる「graduated autonomy」パターン
title_original: Closing the AI agent trust gap with graduated autonomy
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- policy-as-code
- guardrails
- ci-cd
components:
- Amazon Bedrock AgentCore
- Amazon DynamoDB
- AWS CodePipeline
- Cedar
outcome:
  type: risk-compliance
source_id: aws-architecture-blog
source_name: AWS Architecture Blog
source_url: https://aws.amazon.com/blogs/architecture/closing-the-ai-agent-trust-gap-with-graduated-autonomy/
published_at: '2026-08-26'
---

## 概要

「graduated autonomy」は、AIエージェントの権限を全許可か読み取り専用かの二択にせず、継続的な信頼度スコアに応じて段階的に拡大・縮小するアーキテクチャパターン。Bedrock AgentCoreがランタイム/ゲートウェイ/評価を提供し、DynamoDBが信頼状態を保持、CodePipelineが評価結果でデリバリーをゲートする6層構成で、可視性・判断の来歴・可逆性を実現する。

## 設計のポイント

- 安全性スコアは他の指標と平均化せず、常に独立した下限(フロア)として扱う
- 全エージェントは最も低い自律レベルから開始し、昇格は緩やかに、性能劣化時の降格は即座に行う
- 高速なプロセス内フィルタは単独で信頼せず、エージェントのプロセス外で強制されるCedarポリシーでバックストップする
- 実行後の監査記録に実行前の状態を残し、誤動作からの復旧(リバーシビリティ)を可能にする

## 使いどころ

- 顧客データの読み書きや返金・アカウント削除など高リスク操作を行うエージェントの権限管理
- モデル更新やプロンプト変更で挙動が変わりうるエージェントの自律度を運用中に継続調整したい場合
