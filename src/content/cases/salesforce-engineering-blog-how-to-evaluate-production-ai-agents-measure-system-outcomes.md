---
type: guidance
title: AIエージェント評価は会話ではなくシステムの状態変化で測るべき
title_original: 'How to Evaluate Production AI Agents: Measure System Outcomes, Not Conversations'
company: Salesforce
industry: cross-industry
cloud: []
patterns:
- eval
- ai-agent
components:
- CRMAgentBench
outcome:
  type: reliability
source_id: salesforce-engineering-blog
source_name: Salesforce Engineering Blog
source_url: https://engineering.salesforce.com/how-to-evaluate-production-ai-agents-measure-system-outcomes-not-conversations/
published_at: '2026-08-17'
---

## 概要

本番AIエージェントは会話が正しく見えても、実際にはツール呼び出しが行われずシステム状態が変わっていないことがある。SalesforceはCRMAgentBenchで、会話内容ではなくCRMの最終状態や許可されたツール・引数・実行順序をすべて満たすかを厳格に採点し、さらにpass^kで複数回実行時の安定した成功率を測定する手法を提示する。

## 設計のポイント

- 会話の応答内容ではなく、ツール呼び出し後のシステムの最終状態を検証の根拠にする
- 正しいツール・引数・実行順序・禁止操作の不在をすべて満たす場合のみ成功とする全か無かの採点にする
- pass@kではなくpass^kを用い、複数回の独立試行すべてで成功する確率を測ることで安定性を評価する
- キャンペーンIDを意図的に伏せるなど、推測では解けないタスクを混ぜて発見・確認行動を検証する

## 使いどころ

- 顧客の請求・予約・レコード更新など実システムを変更する本番AIエージェントの評価基盤を設計するチーム
- 会話ログだけでは検出できない『言ったのにやっていない』失敗を防ぎたい場合
- エージェントの一発成功率ではなく、繰り返し利用時の信頼性を保証したいプロダクトオーナー
