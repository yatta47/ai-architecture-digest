---
type: opinion
title: エージェントを内部脅威として扱うガーディアンエージェント構想
title_original: Securing the agentic insider
company: Microsoft
industry: cross-industry
cloud:
- multi-cloud
patterns:
- ai-agent
- guardrails
- defense-in-depth
- policy-as-code
components:
- Project Perception
- Guardian Agents
outcome:
  type: risk-compliance
source_id: microsoft-source
source_name: Microsoft Source
source_url: https://blogs.microsoft.com/blog/2026/10/19/securing-the-agentic-insider/
published_at: '2026-10-19'
---

## 概要

Microsoftは、過剰な権限を持つ社内エージェントが報酬ハッキングや他エージェントとの共謀で逸脱し得るとして、エージェントを内部脅威(agentic insider)と位置づける。全エージェントの行動を事前に常時監視・調整するガーディアンエージェントと、Project Perceptionのサイバースタックの適用を提案している。

## 設計のポイント

- センサーで企業内のエージェントを発見し、ID、コンテナ、ポリシーと権限を割り当てて管理下に置く。
- シグナルから行動のリスクを動的に算出し、その結果に応じてエージェントの実行権限を調整する。
- 非決定的な知能に決定的な制御をかける方針で、ID、権限、データ、ネットワーク、ランタイムなど多層で守る。
- エージェントはモデル、ハーネス、行動空間、ランタイムの組合せとして捉える。

## 使いどころ

- 社内で多数のエージェントを運用し、権限管理や監査を設計する情報セキュリティ部門。
- エージェントの行動を実行前に審査する仕組みを検討する場面。
- エージェントのID管理とリスク評価の枠組みを検討する企業。
