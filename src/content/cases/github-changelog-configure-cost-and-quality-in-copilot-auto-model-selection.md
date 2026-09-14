---
type: announcement
title: GitHub Copilotのモデル自動選択にコスト/品質の3段階ティアを追加
title_original: Configure cost and quality in Copilot auto model selection
company: GitHub
industry: cross-industry
cloud: []
patterns:
- multi-model-routing
components:
- GitHub Copilot
outcome:
  type: cost
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-14-configure-cost-and-quality-in-copilot-auto-model-selection
published_at: '2026-09-14'
---

## 概要

GitHub Copilotの自動モデル選択機能に「efficiency（低コスト優先）」「balance（コスト・品質・速度のバランス）」「intelligence（品質優先）」の3ティアが追加された。同じモデル群の中からプロンプトごとに最適なモデルを選ぶ点は変わらず、簡単なタスクはintelligenceティアでも小型モデルが選ばれることがある。

## 設計のポイント

- 利用可能なモデル群は全ティア共通とし、ティアはあくまで選択の重み付けを変えるだけに留める
- プロンプト単位で個別に評価してモデルを選択し、ティアに関わらずタスクの単純さに応じて小型モデルも使う
- 課金はティアではなく実際に選ばれたモデルに基づいて行い、透明性を保つ

## 使いどころ

- コストを抑えたい定型タスクと、品質を優先したい複雑なタスクが混在する開発チーム
- モデル選択の運用ポリシーをユーザーごとに変えたい組織
