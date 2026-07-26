---
type: guidance
title: LlamaDeployとSolaceイベントメッシュで本番運用向けエージェント基盤を10分構築
title_original: Configuring Solace as LlamaDeploy's event broker
industry: cross-industry
cloud: []
patterns:
- event-driven
- multi-agent-orchestration
components:
- LlamaDeploy
- Solace Event Broker
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/configuring-solace-as-llamadeploy-s-event-broker
published_at: '2026-07-19'
---

## 概要

LlamaDeploy（旧llama-agents）は非同期イベントでAIエージェント間の情報伝達を行うマルチサービス構成のデプロイフレームワークで、Solaceのイベントメッシュ型ブローカーと統合された。ノートブックで組んだワークフローをほぼ変更なしに本番相当のエージェントサービスへ移行でき、Solace導入により信頼性・速度・デプロイ容易性が向上する。

## 設計のポイント

- エージェント間通信を同期呼び出しではなく非同期イベントで設計し、サービス追加・スケールを疎結合に保つ
- イベントブローカーをプラガブルにし、Solaceのようなプロダクション実績のあるイベントメッシュに差し替え可能にする

## 使いどころ

- 不正検知や業務自動化など、複数のAIエージェントをまたぐビジネスクリティカルな処理を本番運用したい場合
- ノートブックでの検証からプロダクション化までの移行コストを最小化したいチーム
