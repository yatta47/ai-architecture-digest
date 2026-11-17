---
type: guidance
title: 製造業の知見から整理したマルチエージェント設計パターンとアンチパターン
title_original: Taxonomy of multi-agent design patterns, anti-patterns, and lessons from manufacturing
company: AWS
industry: manufacturing
cloud:
- aws
patterns:
- multi-agent-orchestration
- ai-agent
- human-in-the-loop
components: []
outcome:
  type: reliability
source_id: aws-machine-learning-blog
source_name: AWS Machine Learning Blog
source_url: https://aws.amazon.com/blogs/machine-learning/taxonomy-of-multi-agent-design-patterns-anti-patterns-and-lessons-from-manufacturing/
published_at: '2026-11-16'
---

## 概要

マルチエージェントの協調は分散システムの問題だとして、制御フローを人が定めるTier 1とモデルが実行時に決めるTier 2に分けてパターンを整理する。製造業のタクトタイムや安全境界を踏まえ、アンチパターンも示す。

## 設計のポイント

- まず決定的なTier 1から始め、サブタスクが動的に生じる場合のみTier 2に移す。
- ステップ連鎖の信頼性は積で劣化するため、段数と引き継ぎを最小化する。
- タクトタイム、安全境界、エッジデータ、シフトサイクルを設計制約に含める。

## 使いどころ

- マルチエージェント化の要否を判断するアーキテクト。
- 製造現場にエージェントを導入するチーム。
