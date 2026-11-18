---
type: announcement
title: LangSmithがコーディングエージェントの支出をPR成果に紐づけて可視化
title_original: 'LangSmith for Coding Agents: Now track spend by outcome'
company: LangChain
industry: cross-industry
cloud: []
patterns:
- llmops
- eval
- cost-optimization
components:
- LangSmith
- Claude Code
- Codex
- GitHub
- GitLab
outcome:
  type: cost
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/langsmith-coding-agents-roi
published_at: '2026-11-18'
---

## 概要

LangSmithは新概念「outcomes」でGitHubのPRやGitLabのMRをスレッドに紐づけ、コーディングエージェントのトレース単位のコストをPRに帰属させる機能を発表した。マージされたPRあたりのコストや、PRに結びつかなかった支出を把握できる。

## 設計のポイント

- トレースのコストを成果物（PR）へ帰属させ、使用量ではなくROIで評価する。
- 1スレッドが複数PRを生む／1PRが複数スレッドにまたがる関係を前提に帰属を設計する。
- エージェント種別ごとに専用ダッシュボードと評価軸を持たせる。

## 使いどころ

- コーディングエージェントのAI予算のROIを説明したいエンジニアリング責任者。
- モデルやポリシー変更が1PRあたりコストに与える影響を比較したいチーム。
