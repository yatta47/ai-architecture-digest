---
type: case
title: Claude Fable 5の自己検証機能で一晩中エージェントを走らせる楽天
title_original: 'Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5'
company: Rakuten
industry: retail
cloud: []
patterns:
- ai-agent
- multi-agent-orchestration
- memory-consolidation
components:
- Claude Code
- Claude Cowork
- Claude Platform
- Claude Managed Agents
- Slack
- Microsoft Teams
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-07-20-ai-credit-pools-for-cost-centers-in-the-billing-ui
published_at: '2026-07-20'
---

## 概要

楽天はClaude Codeでの開発支援に続き、営業・マーケティング・財務など全社の業務にClaude Managed Agentsを1週間で展開した。Claude Fable 5は自己検証・自己反省を頻繁に行い、実行途中で誤った前提に気づいて自ら修正できるため、数時間〜終日かかるタスクを人の監視なしに任せられるようになった。

## 設計のポイント

- モデルが自らのミスに気づき軌道修正できることで、委任の単位が「タスク」から「意思決定」へと変わり、細かくタスク分割する必要が減る。
- セッションをまたいだメモリで過去の失敗を記憶し、同じ間違いを繰り返さないようにする。
- タスク完了率とタスクあたりコストを併せて計測し、追加の能力が必要な仕事だけにFable 5を割り当てるコスト配分を行う。

## 使いどころ

- 数時間〜終日かかる長時間タスクを人の監視なしにエージェントへ委任したいエンタープライズ。
- Slack/Teamsや社内タスクシステムに繋がった業務横断エージェントを短期間で全社展開したい組織。
