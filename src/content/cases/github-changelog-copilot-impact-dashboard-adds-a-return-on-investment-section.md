---
type: announcement
title: GitHub Copilot Impact DashboardにROI可視化セクションを追加
title_original: Copilot impact dashboard adds a return on investment section
company: GitHub
industry: cross-industry
cloud: []
patterns:
- cost-optimization
components:
- GitHub Copilot
- Copilot impact dashboard
outcome:
  type: cost
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-08-07-copilot-impact-dashboard-adds-a-return-on-investment-section
published_at: '2026-08-07'
---

## 概要

GitHub CopilotのImpact Dashboardに「投資対効果」セクションが追加され、開発者あたりの月額コストとPR生産量を、Copilot活用度が浅い層とエージェント中心の層で比較できるようになった。給与水準を選択すると人件費に対するコスト比率も再計算され、管理者が投資判断や有効化施策のターゲティングを行いやすくなる。

## 設計のポイント

- 開発者をCopilotの活用フェーズ（受動的利用者 vs エージェント中心の利用者）で分類し、コストとアウトプットを対比させる。
- AIクレジット消費量から実コストを推定し、給与バンドの選択に応じてコスト比率をリアルタイムに再計算する。
- コスト指標はあくまで目安であることを明示し、実際の給与データではなくモデリング入力として扱う設計にしている。

## 使いどころ

- Copilotの投資対効果を経営層に説明し、追加投資を正当化したい管理者。
- 活用フェーズごとの伸びしろを見極め、有効化・トレーニング施策を優先度付けしたいイネーブルメント担当者。
