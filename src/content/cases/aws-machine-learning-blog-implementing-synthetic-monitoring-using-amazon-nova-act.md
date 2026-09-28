---
type: case
title: 画面を見て判断するエージェント型シンセティックモニタリング（Nova Act×AgentCore）
title_original: Implementing synthetic monitoring using Amazon Nova Act
industry: cross-industry
cloud:
- aws
patterns:
- ai-agent
- event-driven
components:
- Amazon Nova Act
- Amazon Bedrock AgentCore
- Amazon Bedrock AgentCore Browser
- Amazon EventBridge Scheduler
- Amazon SNS
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/implementing-synthetic-monitoring-using-amazon-nova-act/
published_at: '2026-09-28'
---

## 概要

セレクタベースのUI自動化に代わり、マルチモーダルLLMがスクリーンショットを見て操作するAmazon Nova Actで、ログインや購入導線などの重要なユーザージャーニーを定期的に検証する構成。EventBridge SchedulerでAgentCore Runtime上のエージェントを定期起動し、失敗時はSNSで即座に通知する。

## 設計のポイント

- DOMセレクタではなく画面のスクリーンショットを見て操作するNova Actにより、UI変更に対する耐性を高めセレクタ保守コストを削減する。
- AgentCore Runtimeでサーバーレスにエージェントを実行し、AgentCore Browserで各テスト実行ごとに隔離されたリモートブラウザ環境を使い捨てで用意する。
- EventBridge SchedulerのUniversal TargetからInvokeAgentRuntimeを直接呼び出し、5分〜1時間の間隔でジャーニーの重要度に応じたスケジュールを組む。

## 使いどころ

- ECサイトの検索・カート・決済など、バックエンド指標だけでは検知できないユーザー体験レベルの障害を早期発見したい場合。
- 金融・旅行・SaaS・医療など、ログインや予約、申込フローの継続的な健全性確認が必要な業種。
