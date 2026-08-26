---
type: announcement
title: 長時間稼働・ステートフルなAIエージェントを展開・管理するLangGraph Platformが正式提供開始
title_original: 'LangGraph Platform is now Generally Available: Deploy & manage long-running, stateful Agents'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- human-in-the-loop
- llmops
components:
- LangGraph Platform
- LangGraph Studio
- LangSmith
- GitHub
outcome:
  type: speed
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langgraph-platform-ga
published_at: '2026-08-26'
---

## 概要

LangChainは長時間稼働・ステートフルなエージェントのデプロイと運用に特化したLangGraph Platformを正式提供開始した。1クリックデプロイ、水平スケーリング、メモリ・会話履歴を保持する永続化レイヤー、デバッグ用のLangGraph Studioを備え、ベータ期間中に約400社が本番導入した。Cloud/Hybrid/フルセルフホストの3形態で提供され、データ機密性の要件に応じて選択できる。

## 設計のポイント

- 永続化レイヤーでメモリ・会話履歴・人間参加型(human-in-the-loop)や他エージェント待ちなど非同期コラボレーションの状態を保持し、不確実なタイミングのイベントに耐える設計とする
- チェックポイント機構により失敗箇所からのリワインド・編集・再実行を可能にし、長時間タスクの途中失敗に対する耐障害性を高める
- Remote Graphsとして他のエージェントを呼び出す分散型マルチエージェントアーキテクチャを構成できるようにする
- 管理コンソールでエージェントのバージョン管理(assistants)・レジストリ・RBAC/ワークスペースを一元化し、組織横断でのガバナンスを担保する

## 使いどころ

- deep researchエージェントやスケジュール/イベント駆動でバックグラウンド実行される長時間タスクを本番運用したいチーム
- 人間の承認・入力待ちや複数エージェント間の非同期連携を伴うワークフローを安定運用したい場合
- データ機密性の要件に応じてSaaS・ハイブリッド・フルセルフホストを使い分けたいエンタープライズ
- 複数チームでエージェント開発が広がり、可視化・デバッグ・バージョン管理を横断的に統制したい組織
