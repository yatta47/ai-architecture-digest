---
type: announcement
title: GitHub Copilotクラウドエージェント、モデルの推論レベルをタスク単位で選択可能に
title_original: Customize the reasoning level for Copilot cloud agent
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
- inference-optimization
components:
- GitHub Copilot cloud agent
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-03-customize-the-reasoning-level-for-copilot-cloud-agent
published_at: '2026-08-03'
---

## 概要

GitHub Copilotクラウドエージェントにタスクを委任する際、対応モデルであれば推論レベルを選択できるようになった。推論レベルを上げると複雑な問題への回答精度は向上するが、トークン消費量とクレジット消費が増える。Copilot Pro、Pro+、Business、Enterpriseなどクラウドエージェントを含む有料プラン全体で利用できる。

## 設計のポイント

- モデル選択とは別に推論レベルという独立したパラメータを設けることで、精度とコストのトレードオフをタスク単位で調整可能にしている
- 推論レベルはタスク開始時にモデルと合わせて指定し、そのランの間固定して使用する設計になっている
- 高い推論レベルほどトークン消費・クレジット消費が増えることを明示し、コスト意識を持った使い分けを促している

## 使いどころ

- 複雑な設計判断やデバッグなど高精度な回答が必要なタスクでは推論レベルを上げて品質を優先する
- 定型的で単純なタスクでは推論レベルを下げてクレジット消費を抑えたい開発者・チームに有効
- エンタープライズなどコスト管理が重要な組織で、タスクの難易度に応じたモデル運用ポリシーを設計する際の参考になる
