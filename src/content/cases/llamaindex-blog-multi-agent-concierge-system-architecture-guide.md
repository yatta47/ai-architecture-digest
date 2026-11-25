---
type: guidance
title: 依存関係のあるタスクを捌くマルチエージェント・コンシェルジュ設計
title_original: Building a Multi-Agent Concierge System
company: LlamaIndex
industry: cross-industry
cloud: []
patterns:
- multi-agent-orchestration
- ai-agent
components:
- LlamaIndex
outcome:
  type: reliability
source_id: llamaindex-blog
source_name: LlamaIndex Blog
source_url: https://www.llamaindex.ai/blog/building-a-multi-agent-concierge-system
published_at: '2024-07-17'
---

## 概要

銀行業務を例に、タスクごとのエージェントと案内・振り分け・継続の3つのメタエージェントを組み合わせたオープンソースのチャットシステムを解説する。認証や残高確認といった前提タスクは共有状態と会話履歴をもとに連鎖実行する。

## 設計のポイント

- 巨大な単一プロンプトを避け、トップレベルのタスクごとにエージェントを分ける。
- 振り分け役は利用者に返答せず、担当エージェント名だけを返してコードがルーティングする。
- 継続エージェントが元の依頼を会話履歴から復元し、次の依頼を自動で発行する。
- 全エージェントで利用者の状態を共有する。

## 使いどころ

- 多数のツールと依存関係を持つ顧客対応ボットの設計。
- 単一エージェントのプロンプトが肥大化しているチーム。
