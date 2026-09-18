---
type: announcement
title: Copilot impactダッシュボードが機能別エンゲージメントを可視化
title_original: Copilot impact dashboard now shows feature engagement
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- GitHub Copilot
- Copilot impact dashboard
outcome:
  type: productivity
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-09-17-copilot-impact-dashboard-now-shows-feature-engagement
published_at: '2026-09-17'
---

## 概要

Copilot impactダッシュボードに、コード補完・エージェント編集・コードレビュー・CLI・アプリなど機能ごとに28日間で2日以上利用したアクティブユーザー数を表示する機能が追加された。エンタープライズ/組織のレポートAPIでも同じ内訳と、AI導入フェーズごとの28日間ローリング母集団全体を返すよう拡張され、管理者はどの機能が定着し、どこに導入支援が必要かを機能単位で把握できるようになる。

## 設計のポイント

- 集計を『全体のアクティブユーザー数』だけでなく機能別（コード補完・エージェント編集・受動/能動的コードレビュー・CLI・アプリ）に分解し、機能ごとの定着度を可視化する
- ダッシュボードと同じ内訳をレポートAPIでも提供し、社内の独自AI導入ダッシュボードへ組み込めるようにする
- AI導入フェーズの集計を『その日アクティブだったユーザー』だけでなく『その日時点の28日間ローリング母集団全体』でも返すことで、フェーズ間の比較基準を安定させる

## 使いどころ

- Copilotの機能別定着度を見て、どこに研修や設定変更を投下すべきか判断したいエンタープライズ管理者
- 社内向けのAI導入状況ダッシュボードをレポートAPI経由で構築したいプラットフォームチーム
