---
type: case
title: StripeがDeep Agentsで全社向けナレッジAIエージェントKaiを1週間で構築
title_original: 'How Stripe Built their Knowledge AI Platform: A Company-Wide AI Agent on Deep Agents, Live in 1 Week'
company: Stripe
industry: financial-services
cloud:
- aws
patterns:
- ai-agent
- context-engineering
- memory-consolidation
- unified-runtime
components:
- LangChain
- LangGraph
- Deep Agents
- Amazon S3
- Slack
- Google Suite
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/how-stripe-built-their-knowledge-ai-platform-on-deep-agents
published_at: '2026-08-03'
---

## 概要

Stripeは非エンジニア従業員も含む全社員向けの常時稼働エージェント「Kai」を、LangChainのオープンソースエージェントハーネスDeep Agents上に構築した。ツール呼び出しループやミドルウェア、状態管理をDeep Agentsに任せることで、社内固有の統合層に集中でき初期版を1週間で本番投入した。

## 設計のポイント

- Deep Agentsを基盤層、その上にStripe固有のセキュリティ・インフラ統合層、さらに上にチームごとのカスタムエージェント設定層を重ねる3層アーキテクチャにする
- S3を裏側に持つ仮想ファイルシステムでセッション間のコンテキストを永続化し、サンドボックス実行前後で同期する「sync in/sync out」パターンを使う
- コード実行はエージェント本体の外にあるサンドボックスをツールとして呼び出す形にし、実行境界を分離してLLM生成コードのリスクを抑える
- 長時間の多ターンセッションではサマライズ用ミドルウェアの閾値やモデルをチューニングし、キャッシュヒット率とコストのバランスを取る

## 使いどころ

- 非エンジニアにコーディングエージェント相当の生産性ツールを提供したい全社プラットフォームチーム
- 100チーム規模で分散管理されるスキル/ツールを1つのエージェント基盤に集約したいケース
- 本番運用に耐えるエージェントハーネスをゼロから作る代わりに既存OSSで速く立ち上げたいチーム
