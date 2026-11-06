---
type: announcement
title: Copilot利用メトリクスのテレメトリ欠落とバージョン不足の検出
title_original: Usage metrics API flags telemetry and version gaps
company: GitHub
industry: cross-industry
cloud: []
patterns:
- llmops
components:
- GitHub Copilot
- Copilot usage metrics API
outcome:
  type: quality
source_id: github-changelog
source_name: GitHub Changelog
source_url: https://github.blog/changelog/2026-11-05-usage-metrics-api-flags-telemetry-and-version-gaps
published_at: '2026-11-06'
---

## 概要

Copilot利用メトリクスAPIに、クライアントテレメトリが届いていないユーザーや、IDE/拡張機能が最小バージョン未満のユーザーを示す項目が追加された。影響ユーザー数を把握し、サポート問い合わせなしで欠落を解消できる。

## 設計のポイント

- ユーザー単位でテレメトリ有無と各IDE/拡張のバージョン適合を持たせ、フォロー対象を特定できる。
- 日次の影響ユーザー数を出し、二つの指標は重複し得るため合算しない設計になっている。
- 値がnullの場合は不明を意味し、falseや0とは区別される。

## 使いどころ

- Copilot利用状況レポートの精度を上げたい管理者。
- プロキシやテレメトリ無効化で欠けるデータを洗い出したい企業。
