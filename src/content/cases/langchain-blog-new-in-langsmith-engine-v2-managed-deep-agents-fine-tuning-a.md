---
type: announcement
title: 'LangSmith: Engine v2・Managed Deep Agents・Fine-Tuning'
title_original: 'New in LangSmith: Engine v2, Managed Deep Agents, Fine-Tuning, and More'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- ai-agent
- eval
- fine-tuning
- root-cause-analysis
- memory-consolidation
components:
- LangSmith
- LangSmith Engine
- Managed Deep Agents
- LangSmith Trajectories
- LangSmith Fine-Tuning
- Parallel
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-engine-agents-fine-tuning-trajectories
published_at: '2026-09-25'
---

## 概要

LangChainがInterrupt NYCでLangSmithの新機能を発表した。Engine v2は敵対的検証と修正の自動検証、Managed Deep Agentsはユーザー単位メモリと認証、TrajectoriesとFine-Tuningはセッションから学習データを作る流れを支える。

## 設計のポイント

- エージェント層とユーザー層でメモリを分離し、アクセスポリシーを各層で定義する。
- Engineが本番トレースから問題を特定し、修正を評価セットで検証してからPR化する。
- トレースを会話形のTrajectoriesにして、レビューや評価、SFTデータ化に使う。

## 使いどころ

- 本番エージェントの改善サイクルを自動化したいチーム。
- ユーザーごとの資格情報とメモリを分けたいマルチユーザーのエージェント運用。
