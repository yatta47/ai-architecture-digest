---
type: opinion
title: LangChain創業2年の振り返り：ライブラリから「LangChain・LangGraph・LangSmith」の3製品体制へ
title_original: LangChain's Second Birthday
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- multi-agent-orchestration
- human-in-the-loop
components:
- LangChain
- LangGraph
- LangSmith
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langchain-second-birthday
published_at: '2026-08-26'
---

## 概要

LangChainがOSSライブラリ公開から2年を振り返り、単一パッケージから「langchain・LangGraph・LangSmith」の3製品体制の企業へと進化した経緯を語る。LLMプロバイダが3社から70社超・統合700件超へと拡大する中で、開発者の課題が『とにかく始める』から『本番で信頼性高く動かす』へ移行したことが、可観測性/評価基盤LangSmithと柔軟なエージェント制御基盤LangGraphの開発を後押しした。

## 設計のポイント

- LangSmithは可観測性（どこで失敗しているかの特定）と評価（リグレッション防止・継続的改善）の2本柱を軸に設計し、本番運用でのデバッグと品質改善を分離して扱う。
- 既製のchainや事前設定エージェントは柔軟性・信頼性に欠けるという顧客フィードバックを受け、LangGraphでは『厳密なワークフロー〜自律的エージェント』までの自由度を開発者が選べるオーケストレーション設計にした。
- LangGraphにhuman-in-the-loopとモデレーションループを組み込み、エージェントの挙動に対する制御性を高めて本番信頼性を担保する。
- 主要パートナー向けに専用integrationパッケージと標準テストを整備し、700以上に拡大した統合の品質を維持する。

## 使いどころ

- LLMアプリのプロトタイプから本番運用への移行期にあり、可観測性・評価基盤が必要なチーム。
- 既製の固定chainやプリセットエージェントでは柔軟性・信頼性が不足していると感じている開発者。
- 複雑なタスクをこなすエージェントに対して、人間の介入や制御を組み込みたいエンタープライズ。
