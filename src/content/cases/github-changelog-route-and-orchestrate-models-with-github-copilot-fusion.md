---
type: announcement
title: タスクごとにモデルを自動選択・協調させるCopilot Fusion
title_original: Route and orchestrate models with GitHub Copilot Fusion
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- multi-agent-orchestration
- cost-optimization
components:
- GitHub Copilot Fusion
- GitHub Copilot CLI
- VS Code
outcome:
  type: cost
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-28-route-and-orchestrate-models-with-github-copilot-fusion
published_at: '2026-10-28'
---

## 概要

GitHub Copilot Fusionが一般提供となり、開発者はモデルを選ばず、システムがタスクごとにモデルのルーティングと協調を行う。Single/Cascade/Critiqueの3つのワークフローを使い分け、Artificial Analysis Coding Agent Indexで上位モデルに迫るスコアを約半分のコストで達成したとされる。

## 設計のポイント

- 努力レベル(Standard/High/Max)だけをユーザーに公開し、モデル選択は内部ルーティングに隠蔽する。
- 安価なモデルで下書きし品質チェックで上位モデルへ昇格するCascade、別モデルがレビューして修正するCritiqueを使い分ける。
- 利用可能モデルは組織のモデルポリシーに従い、管理者がFusion用に個別に無効化できる。

## 使いどころ

- モデル切替の手間と過剰スペック選択によるコストを減らしたい開発組織。
- 管理者がモデル利用範囲を統制しつつ既定モデルを配布したい企業。
