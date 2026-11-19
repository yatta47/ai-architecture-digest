---
type: announcement
title: Copilotコードレビューの成果をリポジトリ単位で可視化
title_original: Track Copilot code review outcomes in Repository insights
company: GitHub
industry: cross-industry
cloud: []
patterns:
- eval
- ci-cd
components:
- GitHub Copilot code review
- Repository insights
- Copilot usage metrics API
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-17-track-copilot-code-review-outcomes-in-repository-insights
published_at: '2026-11-17'
---

## 概要

リポジトリのInsightsに、Copilotコードレビューの指摘が実際に対応されたかを示すページが追加された。対応済みコメント数、人間レビュアーの後続変更要求の有無、Copilot未レビューのマージなどを見られる。同指標はusage metrics APIでも取得できる。

## 設計のポイント

- 指摘の対応率を分子・分母・評価不能除外付きで示し、AIレビューの有効性を測る。
- 人間の後続変更要求の有無を併せて見て、AIレビューの見落としを推定する。
- Copilot未レビューでマージされたPRを出し、適用範囲の穴を見つける。

## 使いどころ

- AIコードレビュー導入後の効果測定をしたい開発組織。
- リポジトリ別に展開の優先度を決めたいエンタープライズ管理者。
