---
type: announcement
title: Claude Enterpriseに管理者向けの利用状況分析とコスト管理機能を追加
title_original: Giving admins more visibility and control over Claude spend
company: Anthropic
industry: cross-industry
cloud: []
patterns:
- llmops
- cost-optimization
- multi-model-routing
components:
- Claude Enterprise
- Claude Code
- Analytics API
- Admin API
outcome:
  type: cost
source_id: claude-blog
source_name: Claude Blog
source_url: https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend
published_at: '2026-07-02'
---

## 概要

Anthropicは、Claude Enterpriseの管理者向けに、グループ/ユーザー単位の利用状況とコストを可視化するアナリティクスダッシュボードの拡張、モデルごとの利用権限設定、支出しきい値アラートを追加した。Claude Codeの利用状況の可視化やAnalytics API経由でのDatadog・CloudZeroなど既存のコスト管理ツールとの連携も可能になり、組織全体でAIの利用状況と投資対効果を把握しやすくする。

## 設計のポイント

- 利用状況とコストのデータをダッシュボードのUIだけでなくAnalytics APIとして公開し、Datadog Cloud Cost ManagementやCloudZeroなど既存のFinOpsツールに取り込めるようにすることで、AI支出を他のクラウド/AIコストと同じ土俵で管理できるようにする。
- 組織単位・グループ単位・個人単位という3階層で利用と支出の可視化と上限設定を分離し、SCIMグループなど既存の組織構造をそのまま利用状況の切り口として使えるようにする。
- スレッショルドアラートを管理者（75%/90%）とエンドユーザー（75%/95%）で別々に用意し、いずれも上限到達前に予算引き上げや利用調整の猶予を持たせる設計にする。
- 会話開始時のデフォルトモデルをロールや組織単位で設定できるようにし、日常的な軽作業が常に最上位モデルに流れないようコストの初期値をコントロールする。

## 使いどころ

- 多数のチームでClaudeを横断的に導入しており、部門やユーザー単位でのROIと支出を経営層やCFOに説明する必要がある管理者。
- 既存のクラウド/SaaSコスト管理基盤（Datadog、CloudZeroなど）にAI利用コストも統合したいFinOps/IT部門。
- 多数のグループにまたがる支出上限や増額申請の運用をスクリプトで自動化したい大規模組織の管理者。
