---
type: case
title: ハーネス改善のみでTerminal Bench順位をTop30からTop5へ
title_original: Improving Deep Agents with harness engineering
company: LangChain
industry: cross-industry
cloud: []
patterns:
- ai-agent
- eval
- llmops
components:
- Deep Agents
- LangSmith
- Terminal Bench 2.0
- Harbor
- Daytona
outcome:
  type: quality
source_id: langchain-blog
source_name: LangChain Blog
source_url: https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering
published_at: '2026-10-13'
---

## 概要

モデルをgpt-5.2-codexに固定し、システムプロンプト・ツール・ミドルウェアだけを調整してTerminal Bench 2.0で52.8%から66.5%へ改善した。トレース解析をSkill化し、並列の分析エージェントで失敗要因を集約した。

## 設計のポイント

- モデルを固定しハーネスのみを変えて効果を切り分ける。
- LangSmithのトレースを解析するSkillで改善ループを反復可能にする。
- 特定タスクへの過適合を避ける。

## 使いどころ

- コーディングエージェントの精度を上げたい開発チーム。
