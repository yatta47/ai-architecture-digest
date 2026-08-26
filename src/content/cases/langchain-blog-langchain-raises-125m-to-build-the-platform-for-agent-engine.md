---
type: announcement
title: LangChainがエージェントエンジニアリング基盤の1.0リリースと125億円規模の資金調達を発表
title_original: LangChain raises $125M to build the platform for agent engineering
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- llmops
- eval
- human-in-the-loop
components:
- LangChain
- LangGraph
- LangSmith
- Insights Agent
- Agent Builder
outcome:
  type: reliability
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/series-b
published_at: '2026-08-26'
---

## 概要

LangChainはIVP主導で1.25億ドルを調達し（評価額12.5億ドル）、LangChainとLangGraphの1.0リリース、LangSmith Observabilityの新機能Insights Agent、ノーコードのAgent Builder（プライベートプレビュー）を発表した。プロトタイプは容易だが本番化が難しいエージェントを、構築からオブザーバビリティ・評価・デプロイまで一貫して支援する「agent engineering」向け統合プラットフォームを目指すとしている。

## 設計のポイント

- LangGraphのランタイム上でlangchainを再設計し、低レベルのオーケストレーション・メモリ管理・human-in-the-loop・長時間タスク向けのdurable executionを提供する。
- LangSmithを構築フレームワークから独立させ、本番トレースデータを使った継続的な評価・改善のループ（observability→evaluation→deployment）として位置付ける。
- Insights Agentがエージェントの挙動パターンを自動分類し、大量トレースからの異常検知・傾向把握を人手を介さず行えるようにする。
- 特定モデルベンダーへのロックインを避け、任意のモデルプロバイダを選べる設計方針を維持する。

## 使いどころ

- エージェントをプロトタイプから本番運用に移す際に、信頼性の検証・継続的な評価基盤が必要なAI開発チーム。
- 長時間実行や人間の承認を挟む必要がある複雑なエージェントワークフローを構築する開発者。
- コードを書かずにエージェントを試作・展開したいビジネスユーザーやドメイン担当者。
- 複数のモデルプロバイダを併用・比較しながらエージェントを運用したい組織。
