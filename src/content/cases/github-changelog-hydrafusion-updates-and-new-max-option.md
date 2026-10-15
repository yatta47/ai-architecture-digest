---
type: announcement
title: 複数モデルを組み合わせて応答するHydraFusionの更新とMax
title_original: HydraFusion updates and new Max option
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
- multi-agent-orchestration
- parallel-execution
- ai-agent
components:
- HydraFusion
- GitHub Copilot
- VS Code
- Copilot CLI
- Claude Opus 5.5
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-10-14-hydrafusion-updates-and-new-max-option
published_at: '2026-10-14'
---

## 概要

GitHub Copilotの複数モデル協調機能HydraFusionが更新され、上位モデルを使うMaxが加わった。CascadeとCritiqueのワークフローを改善し、下書きは中程度、レビューは高い推論強度にするなど段階別に調整する。

## 設計のポイント

- 下書きは中程度、レビューは高い推論強度と段階ごとに使い分ける
- Cascadeは判定ステップを置き、必要時のみ修正させる
- Critiqueは並列の批評モデルが作業領域をツールで直接検査する

## 使いどころ

- 速度・コスト・品質のバランスをモデル選択なしで取りたいCopilot利用者
