---
type: announcement
title: LangSmithのエージェント開発基盤群(Interrupt 2026発表まとめ)
title_original: Everything we shipped at Interrupt
company: LangChain
industry: cross-industry
cloud:
- multi-cloud
patterns:
- llmops
- multi-agent-orchestration
- eval
- context-engineering
components:
- LangSmith Engine
- SmithDB
- Managed Deep Agents
- LangSmith Sandboxes
- Context Hub
- Apache DataFusion
- LLM Gateway
outcome:
  type: productivity
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/interrupt-2026-overview
published_at: '2026-06-05'
---

## 概要

LangChainはカンファレンスInterruptで、エージェント開発ライフサイクルを加速する一連の新製品を発表した。本番トレースを監視し障害をクラスタリングして修正PRを自動生成する「LangSmith Engine」、Rust製の高速トレース基盤「SmithDB」、Deep Agentsをホスト実行できる「Managed Deep Agents」、隔離コード実行環境「LangSmith Sandboxes」のGA、エージェントの指示・ポリシーを一元管理する「Context Hub」などが含まれる。いずれもLangSmithの既存のトレーシング・評価基盤の上に構築されている。

## 設計のポイント

- 本番トレースの監視から障害クラスタリング、根本原因診断、修正PR生成、リグレッション防止用evalの追加までを自動化ループとして一体設計している。
- SmithDBはオブジェクトストレージ上のステートレスなRustサービス(Apache DataFusion/Vortex基盤)とし、コンピュートを足すだけでスケールしセルフホスト・マルチクラウドにも展開しやすくしている。
- Managed Deep AgentsはAGENTS.md・skills・subagentsといった既存のDeep Agents構造をそのままAPIでホスト実行できるようにし、独自にランタイムを構築させない。
- Context Hubでエージェントの指示やポリシーをコードとは別に高速に更新・共同編集できるようにし、非エンジニアの関係者も関与できるようにしている。

## 使いどころ

- 本番稼働中のエージェントで発生する障害を人手でトレースを読んで探すのではなく、自動的に検出・修正したいチーム。
- 長時間・大容量化するエージェントトレースを高速にクエリ・全文検索・スレッド復元したい観測基盤担当者。
- 計画立案・ツール利用・サブエージェント委譲を伴うDeep Agentsを、自前でランタイムを構築せず本番運用したい開発チーム。
- モデル生成コードや外部依存を安全に実行するため、隔離されたサンドボックス環境が必要なエージェント開発者。
